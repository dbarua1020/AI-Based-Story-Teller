# app.py
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = #Enter API KEY here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story():
    # Get user input from the form
    user_input = request.form['prompt']

    # Generate story using GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use 'gpt-3.5-turbo' if available
        prompt=f"Write a short story about: {user_input}",
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated story
    story = response.choices[0].text.strip()

    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True)
