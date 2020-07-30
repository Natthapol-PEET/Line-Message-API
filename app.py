from flask import Flask, request
import json
import requests
from firebase import firebase

# Setup Url
Authorization = 'Bearer tVdIAfmI+eV3LfM7LE7RTAQfP6PIcCM/o5/NdkCMV8yUbhcDMnEEX9bGWn8MPbiN8/2gRTAyTemSHxC9YNJYWtaFTliAoVO5vIsxPlnax7FKEpriB8zglavc+0OPPT2AhzLikWe1m7McQxwYoZPUtFGUYhWQfeY8sLGRXgo3xvw='
database_url = 'https://g0lineapi-opxykx.firebaseio.com/'

app = Flask(__name__)
firebase = firebase.FirebaseApplication(database_url, None)

@app.route('/')
def index():
  return "Hello World!"

# ส่วน callback สำหรับ Webhook
@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line, indent=2)
  decoded = json.loads(json_line)

  # delete -> userId
  # add -> userId, replyToken

  try:
    replyToken = decoded["events"][0]['replyToken']
    # print("replyToken: ", replyToken)
    sendText(replyToken, 'Hello, User')
  except:
      pass

  try:
    userId = decoded["events"][0]['source']['userId']
    GetText = decoded["events"][0]['message']['text']
  except:
      pass 

  try:
    postToFirebase(userId, replyToken, GetText)
  except:
    pass

  print(json_line)

  return '', 200

def sendText(replyToken, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization
  }
  data = json.dumps({
    "replyToken": replyToken,
    "messages":[{"type":"text", "text":text}]
  })
  r = requests.post(LINE_API, headers=headers, data=data)

def postToFirebase(userId, replyToken, Text):
  data =  { 'UserID': userId,
            'replyToken': replyToken,
            'text': Text
            }
  result = firebase.post('/g0lineapi-opxykx/Bot noii/', data)
  print(result)

if __name__ == '__main__':
  app.run(debug=True)