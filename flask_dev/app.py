# Flask Backend
from flask import Flask, render_template, request, jsonify
from weather import get_response, parse_cwa_current_data, parse_cwa_past_data
from dotenv import load_dotenv
import os
import logging
import requests

app = Flask(__name__)
load_dotenv()
logger = logging.getLogger(__name__)

### CWA Data API LINK
CWA_CURRENT_URL = "https://opendata.cwa.gov.tw/api/v1/rest/datastore"
CWA_API_TOKEN = os.environ.get("CWA_API_KEY")
current_url = f"{CWA_CURRENT_URL}/O-A0001-001"
past_url = f"{CWA_CURRENT_URL}/C-B0024-001"

@app.route('/')
def hello_world():
    return 'Hello, World!'
# Route that jQuery will call to execute the Python script
@app.route('/api/get_cwa_data', methods=['POST'])
def respone_cwa_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing JSON payload"}), 400
        stationId = data.get('StationId')
        current_parmas = {
            'Authorization' : CWA_API_TOKEN,
            'format' : 'JSON',
            'StationId' : stationId}
        logger.info(str(stationId))
        app.logger.info(str(stationId))
        app.logger.info(str(current_parmas))
        current_respond = get_response(current_url, current_parmas)
        current_data = parse_cwa_current_data(current_respond)
        past_parmas = {
            'Authorization' : CWA_API_TOKEN,
            'format' : 'JSON',
            'stationID' : stationId}
        past_respond = get_response(past_url, past_parmas)
        past_data = parse_cwa_past_data(past_respond)
        cwa_data = {'Current':current_data, 'Past':past_data}
        return  jsonify(cwa_data), 200
    except Exception as e:
        logger.error(request.get_json())
        app.logger.error(request.get_json())
        return 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
