import json
from collections import namedtuple
from json import JSONEncoder

class Payload:
    def __init__(self, context, iss, sub, room, exp):
        self.context = context
        self.iss = iss
        self.sub = sub
        self.room = room
        self.exp = exp

class Context:
    def __init__(self, user):
        self.user = user

class User:
    def __init__(self, id, name, avatar, email):
        self.id = id
        self.name = name
        self.avatar = avatar
        self.email = email

class PayloadEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

def customPayloadDecoder(payloadDict):
    return namedtuple('X', payloadDict.keys())(*payloadDict.values())