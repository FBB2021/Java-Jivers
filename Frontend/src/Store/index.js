// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
axios.defaults.baseURL = "http://127.0.0.1:8000/";

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isAuthenticated: false,
        isAdmin: false,
        user: "",
    },
    mutations: {
        initialiseStore(state) {
            state.isAuthenticated = false;
            state.isAdmin = false;
        },
        set_isAuthenticated(state, value) {
            state.isAuthenticated = value;
        },
        set_isAdmin(state, value) {
            state.isAdmin = value;
        },
        set_user(state, user) {
            state.user = user;
        },
        login_authenticated(state, [user_type, user]) {
            state.isAuthenticated = true;
            state.user = user.username;

            if (user_type == "admin") {
                state.isAdmin = true;
            } else {
                state.isAdmin = false;
            }
        },
    },
    actions: {
        async login(context, user) {
            console.log(user);
            await axios.post("api/token/", user);
            await context.commit("login_authenticated", ["admin", user]);
        },
        logout(context) {
            context.commit("set_isAuthenticated", false);
            context.commit("set_isAdmin", false);
            context.commit("set_user", null);
        },
    },
    getters: {
        get_isAuthenticated: (state) => {
            return state.isAuthenticated;
        },
        get_isAdmin: (state) => {
            return state.isAdmin;
        },
        get_user: (state) => {
            return state.user;
        },
    },
    //plugins: [createPersistedState()],
});

export default store;
