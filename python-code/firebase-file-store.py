import pyrebase

config = {
    'apiKey': "AIzaSyDpoOWQIQGF0ZYJ9QaYj-cG19N3MW2vvhg",
    'authDomain': "pybase-9087d.firebaseapp.com",
    'databaseURL': "https://pybase-9087d-default-rtdb.firebaseio.com",
    'projectId': "pybase-9087d",
    'storageBucket': "pybase-9087d.appspot.com",
    'messagingSenderId': "1064239651081",
    'appId': "1:1064239651081:web:f98e55c2174e0b0c5d9bd8",
    'measurementId': "G-1E8NF8PYHZ"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "images/"
local_path = 'test.jpg'

storage.child(path_on_cloud).put(local_path)
