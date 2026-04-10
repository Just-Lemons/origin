#  AI-Powered Web Vulnerability Scanner  
A lightweight web-based platform that scans websites for critical security vulnerabilities and provides contextual AI-driven explanations.

---

## 1. Problem Statement

Modern web applications rely on complex architectures such as Single Page Applications (SPAs), APIs, and microservices. Existing tools like OWASP ZAP and Burp Suite are effective at detecting known vulnerabilities but lack contextual understanding of application behavior, workflows, and developer usability. They often produce high false positives and do not provide actionable explanations.

This project aims to build a unified, intelligent platform that performs automated vulnerability scanning while enhancing results with contextual insights and simplified reporting for developers.

---

## 2. Features

-  **Automated Vulnerability Scanning**  
  Scans a given website URL for multiple security vulnerabilities.

-  **SQL Injection Detection**  
  Injects test payloads and detects potential database-related errors.

-  **Reflected XSS Detection**  
  Identifies script injection vulnerabilities by analyzing response reflections.

-  **Broken Authentication Check**  
  Attempts unauthorized access to protected endpoints.

-  **Open Redirect Detection**  
  Detects unsafe redirect mechanisms using manipulated query parameters.

-  **Security Misconfiguration Analysis**  
  Checks for missing HTTP security headers and insecure protocols.

-  **Web Dashboard Interface**  
  User-friendly Django-based UI to input URLs and view scan results.

---

## 3. Tech Stack

### Backend
- Python
- FastAPI (Scanning Engine)
- Django (Web Framework)
- Requests (HTTP handling)

### Frontend
- HTML
- CSS
- Django Templates

### Optional / Planned
- BeautifulSoup (Crawler)
- Ollama (AI explanation layer)

---

## 4. Project Structure
origin/
│
│-- Cyber/ # Virtual Environment
├── scanner/ # FastAPI-based scanning engine
│ └── main.py # Core vulnerability detection logic
│
├── webapp/ # Django project
│ ├── manage.py
│ ├── webapp/ # Django settings & config
│ └── dashboard/ # Main UI app
│ ├── views.py # Connects UI to FastAPI
│ ├── urls.py # Routing
│ └── templates/ # HTML UI files
│ └── home.html # Main dashboard page


---

## 5. Installation & Setup

### Step 1: Clone Repository
git clone <your-repo-url>
cd origin

### Step 2: Create Virtual Environment
python -m venv cyber
source cyber/bin/activate # Linux/Mac
cyber\Scripts\activate # Windows

### Step 3: Install Dependencies
pip install fastapi uvicorn django requests

### Step 4: Run FastAPI Scanner
cd scanner
uvicorn main:app --reload

### Step 5: Run Django Server
cd ../webapp
python manage.py runserver

### Step 6: Open Application


---

## 6. How It Works(Main Functionality)

1. User enters a target URL in the Django web interface  
2. Django sends a request to the FastAPI `/scan` endpoint  
3. FastAPI executes multiple vulnerability tests:
   - SQL Injection
   - XSS
   - Authentication
   - Redirect
   - Header checks  
4. Each test sends crafted HTTP requests using payloads  
5. Responses are analyzed for anomalies or reflections  
6. Results are returned as JSON  
7. Django renders results on the dashboard  

---

## 7. Scalability

-  **Modular Architecture**  
  FastAPI and Django separation allows independent scaling.

-  **Async Support (Future)**  
  FastAPI can be extended to run concurrent scans.

-  **Cloud Deployment Ready**  
  Can be containerized using Docker and deployed on cloud platforms.

-  **Multi-Target Scanning (Future)**  
  Queue-based system can handle multiple users simultaneously.

---

## 8. Feasibility

- Built using lightweight and widely used tools (Python, FastAPI, Django)  
- Requires no heavy infrastructure for initial deployment  
- Easily extensible with additional scanning modules  
- Can be integrated into CI/CD pipelines for automated testing  

---

## 9. Novelty

Unlike traditional tools that only detect vulnerabilities, this project focuses on:

- Providing **context-aware explanations (AI integration planned)**  
- Simplifying vulnerability understanding for developers  
- Combining scanning + reporting + explainability in one platform  

It bridges the gap between **technical security tools and developer usability**.

---

## 10. Feature Depth(Scope)

- Payload-based testing simulates real-world attack scenarios  
- Multiple vulnerability types covered across different layers  
- Response-based detection ensures lightweight analysis  
- Header analysis detects configuration-level weaknesses  
- Modular functions allow easy extension for new vulnerabilities  

---

## 11. Ethical Use & Disclaimer

This tool is intended strictly for **educational purposes and authorized security testing only**.

- Do NOT scan websites without permission  
- Unauthorized scanning may violate legal and ethical guidelines  
- The authors are not responsible for misuse of this tool  

---

## 12. Author

**Team Lexicon**  
📧 Email: april.appy24@gmail.com
🔗 GitHub: https://github.com/Just-Lemons/origin

---
