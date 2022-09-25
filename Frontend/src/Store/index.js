

// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

 const store = new Vuex.Store({
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
            console.log(" "  + user_type + state.isAuthenticated);
        },
        logout (state){
            state.isAuthenticated= false
            state.isAdmin= false
            state. user= null
        },
        get_isAuthenticated(state){
            return state.isAuthenticated
        }
        
    },
    actions: {
        login (context, user_type, user){
            context.commit('login_authenticated', user_type, user)
        }
    }
})

export default store