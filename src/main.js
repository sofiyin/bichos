import { createApp } from 'vue';
import App from './App.vue';
import axios from 'axios';
import router from './routers';
import './assets/styles/styles.css';

// Configurar Axios para que esté disponible en toda la aplicación
const app = createApp(App);
app.use(router);
app.config.globalProperties.$http = axios;


// Montar la aplicación en el elemento con el id 'app'
app.mount('#app');

