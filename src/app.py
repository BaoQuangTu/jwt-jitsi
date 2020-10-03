from flask import Flask, request
from error import HyperException
import jwt_utils
import config
from gevent.pywsgi import WSGIServer

app = Flask(__name__) #create the Flask app

@app.route('/jwt_jitsi', methods=['POST'])
def get_jwt_jitsi():
    jwt_jitsi = None

    try:
        jwt_jitsi = jwt_utils.generate_token(request);
    except HyperException as e:
        return e.message, e.error_code

    return jwt_jitsi

@app.route('/check_jwt_jitsi', methods=['GET'])
def check_jwt_jitsi():
    payload = None
    try:
        token = jwt_utils.get_access_token_from_request(request)
        payload = jwt_utils.validate_token(token=token)
    except HyperException as e:
        return e.message, e.error_code

    return payload

if __name__ == '__main__':
    app_server = WSGIServer((config.get('SERVER_HOST'), int(config.get('SERVER_PORT'))), app)
    app_server.serve_forever()
    # app.run(debug=True, host=config.get('SERVER_HOST'), port=config.get('SERVER_PORT'))