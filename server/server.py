from flask import Flask, Response, request
from lib.simple_sentiment_analyzer import SimpleSentimentAnalyzer
import json

app = Flask(__name__)
sentiment_analyzer = SimpleSentimentAnalyzer()

@app.route("/sentiment", methods=["POST"])
def sentiment():
    input = json.loads(request.data)
    response = input
    return Response(json.dumps(response), mimetype="application/json")

if __name__ == "__main__":
    app.debug = True
    app.run()