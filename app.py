from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
from rag import main
import os
import uuid

app = Flask(__name__)
app.secret_key = os.urandom(24)  

@app.route('/')
def index():
    return render_template('index.html', conversation=None, chat_history=[])


@app.route('/chat', methods=['POST'])
def query():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

    if 'file_input' in request.files and request.files['file_input'].filename != '':
        uploaded_file = request.files['file_input']
        file_path = secure_filename(uploaded_file.filename)
        uploaded_file.save(file_path)
        session['file_path'] = file_path
    elif 'file_path' in session:
        file_path = session['file_path']
    
    message = request.form['message']

    chat_history, bot_response = main(file_path, message, session['session_id'])

    return render_template('index.html', conversation=bot_response, chat_history=chat_history)
    
if __name__ == '__main__':
    app.run(debug=True)