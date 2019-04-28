import socket
import json

_host = None
_port = None

class SmorError(Exception):
    pass

def config(host, port=8085):
    global _host, _port
    _host = host
    _port = port

def _converse(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((_host, _port))
    sock.sendall(json.dumps(data).encode('utf8'))
    return json.loads(sock.recv(5000).decode('utf8'))

def put(msgbox, message):
    data = {
        'action': 'put',
        'msgbox': msgbox,
        'message': message
    }
    resp = _converse(data)
    if resp['ok']:
        return
    else:
        raise SmorError(resp['error'], resp.get('message'))

def _get(msgbox):
    data = {
        'action': 'get',
        'msgbox': msgbox
    }

    resp = _converse(data)
    if resp['ok']:
        return resp['messages']
    else:
        raise SmorError(resp['error'], resp.get('message'))

_cache = {}
def get_one(msgbox):
    lc = _cache.get(msgbox)
    if lc and len(lc) > 0:
        return lc.pop(0)

    lc = _get(msgbox)
    _cache[msgbox] = lc

    if len(lc) == 0:
        return None
    else:
        return lc.pop(0)

def get_all(msgbox):
    v = []
    if msgbox in _cache:
        v = _cache[msgbox]
        del _cache[msgbox]

    v += _get(msgbox)
    return v