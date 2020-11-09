import jwt
import config
import static_value as config_value
from error import HyperException
from http import HTTPStatus
import time
from payload import *

def generate_token(access_payload, room_id):
    print(access_payload)

    user = User(access_payload['jti'], 
                access_payload['userName'] if 'userName' in access_payload else None, 
                access_payload['avatar'] if 'avatar' in access_payload else None, 
                access_payload['email'] if 'email' in access_payload else None)
    # user = User("abcd:a1b2c3-d4e5f6-0abc1-23de-abcdef01fedcba", "Bao Quang Tu", "https:/gravatar.com/avatar/abc123", None)
    payload = {}

    payload['context'] = user.__dict__
    payload['aud'] = config_value.JWT_AUDIENCE
    payload['iss'] = config_value.JWT_ISSUER
    payload['sub'] = config_value.JWT_SUB
    payload['room'] = room_id
    payload['exp'] = int(round(time.time())) + config_value.JWT_EXPIRE_AFTER

    # Generate jwt jitsi token
    token = jwt.encode(payload, config_value.JWT_SECRET, algorithm='HS256').decode('utf-8')
    print(token)
    return token

def validate_token_rs256(token):
    payload = None

    public_key = open(config.get('PUBLIC_KEY_URL')).read()

    try:
        payload = jwt.decode(token, public_key, algorithms=['RS256'])
    except:
        raise HyperException(error_code=HTTPStatus.UNAUTHORIZED, message="Token decode failure")

    if ('exp' in payload):
        exp = payload['exp']
        if (int(round(time.time())) > exp):
            raise HyperException(error_code=HTTPStatus.UNAUTHORIZED, message="Token expired")

    return payload

def validate_token_hs256(token):
    payload = None
    try:
        payload = jwt.decode(token, config_value.JWT_SECRET, algorithms=['HS256'], audience=config_value.JWT_AUDIENCE)
    except Exception as e:
        print(e)
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
    