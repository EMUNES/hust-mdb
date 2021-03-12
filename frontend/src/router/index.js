import { createWebHistory, createRouter } from 'vue-router';
import HelloWorld from '../views/HelloWorld.vue';
import Materials from '../views/Materials.vue';

const history = createWebHistory()

const routes = [
    {
        path: '/',
        name: 'Helloworld',
        component: HelloWorld
    },
    {
        path: '/materials',
        name: 'Materials',
        component: Materials

    }
]

const router = createRouter({history, routes})

export default router