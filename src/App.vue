<template>
  <div>
    <div>

    <div class="jumbotron">
      <div class="container text-center">
        <h1> Moskitos</h1>   
      </div>
    </div>
    

    <div class="jumbotron2">
      <div class="container text-center">
        <router-view/>     
      </div>
    </div>
    
    
	<label for="checkbox">{{ checked }}</label>
  </div>
  </div>
</template>

<script>
</script>
<style src="./assets/styles/styles.css"></style>