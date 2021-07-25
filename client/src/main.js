import Vue from 'vue';
// import axios from 'axios';
import 'sweetalert2/dist/sweetalert2.min.css';

import titleMixin from './mixins/titleMixin';

import router from './router';
import store from './store';
import App from './App.vue';

// Vue.use(VueSweetalert2);

Vue.mixin(titleMixin);

// axios.defaults.baseURL = 'http://127.0.0.1:8000/';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
