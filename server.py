"""
Main server module to serve the EmotionDetection project
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """
    This route renders the index page
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def get_emotion_details():
    """
    This route calls emotion_detection module
    of the EmotionDetection package to get emotion details
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    # pylint: disable=line-too-long
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
