// Store, term used for state management system using vuex.
// Using to manage authentication
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import axios from "axios";
axios.defaults.withCredentials = true;
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

            const response = axios.get("users/userviewset/", {
                headers: {
                    Authorization:
                        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNDcyODE2LCJpYXQiOjE2NjUyODg4MTYsImp0aSI6IjRhODIxMzNjNjVlNDQzM2Q5NmMzNTFkZGE1MDA3OTI1IiwidXNlcl9pZCI6M30.oweqpwzoDJ4VOYrkfI0yXUXTHDhGQA9a4HTxMC1HaV0",
                },
            });

            const user_data = JSON.parse(response);
            consolve.log(user_data);
            Object.entries(user_data).forEach((entry) => {
                console.log(entry);
                if (entry.username == user.username) {
                    user_type = entry.role;
                }
            });
            if (user_type == "Admin") {
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
            context.commit("login_authenticated", ["Admin", user]);
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
