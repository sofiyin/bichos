from flask import Flask, jsonify
from flask_cors import CORS  # Importa CORS
from dataclasses import dataclass
import datetime
from sqlalchemy import select, and_, or_, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func
from flask import Flask, jsonify,  request, render_template,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY<@_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


CORS(app)  # Configura CORS
@dataclass
class enfermedades(db.Model):
    __tablename__ = 'enfermedades'

    idenfermedades:int
    idenfermedades = db.Column(db.Integer, primary_key=True)
   
    def __repr__(self):
        return f'<enfermedades {self.idenfermedades}>'
    
@app.route('/api/data',methods=['GET', 'POST'])
def get_data():
    
    data = {'message': 'DATOS PARA LA MACHINE LEARNING :D'}
    return jsonify(data)

@app.route('/api/resultados')
def resultados():
    data = {'message': 'AKI ESTAN TUS RESPUESTAS :D'}
    return jsonify(data)

with app.app_context():
        db.create_all()
if __name__ == '__main__':
    app.run(port=5000, debug=True)