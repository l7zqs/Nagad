import requests
from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/', methods=['GET'])
def check_user_status():
    number = request.args.get('number')
    api_url = f"https://app.mynagad.com:20002/api/user/check-user-status-for-log-in?msisdn={number}"

    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1152",
        "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01",
    }

    response = requests.get(api_url, headers=headers)
    
    return jsonify(response.json())

if name == 'main':
    app.run(debug=True)
