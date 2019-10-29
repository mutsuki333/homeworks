import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Stock from './views/Stock.vue'
import Modify from './views/Modify.vue'
import Status from './views/Status.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  // base: process.env.BASE_URL,
  // base: '/dennyplay', //for deploy
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/stock',
      name: 'stock',
      component: Stock
    },
    {
      path: '/modify',
      name: 'modify',
      component: Modify
    },
    {
      path: '/alter/:id',
      name: 'alter',
      props: true,
      component: Modify
    },
    {
      path: '/status',
      name: 'status',
      component: Status
    },
  ]
})
