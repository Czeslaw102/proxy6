from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Adres docelowy serwera, na który będzie przekierowywany cały ruch
TARGET_SERVER = 'http://wp.pl'

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'GET':
        response = requests.get(TARGET_SERVER)
    elif request.method == 'POST':
        data = request.form.get('data', '')
        headers = {'Content-Type': 'application/json'} # adjust content type if needed
        response = requests.post(TARGET_SERVER, data=data, headers=headers)
    
    return Response(response.content, response.status_code)

if __name__ == '__main__':
    app.run(debug=True)
