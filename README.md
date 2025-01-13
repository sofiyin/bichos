# Mosquito Bite Symptom and Risk Estimator

## Overview
This web application estimates the probability of contracting diseases transmitted by mosquitoes based on reported symptoms and geolocation. A heat map highlights the risk of disease based on data from the past 14 days in the user's area.

---

## Features

- **Symptom Analysis**: Users can report symptoms, which the app correlates with potential mosquito-borne diseases.
- **Disease Risk Mapping**: A heat map shows the probability of disease transmission in the user's region based on recent data.
- **API Integration**: Utilizes the Peruvian Ministry of Health (MINSA) API for up-to-date information.
- **Data Visualization**: Embeds interactive content for a comprehensive user experience.
- **Image Upload and Management**: Users can upload pictures of mosquito bites for analysis and delete uploaded images as needed.

---

## Technologies Used

- **Frontend**: Vue.js
- **Backend**: Flask, Python
- **Database**: SQLAlchemy
- **External APIs**: MINSA API

---

## Database Schema

### Table: `ENFERMEDADES`
| Column                | Type     | Description                          |
|-----------------------|----------|--------------------------------------|
| `id`                 | Integer  | Primary key (auto-increment)         |
| `fiebre_repentina`   | Integer  | Sudden fever severity                |
| `dolor_de_cabeza`    | Integer  | Headache severity                    |
| `hemorragia_bucal`   | Integer  | Mouth bleeding severity              |
| `hemorragia_nasal`   | Integer  | Nasal bleeding severity              |
| `dolor_muscular`     | Integer  | Muscle pain severity                 |
| `dolor_en_las_articulaciones` | Integer | Joint pain severity         |
| `vomitos`            | Integer  | Vomiting severity                    |
| `Fatiga`             | Integer  | Fatigue severity                     |
| `Ojos_rojos`         | Integer  | Red-eye severity                     |

### Example Model Definition
```python
class ENFERMEDADES(db.Model):
    __tablename__ = 'enfermedades'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fiebre_repentina = db.Column(db.Integer)
    dolor_de_cabeza = db.Column(db.Integer)
    hemorragia_bucal = db.Column(db.Integer)
    hemorragia_nasal = db.Column(db.Integer)
    dolor_muscular = db.Column(db.Integer)
    dolor_en_las_articulaciones = db.Column(db.Integer)
    vomitos = db.Column(db.Integer)
    Fatiga = db.Column(db.Integer)
    Ojos_rojos = db.Column(db.Integer)

    def __repr__(self):
        return f'<ENFERMEDADES {self.id}>'
```

---

## API Endpoints

### `/api/data`
- **GET**: Retrieves all symptom data from the database.
- **POST**: Submits new symptom data for analysis.

### `/api/resultados`
- **GET**: Returns general results and recommendations.

### `/api/upload`
- **POST**: Accepts image files for analysis and uploads them to the server.

---

## Image Upload and Management

The app includes methods to upload and manage images of mosquito bites:

### **uploadImages(event)**
- **Purpose**: Handles uploading of images selected by the user.
- **Process**:
  1. **Access Selected Files**: Retrieves files uploaded via the `<input type="file">` element.
  2. **Iterate Through Files**: Loops through the selected files to process each one individually.
  3. **Read File as Data URL**: Uses `FileReader` to convert the file into a base64-encoded URL (data URL).
  4. **Store Image Data**: Pushes the converted URL into the `imageUrls` array for display or further processing.

### **deleteImage(index)**
- **Purpose**: Removes an uploaded image from the display list.
- **Process**:
  1. **Identify Image**: Receives the index of the image to be removed.
  2. **Update Array**: Uses `splice` to remove the image from the `imageUrls` array.

---

## Dataset

The project utilizes the *Insect Bite Identifier* dataset, hosted on Roboflow. It contains annotated images of various insect bites, designed to train computer vision models for detection and classification of insect bites. This dataset supports formats for object detection models and offers a robust foundation for image-based predictions.

**Dataset Link**: [Roboflow - Insect Bite Dataset](https://universe.roboflow.com/insect-bite-identifier-ceyst/insect-bites/dataset/3/images/24520da8b13ad3c8b3f076b2b89adf2d)

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
4. Start the backend server:
   ```bash
   python app.py
   ```
5. Start the frontend server:
   ```bash
   npm run serve
   ```

---

## External Resources

- [Dengue Map](https://app7.dge.gob.pe/maps/denguemap/)
- [Weekly Situation Room](https://www.dge.gob.pe/sala-situacional-dengue/)
- [Mosquitos db](https://universe.roboflow.com/insect-bite-identifier-ceyst/insect-bites/)

---

## Set

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a descriptive message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---
