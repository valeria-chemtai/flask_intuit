import urllib
import requests

from flask_api import FlaskAPI
from flask import jsonify, make_response, redirect, request
from werkzeug.exceptions import BadRequest


import config
import util


app = FlaskAPI(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello, Quickbooks!'


@app.route('/auth')
def auth():
    # OAuth2 initiate authorization flow
    params = {
        'scope': 'com.intuit.quickbooks.accounting',
        'redirect_uri': config.REDIRECT_URI,
        'response_type': 'code',
        'client_id': config.CLIENT_ID,
        'state': config.SECRET_KEY
    }
    resp = requests.get("https://developer.intuit.com/.well-known/openid_sandbox_configuration/")
    url = resp.json()['authorization_endpoint'] + '?' + urllib.parse.urlencode(params)
    return redirect(url)


@app.route('/callback')
def callback():
    """Handles callback and returns access_token"""
    auth_stuff = {}
    authorization_code = str(request.args.get('code'))
    if authorization_code is None:
        return BadRequest()

    bearer = util.get_bearer_token(authorization_code)
    realmId = str(request.args.get('realmId'))

    auth_stuff['realm_id'] = realmId
    auth_stuff['access_token'] = bearer['access_token']
    auth_stuff['refresh_token'] = bearer['refresh_token']
    response = auth_stuff
    return make_response(jsonify(response)), 200
