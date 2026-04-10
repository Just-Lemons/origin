import json
from urllib.parse import urlparse
import requests 
from django.shortcuts import render
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
import io

SCANNER_API_URL = "http://127.0.0.1:8001/scan"


def home(request):
    return render(request, "home.html")


def output_view(request):
    raw_url = (request.GET.get("url") or "").strip()

    if not raw_url:
        return render(
            request,
            "output.html",
            {
                "url": "",
                "data": None,
                "raw_json": "",
                "summary_cards": [],
                "error": "Please enter a website URL or domain name.",
            },
        )

    # Allow both domains and full URLs
    parsed = urlparse(raw_url)
    if not parsed.scheme:
        raw_url = "https://" + raw_url

    try:
        response = requests.get(
            SCANNER_API_URL,
            params={"url": raw_url},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as exc:
        return render(
            request,
            "output.html",
            {
                "url": raw_url,
                "data": None,
                "raw_json": "",
                "summary_cards": [],
                "error": f"Scanner service error: {exc}",
            },
        )
    except ValueError:
        return render(
            request,
            "output.html",
            {
                "url": raw_url,
                "data": None,
                "raw_json": "",
                "summary_cards": [],
                "error": "Scanner returned invalid JSON.",
            },
        )

    summary_cards = []

    if isinstance(data, dict):
        key_map = [
            ("status", "Status"),
            ("target", "Target"),
            ("severity", "Severity"),
            ("risk", "Risk"),
            ("score", "Score"),
            ("message", "Message"),
        ]

        for key, label in key_map:
            value = data.get(key)
            if value not in (None, "", [], {}):
                summary_cards.append(
                    {
                        "label": label,
                        "value": value,
                    }
                )

        findings = data.get("findings") or data.get("vulnerabilities") or data.get("issues")
        if isinstance(findings, list):
            summary_cards.append(
                {
                    "label": "Findings",
                    "value": len(findings),
                }
            )

    raw_json = json.dumps(data, indent=2, ensure_ascii=False)

    return render(
        request,
        "output.html",
        {
            "url": raw_url,
            "data": data,
            "raw_json": raw_json,
            "summary_cards": summary_cards,
            "error": None,
        },  
    )

def generate_pdf_report(data, url):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph(f"Security Scan Report", styles["Title"]))
    content.append(Spacer(1, 10))

    # Target
    content.append(Paragraph(f"<b>Target:</b> {url}", styles["Normal"]))
    content.append(Spacer(1, 10))

    # Summary
    content.append(Paragraph("<b>Summary:</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    for key, value in data.items():
        if key != "vulnerabilities":
            content.append(Paragraph(f"{key}: {value}", styles["Normal"]))
            content.append(Spacer(1, 5))

    # Vulnerabilities
    vulns = data.get("vulnerabilities", [])

    content.append(Spacer(1, 15))
    content.append(Paragraph("<b>Vulnerabilities Found:</b>", styles["Heading2"]))
    content.append(Spacer(1, 10))

    if vulns:
        for v in vulns:
            content.append(Paragraph(f"Type: {v.get('type')}", styles["Normal"]))
            content.append(Paragraph(f"Status: {v.get('status')}", styles["Normal"]))

            if "issues" in v:
                content.append(Paragraph(f"Issues: {', '.join(v['issues'])}", styles["Normal"]))

            content.append(Spacer(1, 10))
    else:
        content.append(Paragraph("No vulnerabilities detected.", styles["Normal"]))

    doc.build(content)

    buffer.seek(0)
    return buffer

def download_report(request):
    raw_url = request.GET.get("url")

    if not raw_url:
        return HttpResponse("No URL provided", status=400)

    try:
        response = requests.get(SCANNER_API_URL, params={"url": raw_url})
        data = response.json()
    except:
        return HttpResponse("Error fetching scan data", status=500)

    pdf_buffer = generate_pdf_report(data, raw_url)

    response = HttpResponse(pdf_buffer, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="report.pdf"'

    return response 