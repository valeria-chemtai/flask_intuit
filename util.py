import base64
import requests
import json


import config


def get_bearer_token(authorization_code):
    """Get bearer token from authorization code"""
    resp = requests.get(
        "https://developer.intuit.com/.well-known/openid_sandbox_configuration/")
    token_endpoint = resp.json()['token_endpoint']
    auth_header = 'Basic ' + \
        base64.b64encode(bytes(config.CLIENT_ID + ':' +
                               config.CLIENT_SECRET, 'utf-8')).decode()
    headers = {
        'Accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': auth_header
    }
    payload = {
        'code': authorization_code,
        'redirect_uri': config.REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    r = requests.post(token_endpoint, data=payload, headers=headers)
    if r.status_code != 200:
        return r.text
    bearer = json.loads(r.text)
    return bearer
