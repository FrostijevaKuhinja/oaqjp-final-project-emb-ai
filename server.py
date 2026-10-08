"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_homepage():
    """Render the application's homepage."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_analysis():
    """Analyze user input and return formatted emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"


    emotion_names = ["anger", "disgust", "fear", "joy", "sadness"]

    formatted_emotions = [
        f"'{emotion}': {analysis_result[emotion]}"
        for emotion in emotion_names
    ]


    emotion_summary = (
        ", ".join(formatted_emotions[:-1])
        + " and "
        + formatted_emotions[-1]
    )

    dominant_emotion = analysis_result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"{emotion_summary}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
