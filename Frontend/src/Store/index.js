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
        password: "",
        csrf: "",
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
        set_csrf(state, csrf) {
            state.csrf = csrf;
        },
        set_password(state, password) {
            state.password = password;
        },
    },
    actions: {
        logout(context) {
            axios
                .fetch("http://localhost:8000/Login/logout", {
                    credentials: "include",
                })
                .then(this.this.is_response_ok)
                .then((data) => {
                    console.log(data);
                    context.commit("set_isAuthenticated", false);
                    context.commit("set_isAdmin", false);
                    context.commit("set_user", null);
                    context.commit("set_password", null);
                    this.fetch_CSRF();
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        login(context, user_data) {
            axios
                .fetch("https://java-jivers-ims.herokuapp.com/Login/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": this.state.csrf,
                    },
                    credentials: "include",
                    body: JSON.stringify({
                        username: user_data.username,
                        password: user_data.password,
                    }),
                })
                .then(this.is_response_ok)
                .then((data) => {
                    console.log(data);
                    context.commit("set_isAuthenticated", true);
                    context.commit("set_isAdmin", true);
                    context.commit("set_user", null);
                    context.commit("set_password", null);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        component_did_mount(context) {
            context.commit("get_session");
        },
        // https://github.com/duplxey/django-spa-cookie-auth/blob/master/django_react_cross_origin/frontend/src/App.js
        fetch_CSRF(context) {
            axios
                .fetch("https://java-jivers-ims.herokuapp.com/Login/csrf", {
                    credentials: "includes",
                })
                .then((res) => {
                    context.commit("set_csrf", res.headers.get("X-CSRFToken"));
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        fetch_session(context) {
            axios
                .fetch("https://java-jivers-ims.herokuapp.com/Login/session/", {
                    credentials: "includes",
                })
                .then((res) => res.json())
                .then((data) => {
                    if (data.isAuthenticated) {
                        context.commit("set_isAuthenticated", true);
                    } else {
                        context.commit("set_isAuthenticated", false);
                        this.fetch_CSRF();
                    }
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        whoami(context) {
            axios
                .fetch("https://java-jivers-ims.herokuapp.com/Login/whaomi/", {
                    headers: {
                        "Content-Type": "application/json",
                    },
                    credentials: "include",
                })
                .then((res) => res.json())
                .then((data) => {
                    console.log("You are logged in as: " + data.username);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        is_response_ok(response) {
            if (response.status >= 200 && response.status <= 299) {
                return response.json();
            } else {
                throw Error(response.statusText);
            }
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
