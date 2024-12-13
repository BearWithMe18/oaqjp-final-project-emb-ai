import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inputObj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=inputObj, headers=header)
    formatted_response = json.loads(response.text)

    try:
        text = formatted_response['emotionPredictions'][0]['emotion']
    except:
        text = {}
        text['joy'] = "None"
    if (response.status_code == 400):
        for key in text:
            text[key] = "None"

    return text