# pip install Pyrebase==3.0.27
import pyrebase

config = {
    'apiKey': "AIzaSyBxUA0dGD003HCahLKoYWiwt3J9VGbDg_U",
    'authDomain': "potato-5987d.firebaseapp.com",
    'projectId': "potato-5987d",
    'storageBucket': "potato-5987d.appspot.com",
    'messagingSenderId': "739055637770",
    'appId': "1:739055637770:web:f6771260e7c445bef916f3",
    "databaseURL": "https://potato-5987d-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()
db = firebase.database()
# push data
# db.child("potatoes/").push({"potato": "pakistan potatota"})

# get data
data = db.child("potatoes/").get()
for k in data.val().items():
    print(k[1]['potato'])  # pakistan potatota

# path_on_cloud = "images/"
# local_path = 'test.jpg'

# storage.child(path_on_cloud).put(local_path)
