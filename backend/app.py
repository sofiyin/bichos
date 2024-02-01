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
from sqlalchemy import Column, Integer

import json
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY<@_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


CORS(app)  # Configura CORS
@dataclass
class ENFERMEDADES(db.Model):
    __tablename__ = 'enfermedades'

    id: int  # Assuming a single user for now
    fiebre_repentina: int
    dolor_de_cabeza: int
    hemorragia_bucal: int
    hemorragia_nasal: int
    dolor_muscular: int
    dolor_en_las_articulaciones: int
    vomitos: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fiebre_repentina = db.Column(db.Integer)
    dolor_de_cabeza = db.Column(db.Integer)
    hemorragia_bucal = db.Column(db.Integer)
    hemorragia_nasal = db.Column(db.Integer)
    dolor_muscular = db.Column(db.Integer)
    dolor_en_las_articulaciones = db.Column(db.Integer)
    vomitos = db.Column(db.Integer)
   
    def __repr__(self):
        return f'<enfermedades {self.id}>'
    
@app.route('/api/data', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        
        # Retrieve all symptoms from the database
        all_symptoms = ENFERMEDADES.query.all()

        # Create a list to store symptom data
        symptoms_data = []

        # Loop through each symptom and extract relevant information
        for symptom in all_symptoms:
            symptom_data = {
                'fiebre_repentina': symptom.fiebre_repentina,
                'dolor_de_cabeza': symptom.dolor_de_cabeza,
                'hemorragia_bucal': symptom.hemorragia_bucal,
                'hemorragia_nasal': symptom.hemorragia_nasal,
                'dolor_muscular': symptom.dolor_muscular,
                'dolor_en_las_articulaciones': symptom.dolor_en_las_articulaciones,
                'vomitos': symptom.vomitos
                # Add more fields if needed
            }
            symptoms_data.append(symptom_data)
            print(symptom.dolor_de_cabeza)
            print(symptom.fiebre_repentina)
            print(symptom.hemorragia_bucal)
            print(symptoms_data)

        # Return the symptom data as JSON
        return jsonify({'symptoms': symptoms_data})

    elif request.method == 'POST':
        data = request.get_json()
        symptoms = data.get('symptoms', {})

        # Assuming a single user for now (user_id=1)
        user_id = 1
        existing_record = ENFERMEDADES.query.filter_by(id=user_id).first()
        if existing_record:
            # Borrar los datos existentes
            db.session.delete(existing_record)
            db.session.commit()
        for key in ['fiebre_repentina', 'dolor_de_cabeza', 'hemorragia_bucal', 'hemorragia_nasal', 'dolor_muscular', 'dolor_en_las_articulaciones', 'vomitos']:
            if key not in symptoms or symptoms[key] is None:
                symptoms[key] = 0    

        # Crear un nuevo registro
        symptoms = {key: value or 0 for key, value in symptoms.items()}

        enfermedades = ENFERMEDADES(id=user_id, **symptoms)
        db.session.add(enfermedades)
        db.session.commit()

        data = request.get_json()
        symptoms = data.get('symptoms', {})
            
        # Almacenar los nuevos síntomas
        symptoms_data['symptoms'] = symptoms
        enfermedades = ENFERMEDADES(id=user_id, **symptoms)
        db.session.add(enfermedades)
        db.session.commit()
        return jsonify(enfermedades)    
    


@app.route('/api/resultados')
def resultados():
    data = {'message': 'AKI ESTAN TUS RESPUESTAS :D'}
    return jsonify(data)

with app.app_context():
        db.create_all()
if __name__ == '__main__':
    app.run(port=5000, debug=True)