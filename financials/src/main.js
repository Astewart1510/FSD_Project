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

//import Vue Matertial components
import { MdButton, MdContent, MdTabs, MdList, MdIcon, MdBadge, MdTable, MdField } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(MdButton)
Vue.use(MdContent)
Vue.use(MdTabs)
Vue.use(MdList)
Vue.use(MdIcon)
Vue.use(MdBadge)


import JsonCSV from 'vue-json-csv'
Vue.component('downloadCsv', JsonCSV)



new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
