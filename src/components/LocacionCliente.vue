
<template>

  <div>
    <h2>Paso 3: Tu ubicación </h2>
    <h3>Elige tu locación reciente</h3>
    <input type="file" @change="uploadImages" multiple>
    <div v-for="(imageUrl, index) in imageUrls" :key="index">
      <img :src="imageUrl" alt="Prenesena slika">
      <button @click="deleteImage(index)">Subir</button>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imageUrls: []
    };
  },
  methods: {
    uploadImages(event) {
      const files = event.target.files;
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        if (file) {
          const reader = new FileReader();
          reader.onload = () => {
            this.imageUrls.push(reader.result);
          };
          reader.readAsDataURL(file);
        }
      }
    },
    deleteImage(index) {
      this.imageUrls.splice(index, 1);
    }
  }
};
</script>
