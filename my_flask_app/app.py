from flask import Flask, request, jsonify, render_template
import google.generativeai as ai

app = Flask(__name__)

API_KEY = 'AIzaSyCuFSkr8q6cFBxtovZS436G1cBqKVKh0kk' 
ai.configure(api_key=API_KEY)
model = ai.GenerativeModel("gemini-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    chat = model.start_chat()
    response = chat.send_message(user_message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)
