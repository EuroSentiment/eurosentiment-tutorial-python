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

ELECTRONICS_POSITIVE_ENTRIES = "PREFIX lemon: <http://lemon-model.net/lemon#> PREFIX marl: <http://purl.org/marl/ns/> SELECT ?wordWithSentiment from <http://www.eurosentiment.eu/dataset/electronics/%s/paradigma/lexicon> 	where { 	?entry lemon:sense ?sense . 	?sense marl:polarityValue ?polarityValue . 	?sense marl:hasPolarity <http://purl.org/marl/ns/positive> . 	?sense lemon:reference ?reference .                  ?entryWithSentiment lemon:sense ?context.                 ?entryWithSentiment lemon:canonicalForm ?cf.                 ?cf lemon:writtenRep ?wordWithSentiment.  	} GROUP BY ?wordWithSentiment"
ELECTRONICS_NEGATIVE_ENTRIES = "PREFIX lemon: <http://lemon-model.net/lemon#> PREFIX marl: <http://purl.org/marl/ns/> SELECT ?wordWithSentiment from <http://www.eurosentiment.eu/dataset/electronics/%s/paradigma/lexicon> 	where { 	?entry lemon:sense ?sense . 	?sense marl:polarityValue ?polarityValue . 	?sense marl:hasPolarity <http://purl.org/marl/ns/negative> . 	?sense lemon:reference ?reference .                  ?entryWithSentiment lemon:sense ?context.                 ?entryWithSentiment lemon:canonicalForm ?cf.                 ?cf lemon:writtenRep ?wordWithSentiment.  	} GROUP BY ?wordWithSentiment"
HOTEL_POSITIVE_ENTRIES = "PREFIX lemon: <http://lemon-model.net/lemon#> PREFIX marl: <http://purl.org/marl/ns/> SELECT ?wordWithSentiment from <http://www.eurosentiment.eu/dataset/hotel/%s/paradigma/lexicon> 	where { 	?entry lemon:sense ?sense . 	?sense marl:polarityValue ?polarityValue . 	?sense marl:hasPolarity <http://purl.org/marl/ns/positive> . 	?sense lemon:reference ?reference .                  ?entryWithSentiment lemon:sense ?context.                 ?entryWithSentiment lemon:canonicalForm ?cf.                 ?cf lemon:writtenRep ?wordWithSentiment.  	} GROUP BY ?wordWithSentiment"
HOTEL_NEGATIVE_ENTRIES = "PREFIX lemon: <http://lemon-model.net/lemon#> PREFIX marl: <http://purl.org/marl/ns/> SELECT ?wordWithSentiment from <http://www.eurosentiment.eu/dataset/hotel/%s/paradigma/lexicon> 	where { 	?entry lemon:sense ?sense . 	?sense marl:polarityValue ?polarityValue . 	?sense marl:hasPolarity <http://purl.org/marl/ns/negative> . 	?sense lemon:reference ?reference .                  ?entryWithSentiment lemon:sense ?context.                 ?entryWithSentiment lemon:canonicalForm ?cf.                 ?cf lemon:writtenRep ?wordWithSentiment.  	} GROUP BY ?wordWithSentiment"
