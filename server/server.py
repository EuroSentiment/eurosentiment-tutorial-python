from flask import Flask, Response, request
from lib.simple_sentiment_analyzer import SimpleSentimentAnalyzer
import json

app = Flask(__name__)
sentiment_analyzer = SimpleSentimentAnalyzer()

@app.route("/sentiment", methods=["POST"])
def sentiment():
    input = json.loads(request.data)
    text = input.get("input", "")
    sentiment = sentiment_analyzer.calculate_sentiment(text)
    response = {"@context": "http://eurosentiment.eu/contexts/basecontext.jsonld",
                "@type": "marl:SentimentAnalysis",
                "marl:polarityValue": sentiment}
    return Response(json.dumps(response), mimetype="application/json")

if __name__ == "__main__":
    app.debug = True
    app.run()