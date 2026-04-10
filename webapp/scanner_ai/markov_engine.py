import pandas as pd
import numpy as np

STATES = ["Discovered", "Verified", "Exploitable", "Fixed"]

class ThreatMarkovAI:
    def _init_(self):
        self.matrix = pd.read_csv("scanner_ai/markov_transition_matrix.csv", index_col=0).values

    def predict_next(self, state):
        idx = STATES.index(state)
        probs = self.matrix[idx]
        return {STATES[i]: round(probs[i], 4) for i in range(len(STATES))}

    def predict_n_steps(self, state, steps=3):
        state_vector = np.zeros(len(STATES))
        state_vector[STATES.index(state)] = 1

        temp_matrix = self.matrix.copy()
        for _ in range(steps):
            state_vector = state_vector @ temp_matrix

        return {STATES[i]: round(state_vector[i], 4) for i in range(len(STATES))}