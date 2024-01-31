<template>
  <div id="app">
    <ImageUploader />
    <ImageGallery />
    <LocacionCliente />
    
	<label for="checkbox">{{ checked }}</label>
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