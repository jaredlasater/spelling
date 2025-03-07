from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

spelling_list = {
  "unit": {
    "id": 1,
    "name": "2.1",
    "description": "oi, oy",
    "spelling-words": [
      {
        "id": 1,
        "word": "employ",
        "sentence": "My mom works at a store where they employ many people.",
        "state": ""
      }
      ,
      {
        "id": 2,
        "word": "loyal",
        "sentence": "My dog is very loyal and always stays by my side.",
        "state": ""
      }
      # ,
      # {
      #   "id": 3,
      #   "word": "avoided",
      #   "sentence": "The cat avoided the puddle on the sidewalk.",
      #   "state": ""
      # },
      # {
      #   "id": 4,
      #   "word": "enjoyed",
      #   "sentence": "We enjoyed playing games at the birthday party.",
      #   "state": ""
      # },
      # {
      #   "id": 5,
      #   "word": "noise",
      #   "sentence": "The loud noise of the fire truck woke me up.",
      #   "state": ""
      # },
      # {
      #   "id": 6,
      #   "word": "broil",
      #   "sentence": "My dad will broil the chicken for dinner.",
      #   "state": ""
      # },
      # {
      #   "id": 7,
      #   "word": "hoist",
      #   "sentence": "They will hoist the flag up the flagpole.",
      #   "state": ""
      # },
      # {
      #   "id": 8,
      #   "word": "oily",
      #   "sentence": "The pizza was oily, but it tasted good.",
      #   "state": ""
      # },
      # {
      #   "id": 9,
      #   "word": "choice",
      #   "sentence": "I had a choice between ice cream and cake.",
      #   "state": ""
      # },
      # {
      #   "id": 10,
      #   "word": "invoice",
      #   "sentence": "My dad paid the invoice for the new light.",
      #   "state": ""
      # },
      # {
      #   "id": 11,
      #   "word": "rejoin",
      #   "sentence": "I will rejoin my friends at the park after school.",
      #   "state": ""
      # },
      # {
      #   "id": 12,
      #   "word": "decoy",
      #   "sentence": "The hunter used a decoy to attract the ducks.",
      #   "state": ""
      # },
      # {
      #   "id": 13,
      #   "word": "joyful",
      #   "sentence": "The children were joyful when they saw the clown.",
      #   "state": ""
      # },
      # {
      #   "id": 14,
      #   "word": "spoiled",
      #   "sentence": "The milk got spoiled because it was left out.",
      #   "state": ""
      # }
    ]
  }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quiz_data')
def get_quiz_data():
    return jsonify(spelling_list) #send the spelling list as json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True) # Ensure this line is present