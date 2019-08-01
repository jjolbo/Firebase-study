import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Firebase:
    def firebase_db(self):
        cred = credentials.Certificate('key.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://********.firebaseio.com/'
        })

    def load(self, path):
        ref = db.reference(path)
        data = ref.get()
        return data

    def update(self, dataset):
        ref = db.reference('info')
        ref.update(dataset)
