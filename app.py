from flask import Flask, request, send_file, jsonify, url_for
from stegano import lsb
from vigenerer_chiper import *
from uuid import uuid4

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Stegonografi API'
    })


@app.route('/api/hide', methods=['POST'])
def hide():
    message = request.form['message']
    key = request.form['key']
    image = request.files['image']
    file_name = 'image_' + str(uuid4()) + '.png'
    image_path = 'static/' + file_name

    # Encrypt text
    message = vigenere_encrypt(message, key)

    # Hide the message in the image
    secret_image = lsb.hide(image.stream, message)
    secret_image.save(image_path)

    # return send_file(image_path)
    image_url = url_for('static', filename=file_name, _external=True)

    return jsonify({
        'data': {
            'image': f"{image_url}"
        },
    })


@app.route('/api/reveal', methods=['POST'])
def reveal():
    key = request.form['key']
    image = request.files['image']

    # Reveal the hidden message
    hidden_message = lsb.reveal(image.stream)

    # Decrypt text
    hidden_message = vigenere_decrypt(hidden_message, key)

    return jsonify({
        'data': {
            'message': f"{hidden_message}"
        }
    })


if __name__ == '__main__':
    app.run(port=3000, debug=True)
