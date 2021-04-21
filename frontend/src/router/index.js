import { createWebHistory, createRouter } from 'vue-router';
import store from '../store/index';
import Home from '../views/Home.vue';
import Materials from '../views/Materials.vue';
import Login from '../views/Login.vue';
import API from '../views/API.vue';
import Contact from '../views/Contact.vue';
import SimAnalysis from '../views/SimAnalysis.vue';

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
    {
        path: '/checkAPI',
        name: 'API',
        component: API
    },
    {
        path: '/contact',
        name: 'Contact',
        component: Contact
    },
    {
        path: '/sim-analysis',
        name: 'SimAnalysis',
        component: SimAnalysis
    }
]

const isAuthenticated = store.getters.isAuthenticated

const router = createRouter({history, routes})

// Login and next logic.
router.beforeEach((to, from, next) => {
    if (to.name !=='Login' && !isAuthenticated) {
        next({ name: 'Login' })
    }
    else {
        next()
    }
})

export default router