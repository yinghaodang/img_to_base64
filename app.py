import base64
from flask import (
    Flask, 
    redirect, 
    request, 
    url_for,
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/image_to_base64', methods=['POST'])
def image_to_base64():
    image = request.files['image']
    image_bytes = image.read()
    base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
    return {"base64": base64_encoded}

if __name__ == '__main__':
    app.run(host='0.0.0.0')