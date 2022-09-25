

// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        isAuthenticated: false,
        isAdmin: false,
        user: null
    },
    mutations: {
        initialiseStore(state){
            state.isAuthenticated = false
            state.isAdmin = false

        },
        login_authenticated (state, user_type, user){
            console.log(" "  + user_type);
            state.isAuthenticated = true;
            state.user = user;
            if (user_type == "admin"){
                state.isAdmin = true;
            }
            else{
                state.isAdmin = false;
            }
        },
        logout (state){
            state.isAuthenticated= false
            state.isAdmin= false
            state. user= null
        }
        
    }
})