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
            /* Check if the login details are correct, and login user */
            await axios.post("api/token/", user).then((response) => {
                const token = response.data.access;
                context.commit("set_isAuthenticated", true);
                context.commit("set_user", user.username);
                context.commit("set_token", token);

                localStorage.setItem("token", token);
            });
            /* Now we have to determine the role of the user */
            /* get the entire user database */
            const users_response = await axios.get("users/userviewset/");
            const user_data = users_response.data;
            const user_data_keys = Object.keys(user_data);
            const user_attributes = Object.keys(user_data[user_data_keys[0]]);

            var index_username = 0;
            var index_role = 0;
            //* find the index of username and role
            for (let i = 0; i < user_attributes.length; i++) {
                if (user_attributes[i] == "username") {
                    index_username = i;
                } else if (user_attributes[i] == "role") {
                    index_role = i;
                }
            }
            /* set admin to be false, if a match is found and the role is admin, we will change this to true */
            context.commit("set_isAdmin", false);

            for (let j = 0; j < user_data_keys.length; j++) {
                let current_user_data = Object.values(
                    user_data[user_data_keys[j]]
                );
                let username = current_user_data[index_username];
                let user_role = current_user_data[index_role];
                if (username == user.username && user_role == "Admin") {
                    context.commit("set_isAdmin", true);
                }
            }
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
