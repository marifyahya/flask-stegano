from flask import Flask, request, send_file, jsonify, url_for
from marshmallow import Schema, fields, ValidationError
from stegano import lsb
from vigenerer_chiper import *
from uuid import uuid4

app = Flask(__name__)

class HideSchema(Schema):
    message = fields.String(required=True, validate=lambda x: len(x) >= 1, error_messages={
                            "required": "Message is required.", "validator_failed": "Message must be at least 1 characters long."})
    key = fields.String(required=True, validate=lambda x: len(x) >= 1, error_messages={
                        "required": "Name is required.", "validator_failed": "Key must be at least 1 characters long."})


class RevealSchema(Schema):
    key = fields.String(required=True, validate=lambda x: len(x) >= 1, error_messages={
                        "required": "Name is required.", "validator_failed": "Key must be at least 1 characters long."})


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Stegonografi API'
    })


@app.route('/api/hide', methods=['POST'])
def hide():
    hide_schema = HideSchema()

    try:
        hide_schema.load(request.form)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    image_validate = image_validation(request)
    if (image_validate):
        return jsonify(image_validate), 400

    image = request.files['image']
    file_name = 'image_' + str(uuid4()) + '.png'
    image_path = 'static/' + file_name

    message = request.form['message']
    key = request.form['key']

    message = vigenere_encrypt(message, key)

    secret_image = lsb.hide(image.stream, message)
    secret_image.save(image_path)

    image_url = url_for('static', filename=file_name, _external=True)

    return jsonify({
        'data': {
            'image': f"{image_url}"
        },
    })


@app.route('/api/reveal', methods=['POST'])
def reveal():
    reveal_schema = RevealSchema()

    try:
        reveal_schema.load(request.form)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    if 'image' not in request.files:
        return jsonify({'errors': {'image': ['Image file is required.']}}), 400

    image_validate = image_validation(request)
    if (image_validate):
        return jsonify(image_validate), 400

    image = request.files['image']
    key = request.form['key']

    hidden_message = lsb.reveal(image.stream)
    hidden_message = vigenere_decrypt(hidden_message, key)

    return jsonify({
        'data': {
            'message': f"{hidden_message}"
        }
    })


def allowed_file(filename):
    allowed_extension = {'png', 'jpg', 'jpeg', 'webp'}

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extension


def image_validation(request):
    if 'image' not in request.files:
        return {'errors': {'image': ['Image file is required.']}}

    image = request.files['image']

    if image.filename == '':
        return {'errors': {'image': ['No selected file.']}}

    if not allowed_file(image.filename):
        return {'errors': {
            'image': ['Invalid file type. Allowed types: png, jpg, jpeg, gif.']}}

    return None


if __name__ == '__main__':
    app.run(port=3000, debug=True)
