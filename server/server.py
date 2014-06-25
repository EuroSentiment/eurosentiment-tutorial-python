# encoding: utf-8
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#  The original code are licensed under the GNU Lesser General Public License.

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

from flask import Flask, Response, request
from simple_sentiment_analyzer import SimpleSentimentAnalyzer
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