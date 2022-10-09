// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

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
        log_out(state) {
            state.isAuthenticated = false;
            state.isAdmin = false;
            state.user = "";
        },
    },
    actions: {
        logout(context) {
            context.commit("set_isAuthenticated", false);
            context.commit("set_isAdmin", false);
            context.commit("set_user", null);
        },
        async login(context, user) {
            await axios.post("login", user);
            context.commit("set_user", user.get("username"));
            context.commit("set_isAuthenticated", true);
            context.commit("set_isAdmin", true);
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
});

export default store;
