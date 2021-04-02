import axios from 'axios'
import store from '../store/index'

export default axios.create({
    baseUrl: store.state.backendAPIs.rootAPI,
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + localStorage.getItem('hust-mdbsys-token')
    },
    xsrfCookieName: 'csrf-token',
    xsrfHeaderName: 'X-CSRFToken',
    withCredentials: true,
})