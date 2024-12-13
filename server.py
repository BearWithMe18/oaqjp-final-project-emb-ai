''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5001.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
    runs sentiment analysis over it using emotion_detector()
    function. The output returned shows the label and its confidence 
    score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['joy'] == "None":
        response['dominant_emotion'] = "None"
    else:
        response['dominant_emotion'] = max(response, key=response.get)

    if response['dominant_emotion'] == "None":
        return "Invalid text! Please try again!"

    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #I have an issue with port 5000 from the practice project
    #So I moved this to port 5001
    app.run(host="0.0.0.0", port=5001)