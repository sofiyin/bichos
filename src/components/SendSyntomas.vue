<template>
  <div>
    <!-- Galería de imágenes -->
    <div v-for="(image, index) in images" :key="index">
      <img :src="image" alt="Slika">
    </div>
    
    <div class="jumbotron3">
      <h2>Paso 2: Selecciona los síntomas que has tenido</h2>
    </div>

    
    <!-- Checkboxes de síntomas -->
    <div> <h3>Dale click a los síntomas que presentes: </h3>{{ checkedNames }}</div>
    <br />
    <br />

    <input type="checkbox" id="chkFiebreRepentina" value="fiebre_repentina" v-model="checkedNames">
    <label for="chkFiebreRepentina">fiebre repentina  &nbsp;</label>
    <input type="checkbox" id="chkDolorDeCabeza" value="dolor_de_cabeza" v-model="checkedNames">
    <label for="chkDolorDeCabeza">dolor de cabeza  &nbsp;</label>

    <input type="checkbox" id="chkHemorragiaBucal" value="hemorragia_bucal" v-model="checkedNames">
    <label for="chkHemorragiaBucal">hemorragia bucal  &nbsp;</label>
    <br />
    <br />
    <input type="checkbox" id="chkHemorragiaNasal" value="hemorragia_nasal" v-model="checkedNames">
    <label for="chkHemorragiaNasal">hemorragia nasal &nbsp;</label>

    <input type="checkbox" id="chkDolorMuscular" value="dolor_muscular" v-model="checkedNames">
    <label for="chkDolorMuscular">dolor muscular &nbsp;</label>
    
    <input type="checkbox" id="chkDolorDeArticulaciones" value="dolor_en_las_articulaciones" v-model="checkedNames">
    <label for="chkDolorDeArticulaciones">dolor de articulaciones &nbsp;</label>
    
    <br />
    <br />
    <input type="checkbox" id="chkVomitos" value="vomitos" v-model="checkedNames">
    <label for="chkVomitos">Vomitos&nbsp;</label>
    
    <input type="checkbox" id="chkFatiga" value="Fatiga" v-model="checkedNames">
    <label for="chkFatiga">Fatiga &nbsp;</label>

    <input type="checkbox" id="chkOjosrojos" value="Ojos_rojos" v-model="checkedNames">
    <label for="chkOjosrojos">Ojos rojos &nbsp;</label>

    <br> <br/>
    <button type="button" class="btn btn-info" @click="sendSymptoms">Enviar Síntomas</button>
    <br><br/>

    <router-link to="/LocacionCliente">
      Siguiente
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      images: [], 
      checkedNames: []  // Initialize the array to store selected symptoms
    };
  },
  // ...
methods: {
  sendSymptoms() {
    const mappedSymptoms = {};
    for (const symptom of this.checkedNames) {
      mappedSymptoms[symptom] = 1;
    }

    // Send the selected symptoms to the Flask backend
    axios.post('http://localhost:5000/api/data', { symptoms: mappedSymptoms })
      .then(() => {
        console.log('Síntomas enviados');
      })
      .catch(error => {
        console.error('Error al enviar síntomas a Flask:', error);
      });
  }
},


mounted() {
  // Realiza una solicitud a tu servidor Flask cuando el componente se monta
  axios.get('http://localhost:5000/api/data')
    .then(response => {
      // Actualiza la galería de imágenes con los datos recibidos
      this.images = response.data.images;
    })
    .catch(error => {
      console.error('Error al obtener datos desde Flask:', error);
    });
}
};
</script>
