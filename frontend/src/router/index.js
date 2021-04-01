import { createWebHistory, createRouter } from 'vue-router';
import Home from '../views/Home.vue';
import Materials from '../views/Materials.vue';
import Login from '../views/Login.vue';

const history = createWebHistory()

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/materials',
        name: 'Materials',
        component: Materials

    },
    // {
    //     path: '/materials/<int:pk>',
    //     name: 'Materials',
    //     component: Materials,
    //     props: true
    // }
]

const router = createRouter({history, routes})

export default router