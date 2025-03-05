from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

spelling_list = {
    # "airplane": "We flew on an airplane to visit our grandparents in Florida.",
    # "await": "We await the arrival of the pizza delivery person with excitement!",
    # "daily": "My dad reads the newspaper daily while he drinks his coffee.",
    # "daycare": "My little sister goes to daycare while Mommy is at work.",
    # "daytime": "Owls sleep during the daytime and hunt at night.",
    # "decay": "If you don't brush your teeth, they will start to decay and get cavities.",
    # "detail": "Can you tell me every detail about your trip to the zoo?",
    # "essay": "We had to write an essay in school about our favorite animal.",
    # "gained": "I gained a new friend when I joined the soccer team.",
    # "getaway": "Our family went on a getaway to the beach for the weekend.",
    # "hairdo": "My sister got a fancy hairdo for the school dance.",
    # "hairy": "My dog is very hairy, and he sheds a lot!",
    # "mayor": "The mayor of our city visited our school today.",
    # "remain": "Please remain seated until the bus comes to a complete stop.",
    # "subway": "In New York City, people take the subway to get around."

  "annoy": "It can annoy my little brother when I take his toys.",
  "employ": "My mom works at a store where they employ many people."
#   ,
#   "loyal": "My dog is very loyal and always stays by my side.",
#   "avoided": "The cat avoided the puddle on the sidewalk.",
#   "enjoyed": "We enjoyed playing games at the birthday party.",
#   "noise": "The loud noise of the fire truck woke me up.",
#   "broil": "My dad will broil the chicken for dinner.",
#   "hoist": "They will hoist the flag up the flagpole.",
#   "oily": "The pizza was oily, but it tasted good.",
#   "choice": "I had a choice between ice cream and cake.",
#   "invoice": "My dad paid the invoice for the new light.",
#   "rejoin": "I will rejoin my friends at the park after school.",
#   "decoy": "The hunter used a decoy to attract the ducks.",
#   "joyful": "The children were joyful when they saw the clown.",
#   "spoiled": "The milk got spoiled because it was left out."
}

 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quiz_data')
def get_quiz_data():
    return jsonify(spelling_list) #send the spelling list as json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True) # Ensure this line is present