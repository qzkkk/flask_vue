import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'hash',
  routes: [
    {
      path: '/Login',
      component: ()=>import('~/views/web/Login')
    },
    {
      path: '/Register',
      component: ()=>import('~/views/web/Register')
    },
    {
      path: '/Index',
      component: ()=>import('~/views/web/Index')
    },
    {
      path:'/Category',
      component: ()=>import('~/views/web/Category')
    },
    {
      path:'/Article',
      component: ()=>import('~/views/web/Article')
    },
    // {
    //   path:'/Tags',
    //   component: ()=>import('~/views/web/Tags')
    // },
    {
      path: '/Mine',
      component: ()=>import('~/views/web/Mine')
    },
    {
      path:'/Update',
      component: ()=>import('~/views/web/Update')
    },
    {
      path:'/Detail',
      component: ()=>import('@/articleDetail')
    },
    {
      path: '/',
      redirect: '/Index'
    }
  ]
})