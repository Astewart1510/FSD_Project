import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

// The different views are created on this page
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Search_Share',
    name: 'Search_Share',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Search_Share.vue')
  },
  {
    path: '/Search_Industry',
    name: 'Search_Industry',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Search_Industry.vue')
  },
  {
    path: '/Client_Indices',
    name: 'Client_Indices',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Client_Indices.vue')
  },

]

const router = new VueRouter({
  routes
})

export default router
