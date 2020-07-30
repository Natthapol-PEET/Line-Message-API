from firebase import firebase

# post data to firebase
firebase = firebase.FirebaseApplication('https://g0lineapi-opxykx.firebaseio.com/', None)
data =  { 'UserID': '6040202424',
          'replyToken': '1410501130726',
          'text': 'Hello, world!'
          }
result = firebase.post('/g0lineapi-opxykx/Bot noii/', data)
print(result)

# put/update
# firebase = firebase.FirebaseApplication('https://g0lineapi-opxykx.firebaseio.com/', None)
# firebase.put('/g0lineapi-opxykx/Bot noii/-MDJHXhXRZ2EbDJ2IHVQ', 'UserID', 'update !!')
# print('Record Updated')