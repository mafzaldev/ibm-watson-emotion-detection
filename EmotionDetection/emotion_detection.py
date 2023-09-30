import json
import requests


def emotion_detector(text_to_analyze):
    emotions = {}
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 400:
        emotions["anger"] = None
        emotions["disgust"] = None
        emotions["joy"] = None
        emotions["fear"] = None
        emotions["sadness"] = None
        emotions["dominant_emotion"] = None
    else:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
    return emotions