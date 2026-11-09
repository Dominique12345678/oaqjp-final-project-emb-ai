"""Emotion classification through IBM Skills Network's Watson NLP service."""

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_result():
    """Provide the five expected labels when text is invalid."""
    return {**dict.fromkeys(EMOTION_NAMES), "dominant_emotion": None}


def emotion_detector(text_to_analyze):
    """Return emotion scores and dominant emotion for an English statement.

    An empty input or a Watson HTTP 400 response produces None for every
    score and the dominant emotion, as required by the course application.
    Other service failures are raised so they are not reported as emotions.
    """
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()

    response = requests.post(
        EMOTION_URL,
        headers=HEADERS,
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    if response.status_code == 400:
        return _empty_result()
    response.raise_for_status()
    predictions = response.json()["emotionPredictions"]
    scores = predictions[0]["emotion"]
    values = {name: scores[name] for name in EMOTION_NAMES}
    values["dominant_emotion"] = max(EMOTION_NAMES, key=values.get)
    return values
