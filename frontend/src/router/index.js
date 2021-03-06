import { createWebHistory, createRouter } from 'vue-router';
import HelloWorld from '../components/HelloWorld.vue';

const history = createWebHistory()

const routes = [
    {
        path: '/',
        name: 'Helloworld',
        component: HelloWorld
    }
]

const router = createRouter({history, routes})

export default router