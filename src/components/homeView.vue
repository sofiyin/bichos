<template>
    <!-- Contenido de la plantilla aquí -->
    <div>
      <h1>Bienvenido a BiteSight</h1>
      <!-- boton que dirige a la vista ImageUploader -->
        <router-link to="/ImageUploader">
            Empecemos
        </router-link>
    </div>
</template>
  
<script>
  // Lógica del componente aquí
  export default {
    name: 'HomeView',
    components: {
    },
  };
</script>
  
<style>
  /* Estilos del componente aquí */
</style>