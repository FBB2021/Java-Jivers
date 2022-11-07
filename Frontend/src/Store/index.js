// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "https://java-jivers-ims.herokuapp.com/";

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        isAuthenticated: "",
        isAdmin: "",
        user: "",
        token: "",
        refresh: "",
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
            if (localStorage.getItem("refresh")) {
                state.refresh = localStorage.getItem("refresh");
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
        set_refresh(state, refresh) {
            state.refresh = refresh;
        },
    },
    actions: {
        /* Login based on https://github.com/SteinOveHelset/djackets_vue/blob/master/src/store/index.js */
        async login(context, user) {
            /* Check if the login details are correct, and login user */
            await axios.post("api/token/", user).then((response) => {
                const token = response.data.access;
                const refresh = response.data.refresh;
                context.commit("set_isAuthenticated", true);
                context.commit("set_user", user.username);
                context.commit("set_token", token);
                context.commit("set_refresh", refresh);

                localStorage.setItem("token", token);
                localStorage.setItem("refresh", refresh);
            });
            /* Now we have to determine the role of the user */
            /* get the user based on username from database, then check role and store it*/
            await axios
                .get("users/userviewset?name=" + context.user)
                .then((response) => {
                    const user_role = response.role;
                    if (user_role == "Admin") {
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
