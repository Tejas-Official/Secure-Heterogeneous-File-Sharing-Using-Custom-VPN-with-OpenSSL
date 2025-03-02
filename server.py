from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    files = request.files.getlist('files')
    for file in files:
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))

    return jsonify({'message': 'Files successfully uploaded'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
