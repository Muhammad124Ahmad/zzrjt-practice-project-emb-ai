"""Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


app = Flask(__name__)


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    text = request.args.get("textToAnalyze")
    result = sentiment_analyzer(text)
    return (f"The given text has been identified as {result['label']} with a score of {result['score']}")


@app.route("/")
def render_index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
