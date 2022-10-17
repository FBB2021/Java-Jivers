// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
axios.defaults.withCredentials = true;
// axios.defaults.baseURL = "https://java-jivers-ims.herokuapp.com";
axios.defaults.baseURL = "http://127.0.0.1:8000/";

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isAuthenticated: "",
        isAdmin: "",
        user: "",
        token: "",
    },
    mutations: {
        /* initialiseStore based on https://github.com/SteinOveHelset/djackets_vue/blob/master/src/store/index.js */
        initialiseStore(state) {
            state.isAdmin = false;
            state.token = "";
            state.isAuthenticated = false;
            if (localStorage.getItem("token")) {
                state.token = localStorage.getItem("token");
                state.isAuthenticated = true;
            }
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
        set_token(state, token) {
            state.token = token;
        },
    },
    actions: {
        /* Login based on https://github.com/SteinOveHelset/djackets_vue/blob/master/src/store/index.js */
        async login(context, user) {
            await axios.post("api/token/", user).then((response) => {
                const token = response.data.access;
                context.commit("set_isAuthenticated", true);
                context.commit("set_user", user.username);
                context.commit("set_token", token);

                localStorage.setItem("token", token);

                user_type = "";

                const users_response = axios.get("users/userviewset/"{
                    withCredentials: this.state.token;
                });

                const user_data = JSON.parse(users_response);
                consolve.log(user_data);
                Object.entries(user_data).forEach((entry) => {
                    console.log(entry);
                    if (entry.username == user.username) {
                        user_type = entry.role;
                    }
                });

                if (user_type == "Admin") {
                    context.commit("set_isAdmin", true);
                } else {
                    context.commit("set_isAdmin", false);
                }
            });
        },
        async logout(context) {
            context.commit("set_isAuthenticated", false);
            context.commit("set_isAdmin", false);
            context.commit("set_user", "");
            context.commit("set_token", "");
        },
        refresh_token(context) {},
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
        get_token: (state) => {
            return state.token;
        },
    },
    plugins: [createPersistedState()],
});

export default store;
