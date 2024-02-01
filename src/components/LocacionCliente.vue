
<template>

  <div>
    <div class="jumbotron3">
      <h2>Paso 3: Tu ubicación </h2>
    </div>
    <h3>Elige tu locación reciente</h3>
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
