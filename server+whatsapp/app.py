'''
GET: to give data to the swift program, just do json.dumps
POST: to get json data, use get json to get the json data
'''
from flask import Flask, request
from db_v2 import *
import json
from main_wa_bot import *

app = Flask(__name__)

@app.route('/')
def i():
    return 'Hello World'

@app.route('/get_testdata')
def getdata():
    res = get_items()
    print("hi", json.dumps(res))
    return json.dumps(res)

@app.route('/test_post', methods=['POST'])
def test_post():
    # payload = request.get_json()
    # info, data = payload['info'], payload['data']
    # print(info)
    # print(data)
    # print(type(request.get_json()) is list)
    # print(type(request.get_json()) is dict)
    return json.dumps(get_items())
    
@app.route('/get_badge_for_user', methods=['POST'])
def for_user():
    # payload = request.get_json()
    # if type(doc) is list: upsert_many()
    return json.dumps(get_badges('bl3321'))

@app.route('/get_badge_info', methods=['POST'])
def info():
    # payload = request.get_json()
    # if type(doc) is list: upsert_many()
    return json.dumps(get_badge_info())


# you want twilio to call this post request -> of course this reminds you of using ngrok to make your localhost reachable by twilio
@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    return whatsapp_img_bot()
    pass

    
if __name__ == '__main__':
    print(1, get_badges('bl3321'), json.dumps(get_badges('bl3321')))
    # print(json.dumps(get_badges('bl3321')))
    app.run(port=8000)
