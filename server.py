"""Importing library for emotion detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Analyzer")
@app.route("/emotionDetector")



def sent_analyzer():
    """Analyze the text and return emotion scores."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Try again."
    formatted_output = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, "
            f"and 'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    return formatted_output


@app.route("/")
def render_index_page():
    """Serve the index.html homepage."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
  