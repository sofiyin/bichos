<template>
  <div id="app">
    <ImageUploader />
    <ImageGallery />
    <input type="checkbox" id="checkbox" v-model="checked" />
	<label for="checkbox">{{ checked }}</label>
  </div>
</template>

<script>
import ImageUploader from "./components/ImageUploader.vue"; 
import ImageGallery from "./components/ImageGallery.vue"; 

export default {
  name: 'App',
  components: {
    ImageUploader, 
    ImageGallery, 
  }
}
</script>
<style src="./assets/styles/styles.css"></style>