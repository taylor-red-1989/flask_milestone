from flask import Flask
from flask_restful import Api
from db import db
from resources import Invoice

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'keepitsecret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Invoice, '/generate/invoice', '/view/invoice/<invoice_number>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)