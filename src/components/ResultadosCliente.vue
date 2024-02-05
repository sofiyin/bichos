<link href="css/bootstrap.css" rel="stylesheet" type="text/css" />
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
<template>
  <div>
    
    <div class="jumbotron3">
      <h2>Resultados</h2><!-- Galería de imágenes -->
    </div>
    <h3>Hemos detectado en conjunto a lo seleccionado:</h3>
    <h3>Fotografía, Síntomas y Locación </h3> 
    <h3 style="background-color:tomato;">Podrías tener una enfermedad transmitida por mosquitos en un 76%. </h3> 
    <h3>Te recomendamos que acudas a un médico para que te realice un diagnóstico más preciso. </h3>
    <button type="button" class="btn btn-warning">Alertar a mis usuarios cercanos</button> <br><br/>
    <button type="button" class="btn btn-warning">Actualizar mapa de casos</button> <br><br/>
    <div class="entry-content entry clearfix">
      <div class="tabs-shortcode tabs-wrapper container-wrapper tabs-horizontal flex-tabs is-flex-tabs-shortcodes">
      
      <ul class="tabs" style="opacity: 1;">
      <li class="flexMenu-viewMore">
        <ul class="flexMenu-popup" style="display:none; position: absolute;">
        
        <li>
          <a href="#tab-content-2"> Sala de situación semanal </a>
        </li>
        <li>
          <a href="#tab-content-3"> Sala diaria </a>
        </li>
        <li>
          <a href="#tab-content-4"> Sala semanal en PDF </a>
        </li>

        </ul>
      </li>
      </ul>
    
      <div class="tab-content" id="tab-content-1">
        <div class="tab-content-wrap">
  <iframe src="https://app7.dge.gob.pe/maps/denguemap/" width="95%" height="1000px"></iframe><br>

        </div>
      </div>
    

      <div class="tab-content" id="tab-content-2">
        <div class="tab-content-wrap">
  <h2>Sala de situación semanal</h2>
  <p><b><a class="alert-link" href="https://www.dge.gob.pe/sala-situacional-dengue/" rel="noopener noreferrer">Ir a Sala de situación semanal <i class="fas fa-external-link-alt"></i> <img src="https://www.dge.gob.pe/images/external_link.png" width="20px"></a></b><br>

        </p></div>
      </div>
    

      <div class="tab-content" id="tab-content-3">
        <div class="tab-content-wrap">
  <h2>Sala de situación diaria</h2>
  <p><b><a class="alert-link" href="https://www.dge.gob.pe/sala-situacional-dengue/diaria/" target="_blank" rel="noopener noreferrer">Ir a Sala de situación diaria <i class="fas fa-external-link-alt"></i> <img src="https://www.dge.gob.pe/images/external_link.png" width="20px"></a></b><br>

        </p></div>
      </div>
    

      <div class="tab-content" id="tab-content-4">
        <div class="tab-content-wrap">  
        </div>
      </div>
        <div class="clearfix"></div>
      </div>
      </div>
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
