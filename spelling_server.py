from flask import Flask, jsonify, render_template
import os


app = Flask(__name__)

spelling_list = {
  "spelling_list": {
    "unit": {
      "id": 28,
      "name": "2.8",
      "description": "Words with Long Vowels and Fun Endings",
      "spelling-words": [
        {
          "id": 1,
          "word": "avoided",
          "sentence": "She avoided the puddle so her shoes stayed dry.",
          "state": ""
        },
        {
          "id": 2,
          "word": "daily",
          "sentence": "He brushes his teeth daily to keep them clean.",
          "state": ""
        },
        {
          "id": 3,
          "word": "defeat",
          "sentence": "The team worked hard to defeat their opponents.",
          "state": ""
        },
        {
          "id": 4,
          "word": "enjoyed",
          "sentence": "We enjoyed playing outside on the sunny day.",
          "state": ""
        },
        {
          "id": 5,
          "word": "explode",
          "sentence": "The balloon will explode if you blow it up too much.",
          "state": ""
        },
        {
          "id": 6,
          "word": "gained",
          "sentence": "She gained a new friend at school today.",
          "state": ""
        },
        {
          "id": 7,
          "word": "getaway",
          "sentence": "The cat made a quick getaway from the dog.",
          "state": ""
        },
        {
          "id": 8,
          "word": "idea",
          "sentence": "He had a great idea for a fun game.",
          "state": ""
        },
        {
          "id": 9,
          "word": "outgrow",
          "sentence": "I outgrow my shoes because my feet get bigger.",
          "state": ""
        },
        {
          "id": 10,
          "word": "phrase",
          "sentence": "‘Good job’ is a nice phrase to say.",
          "state": ""
        },
        {
          "id": 11,
          "word": "produce",
          "sentence": "Farmers produce yummy fruits and vegetables.",
          "state": ""
        },
        {
          "id": 12,
          "word": "revenge",
          "sentence": "He didn’t want revenge; he just wanted to play fair.",
          "state": ""
        },
        {
          "id": 13,
          "word": "toaster",
          "sentence": "Mom put bread in the toaster for breakfast.",
          "state": ""
        },
        {
          "id": 14,
          "word": "unseen",
          "sentence": "The kitten hid in an unseen spot under the bed.",
          "state": ""
        },
        {
          "id": 15,
          "word": "yogurt",
          "sentence": "I like to eat yogurt with fruit for a snack.",
          "state": ""
        }
      ]
    }
  }
}



# spelling_list = {
#   "unit": {
#     "id": 27,
#     "name": "2.7",
#     "description": "Vowel Teams OW & OA",
#     "spelling-words": [
#       {
#         "id": 1,
#         "word": "arrow",
#         "sentence": "The arrow pointed to the treasure on the map.",
#         "state": ""
#       },
#       {
#         "id": 2,
#         "word": "boast",
#         "sentence": "My friend likes to boast about his fast bike.",
#         "state": ""
#       },
#       {
#         "id": 3,
#         "word": "cloak",
#         "sentence": "The superhero wore a red cloak that flapped in the wind.",
#         "state": ""
#       },
#       {
#         "id": 4,
#         "word": "floated",
#         "sentence": "My boat floated on the water at the lake.",
#         "state": ""
#       },
#       {
#         "id": 5,
#         "word": "follow",
#         "sentence": "I follow my teacher to the lunchroom every day.",
#         "state": ""
#       },
#       {
#         "id": 6,
#         "word": "groan",
#         "sentence": "I heard a groan when my brother stubbed his toe.",
#         "state": ""
#       },
#       {
#         "id": 7,
#         "word": "oatmeal",
#         "sentence": "Mom made warm oatmeal with honey for breakfast.",
#         "state": ""
#       },
#       {
#         "id": 8,
#         "word": "outgrow",
#         "sentence": "I outgrow my shoes because my feet get bigger.",
#         "state": ""
#       },
#       {
#         "id": 9,
#         "word": "pillow",
#         "sentence": "My soft pillow helps me sleep at night.",
#         "state": ""
#       },
#       {
#         "id": 10,
#         "word": "raincoat",
#         "sentence": "I wear my raincoat when it rains on my way to school.",
#         "state": ""
#       },
#       {
#         "id": 11,
#         "word": "shadow",
#         "sentence": "My shadow follows me when I walk in the sun.",
#         "state": ""
#       },
#       {
#         "id": 12,
#         "word": "soapy",
#         "sentence": "My hands got soapy when I washed the dishes.",
#         "state": ""
#       },
#       {
#         "id": 13,
#         "word": "throwing",
#         "sentence": "We had fun throwing a ball at the park.",
#         "state": ""
#       },
#       {
#         "id": 14,
#         "word": "toaster",
#         "sentence": "The toaster popped up my bread for breakfast.",
#         "state": ""
#       },
#       {
#         "id": 15,
#         "word": "yellow",
#         "sentence": "The yellow sun shines bright in the sky.",
#         "state": ""
#       }
#     ]
#   }
# }
# spelling_list = {

#     "unit": {
#         "id": 2,
#         "name": "2.6",
#         "description": "Vowel Teams EA & EE",
#         "spelling-words": [{
#         "id": 1,
#         "word": "defeat",
#         "sentence": "We can defeat the other team if we try our best.",
#         "state": ""
#       },
#       {
#         "id": 2,
#         "word": "unreal",
#         "sentence": "The dragon in my book looks unreal but so cool!",
#         "state": ""
#       },
#       {
#         "id": 3,
#         "word": "sixteen",
#         "sentence": "I counted sixteen balloons at the party.",
#         "state": ""
#       },
#       {
#         "id": 4,
#         "word": "mistreat",
#         "sentence": "It’s not nice to mistreat your toys by throwing them.",
#         "state": ""
#       },
#       {
#         "id": 5,
#         "word": "degree",
#         "sentence": "My teacher has a degree to teach us fun things.",
#         "state": ""
#       },
#       {
#         "id": 6,
#         "word": "unseen",
#         "sentence": "The bug was unseen because it hid under a leaf.",
#         "state": ""
#       },
#       {
#         "id": 7,
#         "word": "wheat",
#         "sentence": "Bread is made from wheat that grows in fields.",
#         "state": ""
#       },
#       {
#         "id": 8,
#         "word": "disagree",
#         "sentence": "I disagree with my friend about the best color.",
#         "state": ""
#       },
#       {
#         "id": 9,
#         "word": "agreed",
#         "sentence": "We agreed to play tag at recess today.",
#         "state": ""
#       },
#       {
#         "id": 10,
#         "word": "ordeal",
#         "sentence": "Cleaning my messy room was a big ordeal!",
#         "state": ""
#       },
#       {
#         "id": 11,
#         "word": "spree",
#         "sentence": "We went on a fun spree picking out candy.",
#         "state": ""
#       },
#       {
#         "id": 12,
#         "word": "breed",
#         "sentence": "The farmer wants to breed cows on his farm.",
#         "state": ""
#       },
#       {
#         "id": 13,
#         "word": "squeal",
#         "sentence": "I heard a squeal when my sister saw a mouse.",
#         "state": ""
#       },
#       {
#         "id": 14,
#         "word": "sheen",
#         "sentence": "My new shoes have a shiny sheen I like.",
#         "state": ""
#       },
#       {
#         "id": 15,
#         "word": "indeed",
#         "sentence": "It is indeed a sunny day to play outside.",
#         "state": ""
#       }
#         ]
#     }

# }
# spelling_list = {
#   "unit": {
#     "id": 1,
#     "name": "2.1",
#     "description": "oi, oy", 
#     "spelling-words": [
#       {
#         "id": 1,
#         "word": "employ",
#         "sentence": "My mom works at a store where they employ many people.",
#         "state": ""
#       }
#       ,
#       {
#         "id": 2,
#         "word": "loyal",
#         "sentence": "My dog is very loyal and always stays by my side.",
#         "state": ""
#       }
#       ,
#       {
#         "id": 3,
#         "word": "avoided",
#         "sentence": "The cat avoided the puddle on the sidewalk.",
#         "state": ""
#       },
#       {
#         "id": 4,
#         "word": "enjoyed",
#         "sentence": "We enjoyed playing games at the birthday party.",
#         "state": ""
#       },
#       {
#         "id": 5,
#         "word": "noise",
#         "sentence": "The loud noise of the fire truck woke me up.",
#         "state": ""
#       },
#       {
#         "id": 6,
#         "word": "broil",
#         "sentence": "My dad will broil the chicken for dinner.",
#         "state": ""
#       },
#       {
#         "id": 7,
#         "word": "hoist",
#         "sentence": "They will hoist the flag up the flagpole.",
#         "state": ""
#       },
#       {
#         "id": 8,
#         "word": "oily",
#         "sentence": "The pizza was oily, but it tasted good.",
#         "state": ""
#       },
#       {
#         "id": 9,
#         "word": "choice",
#         "sentence": "I had a choice between ice cream and cake.",
#         "state": ""
#       },
#       {
#         "id": 10,
#         "word": "invoice",
#         "sentence": "My dad paid the invoice for the new light.",
#         "state": ""
#       },
#       {
#         "id": 11,
#         "word": "rejoin",
#         "sentence": "I will rejoin my friends at the park after school.",
#         "state": ""
#       },
#       {
#         "id": 12,
#         "word": "decoy",
#         "sentence": "The hunter used a decoy to attract the ducks.",
#         "state": ""
#       },
#       {
#         "id": 13,
#         "word": "joyful",
#         "sentence": "The children were joyful when they saw the clown.",
#         "state": ""
#       },
#       {
#         "id": 14,
#         "word": "spoiled",
#         "sentence": "The milk got spoiled because it was left out.",
#         "state": ""
#       }
#     ]
#   }
# }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quiz_data')
def get_quiz_data():
    return jsonify(spelling_list) #send the spelling list as json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True) # Ensure this line is present
