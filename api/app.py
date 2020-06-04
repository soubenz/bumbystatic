import hug
import requests
import json
from requests.exceptions import ConnectionError
import db
import new
from marshmallow import fields
from marshmallow.validate import Length, OneOf
from werkzeug.security import generate_password_hash
from falcon import HTTP_400
import jwt
from collections import Counter
import dateparser

SCRAPYD_HOST = "http://scrapyd.promotya.com"
api = hug.API(__name__)
# hug.get('/admin/users', api=api)(service.get_users)
# hug.get('/generator/links', api=api)(new.mock_layout)
hug.get('/generator/links', api=api)(new.mock_community)
