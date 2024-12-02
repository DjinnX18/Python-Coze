import base64
import json

class B64(bytes):
    def __init__(self, b):
        super().__init__()

    def from_json(self, b):
        s = base64.urlsafe_b64decode(b.strip('"').encode('utf-8'))
        return B64(s)

    def to_json(self):
        return json.dumps(self.decode('utf-8'))

    def __str__(self):
        return base64.urlsafe_b64encode(self).decode('utf-8')

    def __repr__(self):
        return base64.urlsafe_b64encode(self).decode('utf-8')

def decode(b64):
    return B64(base64.urlsafe_b64decode(b64))

def must_decode(b64):
    try:
        return B64(base64.urlsafe_b64decode(b64))
    except Exception as e:
        raise RuntimeError(e)

