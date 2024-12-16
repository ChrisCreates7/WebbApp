from flask import Flask, request, jsonify, render_template, send_file
import requests
import io

app = Flask(__name__)

API_KEY = "QvFJ2PPMV3k66dPDifPNo1G5"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files['image']
    if file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            headers={'X-Api-Key': API_KEY},
            files={'image_file': file},
            data={'size': 'auto'}
        )
        if response.status_code == 200:
            return send_file(io.BytesIO(response.content), mimetype='image/png', as_attachment=False)
        else:
            return jsonify({'error': response.text}), response.status_code
    return jsonify({'error': 'No file uploaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)
