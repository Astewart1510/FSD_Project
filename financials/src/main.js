import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

//import BootstrapVue
import  BootstrapVue  from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


import JsonCSV from 'vue-json-csv'
Vue.component('downloadCsv', JsonCSV)



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
