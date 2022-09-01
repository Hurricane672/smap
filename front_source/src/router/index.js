import Vue from 'vue'
import VueRouter from 'vue-router'

import topo from '../views/topo.vue'
import search from '../views/search.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'search',
    component: search
  },
  {
    path: '/topo',
    name: 'topo',
    component: topo,
    
    children:[

    ]
  },
]

const router = new VueRouter({
  routes
})

export default router
