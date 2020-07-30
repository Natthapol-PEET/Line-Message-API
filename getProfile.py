import json
import requests

# Setup Url
Authorization = 'Bearer tVdIAfmI+eV3LfM7LE7RTAQfP6PIcCM/o5/NdkCMV8yUbhcDMnEEX9bGWn8MPbiN8/2gRTAyTemSHxC9YNJYWtaFTliAoVO5vIsxPlnax7FKEpriB8zglavc+0OPPT2AhzLikWe1m7McQxwYoZPUtFGUYhWQfeY8sLGRXgo3xvw='
userId = 'Ubc69ab33ddd35bef46d5b6786d9166ca'    # PEET
# userId = 'U417e7d68fe88a6063dd8aa4ef40f326c'  # FAH

def getProfile():
  LINE_API = 'https://api.line.me/v2/bot/profile/' + userId
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization': Authorization
  }
  r = requests.get(LINE_API, headers=headers)

  return r.text


if __name__ == '__main__':
  data = getProfile()
  print(data)