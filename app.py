from fastapi import FastAPI
from intent import compute_intent
from drift import drift_score

app = FastAPI()

@app.post("/detect")
def detect(history: list, recent: list):
    past_intent = compute_intent(history)
    current_intent = compute_intent(recent)

    score = drift_score(past_intent, current_intent)

    verdict = "stable"
    if score > 5:
        verdict = "moderate drift"
    if score > 10:
        verdict = "severe drift"

    return {
        "drift_score": round(score, 2),
        "verdict": verdict,
        "past_intent": past_intent,
        "current_intent": current_intent
    }
