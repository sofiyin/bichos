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

    <input type="checkbox" id="fiebre repentina" value="fiebre repentina" v-model="checkedNames">
    <label for="fiebre repentina">fiebre repentina</label>

    <input type="checkbox" id="dolor de cabeza" value="dolor de cabeza" v-model="checkedNames">
    <label for="dolor de cabeza">dolor de cabeza</label>

    <input type="checkbox" id="hemorragia bucal" value="hemorragia bucal" v-model="checkedNames">
    <label for="hemorragia bucal">hemorragia bucal</label>

    <br />
    <br />
    <input type="checkbox" id="hemorragia nasal" value="hemorragia nasal" v-model="checkedNames">
    <label for="hemorragia nasal">hemorragia nasal</label>

    <input type="checkbox" id="dolor muscular" value="dolor muscular" v-model="checkedNames">
    <label for="dolor muscular">dolor muscular</label>
    
    <input type="checkbox" id="dolor de articulaciones" value="dolor de articulaciones" v-model="checkedNames">
    <label for="dolor de articulaciones">dolor de articulaciones</label>
    <br />
    <br />
    <input type="checkbox" id="vomitos" value="vomitos" v-model="checkedNames">
    <label for="vomitos">vomitos</label>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      images: [],
      checkedNames: []  // Inicializa el array para almacenar los síntomas seleccionados
    };
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
