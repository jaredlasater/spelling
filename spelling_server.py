from flask import Flask, jsonify, render_template, request
from PIL import Image
import base64
import io
import os
from openai import OpenAI

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quiz_data', methods=['POST'])
def process_image():
    # return jsonify('{  "unit": {    "id": 28,    "name": "2.8",    "description": "Words with Long Vowels and Fun Endings",    "spelling-words": [      {        "id": 1,        "word": "afraid",        "sentence": "I was afraid of the dark, so I kept my night light on.",        "state": ""      },      {        "id": 2,        "word": "delay",        "sentence": "We had to delay our picnic because it started to rain.",        "state": ""      },      {        "id": 3,        "word": "safeguard",        "sentence": "I use a lock to safeguard my bike in the schoolyard.",        "state": ""      },      {        "id": 4,        "word": "decayed",        "sentence": "The old apple in the fridge decayed and turned brown.",        "state": ""      },      {        "id": 5,        "word": "faraway",        "sentence": "My grandma lives in a faraway city, but we visit her sometimes.",        "state": ""      },      {        "id": 6,        "word": "greyhound",        "sentence": "A greyhound is a fast dog that likes to run races.",        "state": ""      },      {        "id": 7,        "word": "stagecoach",        "sentence": "In old movies, people travel in a stagecoach pulled by horses.",        "state": ""      },      {        "id": 8,        "word": "outgrow",        "sentence": "I outgrew my shoes, so I need new ones that fit.",        "state": ""      },        {        "id": 9,        "word": "brainstorm",        "sentence": "We had to brainstorm ideas for our class project.",        "state": ""      },      {        "id": 10,        "word": "daydream",        "sentence": "Sometimes I daydream about flying like a superhero.",        "state": ""      },      {        "id": 11,        "word": "breakfast",        "sentence": "I eat cereal for breakfast every morning.",        "state": ""      },      {        "id": 12,        "word": "sunshine",        "sentence": "The sunshine makes the flowers grow in our garden.",        "state": ""      },      {        "id": 13,        "word": "touchdown",        "sentence": "The football player scored a touchdown and everyone cheered.",        "state": ""      },      {        "id": 14,        "word": "scrapbook",        "sentence": "I made a scrapbook with pictures from my birthday party.",        "state": ""      },      {        "id": 15,        "word": "housework",        "sentence": "I help my mom with housework by picking up my toys.",        "state": ""      }    ]  }}')


    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    
    # Open image with Pillow
    try:
        img = Image.open(image_file)
        
        # Convert to grayscale (reduces size significantly)
        img = img.convert('L')  # 'L' mode is 8-bit grayscale
        
        # Resize to a smaller resolution (e.g., 300px max dimension)
        max_size = 300
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        # Optional: Convert to 1-bit black/white (even smaller size, but less detail)
        # img = img.convert('1')  # Uncomment if you want pure black/white
        
        # Save to a bytes buffer with low quality JPEG compression
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=20)  # Low quality for smaller size
        buffer.seek(0)
        
        # Base64 encode the compressed image
        base64_encoded = base64.b64encode(buffer.read()).decode('utf-8')

        XAI_API_KEY = os.getenv("XAI_API_KEY")
        if not XAI_API_KEY:
            raise ValueError("XAI_API_KEY environment variable is not set.")
        
        print("XAI_API_KEY: " +  XAI_API_KEY)
        
        client = OpenAI(
            api_key=XAI_API_KEY,
            base_url="https://api.x.ai/v1",
        )

        unit_id = 28;
        unit_name = "2.8";
        unit_description = "Words with Long Vowels and Fun Endings";
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_encoded}",
                            "detail": "high",
                        },
                    },
                    {
                        "type": "text",
                        "text": "There is a table at the bottom of this image. The image may be rotated. Take each word in the table and generate a sentence that is appropriate for a second grader. Place the word and sentence in the spelling-words array. Return a JSON object with the following structure and only the JSON object. : "
                                f"{{"
                                f"  \"unit\": {{"
                                f"    \"id\": {unit_id},"
                                f"    \"name\": \"{unit_name}\","
                                f"    \"description\": \"{unit_description}\","
                                f"    \"spelling-words\": ["
                                f"      {{"
                                f"        \"id\": <unique_id>,"
                                f"        \"word\": <word>,"
                                f"        \"sentence\": <sentence appropriate for a second grader>,"
                                f"        \"state\": \"\""
                                f"      }}"
                                f"    ]"
                                f"  }}"
                                f"}}"
                        ,
                    },
                ],
            },
        ]

        grok_response = client.chat.completions.create(
            model="grok-2-vision-latest",
            messages=messages,
            temperature=0.01,
        ).model_dump()

        content = grok_response["choices"][0]["message"]["content"]

        if content.startswith("```json"):
            content = content[7:-3].strip()  # Remove the ```json and ``` markers

        return jsonify(content)
    
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500



if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
