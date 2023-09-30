import './assets/main.css';
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import VueAxios from "vue-axios";
import axios from "axios";

import "primevue/resources/themes/lara-light-blue/theme.css";
import "primeicons/primeicons.css";

const app = createApp(App);

app.use(router);
app.use(PrimeVue);
app.use(VueAxios, axios);

app.provide('axios', app.config.globalProperties.axios);

app.mount('#app');
