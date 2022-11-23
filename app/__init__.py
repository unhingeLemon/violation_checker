from flask import Flask
import pyrebase




config = {
  "apiKey": "AIzaSyDJLHvMMeAe1X_5slENMx_aSUQo4OnbEkA",
  "authDomain": "licenseplaterecognition-7c938.firebaseapp.com",
  "projectId": "licenseplaterecognition-7c938",
  "storageBucket": "licenseplaterecognition-7c938.appspot.com",
  "messagingSenderId": "833473633691",
  "databaseURL": "https://licenseplaterecognition-7c938-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "appId": "1:833473633691:web:bf0c32a02331938e33553e"
}




firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'papasakamepapasakame'
    @app.after_request
    def add_header(response):
        # response.cache_control.no_store = True
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0. pre-check=0,max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response



    # FIREBASE:
    


    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app





