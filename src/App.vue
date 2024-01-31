<template>
  <div id="app">
    <div>
    <div class="jumbotron2">
      <div class="container text-center">
        <ImageUploader />     
      </div>
    </div>
    
    <ImageGallery />
    <LocacionCliente />
    
	<label for="checkbox">{{ checked }}</label>
  </div>
  </div>
</template>

<script>

import ImageUploader from "./components/ImageUploader.vue"; 
import ImageGallery from "./components/ImageGallery.vue"; 
import LocacionCliente from "./components/LocacionCliente.vue"; 

export default {
  name: 'App',
  components: {
    ImageUploader, 
    ImageGallery, 
    LocacionCliente,
  }
}
</script>
<style src="./assets/styles/styles.css"></style>