import jwt
import config
import static_value as config_value
from error import HyperException
from http import HTTPStatus
import time
from payload import *

def generate_token(access_payload, room_id):
    print(access_payload)

    user = User(access_payload['jti'], access_payload['name'], access_payload['avatar'], access_payload['email'])
    # user = User("abcd:a1b2c3-d4e5f6-0abc1-23de-abcdef01fedcba", "Bao Quang Tu", "https:/gravatar.com/avatar/abc123", None)
    payload = {}

    payload['context'] = user.__dict__
    payload['iss'] = config_value.JWT_ISSUER
    payload['sub'] = config_value.JWT_SUB
    payload['room'] = room_id
    payload['exp'] = int(round(time.time())) + config_value.JWT_EXPIRE_AFTER

    private_key = open(config.get('PRIVATE_KEY_URL')).read()

    # Generate jwt jitsi token
    token = jwt.encode(payload, private_key, algorithm='RS256').decode('utf-8')
    print(token)
    return token

def validate_token(token, on_sso=False):
    payload = None
    PUBLIC_KEY_URL = None
    
    if (on_sso is True):
        PUBLIC_KEY_URL = 'SSO_PUBLIC_KEY_URL'
    else:
        PUBLIC_KEY_URL = 'PUBLIC_KEY_URL'

    public_key = open(config.get(PUBLIC_KEY_URL)).read()

    try:
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
    except:
        raise HyperException(error_code=HTTPStatus.UNAUTHORIZED, message="Token decode failure")

    if ('exp' in payload):
        exp = payload['exp']
        if (int(round(time.time())) > exp):
            raise HyperException(error_code=HTTPStatus.UNAUTHORIZED, message="Token expired")

    return payload

def get_access_token_from_request(request):
    if (config_value.JWT_REQUEST_KEY not in request.headers):
        raise HyperException(error_code=HTTPStatus.UNAUTHORIZED, message='Access token header null: ' + config_value.JWT_REQUEST_KEY)
    
    return request.headers[config_value.JWT_REQUEST_KEY]
    