from flask import Flask, jsonify, render_template, request
import os
import requests

app = Flask(__name__)

spelling_list = {
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quiz_data')
def get_quiz_data():
    return jsonify(spelling_list)  # Send the spelling list as JSON

@app.route('/generate_sentences', methods=['POST'])
def generate_sentences():
    print("Received request for /generate_sentences")

    data = request.json
    words = data.get('words', [])
    unit_id = data.get('unit_id', 1)  # Default to 1 if not provided
    unit_name = data.get('unit_name', "Generated Unit")  # Default to "Generated Unit" if not provided
    unit_description = data.get('unit_description', "Generated sentences for the provided words")  # Default description

    if not words:
        return jsonify({"error": "No words provided"}), 400

    # Construct the prompt
    prompt = (
        f"Generate a JSON object with the following structure:\n"
        f"{{\n"
        f"  \"unit\": {{\n"
        f"    \"id\": {unit_id},\n"
        f"    \"name\": \"{unit_name}\",\n"
        f"    \"description\": \"{unit_description}\",\n"
        f"    \"spelling-words\": [\n"
        f"      {{\n"
        f"        \"id\": <unique_id>,\n"
        f"        \"word\": <word>,\n"
        f"        \"sentence\": <sentence appropriate for a second grader>,\n"
        f"        \"state\": \"\"\n"
        f"      }}\n"
        f"    ]\n"
        f"  }}\n"
        f"}}\n\n"
        f"Generate this JSON object for the following words: {', '.join(words)}. Only return the JSON object in the response."
    )

    # Construct the payload for Grok's API
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "model": "grok-2-latest",
        "stream": False,
        "temperature": 0
    }

    # Output the payload to the console
    print("Payload being sent to Grok API:", payload)

    try:
        # Make a POST request to Grok's API
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",  # Grok's API endpoint
            headers={
                "Authorization": f"Bearer {"xai-"}",  # Replace with your actual API key
                "Content-Type": "application/json"
            },
            json=payload
        )
        response.raise_for_status()  # Raise an error for HTTP errors

        # Extract the content from the response
        grok_response = response.json()
        content = grok_response["choices"][0]["message"]["content"]

        # Parse the JSON content (removing the code block markers if present)
        if content.startswith("```json"):
            content = content[7:-3].strip()  # Remove the ```json and ``` markers

        # Return the parsed JSON content
        return jsonify(content)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request failed: {e}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
