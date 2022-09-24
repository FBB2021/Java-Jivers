import {createStore} from 'vuex'

// Store, term used for state management system using vuex.
// Using to manage authentication

export default createStore({
    state:{
        isAuthenticated: false,
        isAdmin: false,
        token: '',
    },
    mutations: {
        // based on https://github.com/SteinOveHelset/djackets_vue/blob/master/src/store/index.js
        initialiseStore(state){
            if (localStoreage.getItem('token')){
                state.token = localStoreage.getItem('token')
                state.isAuthenticated = true
            }
            else{
                state.token = ''
                state.isAuthenticated = false
                state.isAdmin = false
            }
        },
        setToken(state, token){
            state.token = token
            state.isAuthenticated = true
        },
        removeToke(state){
            state.token = ''
            state.isAuthenticated = false
            state.isAdmin = false
        }
    }
})

const app = createApp