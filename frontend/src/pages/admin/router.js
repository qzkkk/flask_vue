import Vue from 'vue';
import vueRouter from 'vue-router';
import layout from '~/views/admin/layout.vue';
Vue.use(vueRouter)
const router = new vueRouter({
    mode: 'hash',
    routes: [
        {
            path: '/',
            component: layout,
            redirect: 'Index',
            children: [
                {
                    path: 'Index',
                    component: () => import('~/views/admin/index.vue')
                },
                {
                    path: 'category',
                    component: () => import('~/views/admin/category/CategoryAdmin.vue')
                },
                {
                    path: 'article',
                    component: () => import('~/views/admin/article/articlesAdmin.vue')
                },
                {
                    path: 'Edit',
                    component: () => import('~/views/admin/article/Edit')
                },
                {
                    path: 'user',
                    component: () => import('~/views/admin/usersAdmin.vue')
                }
            ]
        },
        {
            path: '/login',
            component: () => import('~/views/admin/Login.vue')
        },
    ]
})

export default router;