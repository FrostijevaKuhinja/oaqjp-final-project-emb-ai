import json
import requests

def emotion_detector(text_to_analyze):

    response = requests.post(
        url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={ "raw_document": { "text": text_to_analyze } }
    )

    #return response
   
    if response.status_code == 400:
        analysis_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
    
    else:
        response_text_dict = json.loads(response.text)

        emotions = response_text_dict["emotionPredictions"][0]["emotion"]

        key_max_score = max(emotions, key = emotions.get)
        
        analysis_result = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': key_max_score
        }
        
    return analysis_result