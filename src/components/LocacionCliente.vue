<template>
  <div>
    <div class="jumbotron3">
      <h2>Paso 3: Tu ubicación </h2>
    </div>
    
    <h3>Elige tu locación reciente</h3>
     <div>
    <div class="google-map" ref="googleMap"></div>
    <template v-if="Boolean(this.google) && Boolean(this.map)">
      <slot
        :google="google"
        :map="map"
      />
    </template>
  </div>
    
  </div>
</template>

<script>
import Loader from 'google-maps-api-loader';

export default {
  props: {
    mapConfig: Object,
    apiKey: String,
  },

  data() {
    return {
      google: null,
      map: null,
    };
  },

  async mounted() {
    // As per the documentation for the google maps API loader
    const googleMapApi = await Loader({
      apiKey: this.apiKey,
    });

    // Set the google object from the correct location
    this.google = window.google || googleMapApi;

    this.initializeMap();
  },

  methods: {
    initializeMap() {
      const mapContainer = this.$refs.googleMap;
      this.map = new this.google.maps.Map(mapContainer, this.mapConfig);
    },
  },
};
</script>

