# pip install Pyrebase==3.0.27
import pyrebase

config = {

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
