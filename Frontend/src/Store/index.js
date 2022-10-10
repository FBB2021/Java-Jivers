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
        }
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
        component_did_mount(context){
            context.commit("get_session");
        },
        // https://github.com/duplxey/django-spa-cookie-auth/blob/master/django_react_cross_origin/frontend/src/App.js
        fetch_CSRF(context){
            axios.fetch("https://java-jivers-ims.herokuapp.com/Login/csrf",{
                credentials: "includes",
            })
            .then((res) => {
                context.commit("set_csrf", res.headers.get("X-CSRFToken"));
            })
            .catch((err) => {
                console.log(err);
            })
        },
        fetch_session(context){
            axios.fetch("https://java-jivers-ims.herokuapp.com/Login/session/",{
                credentials: "includes",
            })
            .then((res) => res.json())
            .then((data) => {
                if(data.isAuthenticated){
                    context.commit("set_isAuthenticated", true);
                }
                else{
                    context.commit("set_isAuthenticated", false);
                    this.fetch_CSRF();
                }
            })
            .catch((err) => {
                console.log(err);
            })
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

  whoami = () => {
    fetch("http://localhost:8000/api/whoami/", {
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
  }

  handlePasswordChange = (event) => {
    this.setState({password: event.target.value});
  }

  handleUserNameChange = (event) => {
    this.setState({username: event.target.value});
  }

  isResponseOk(response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  login = (event) => {
    event.preventDefault();
    fetch("http://localhost:8000/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": this.state.csrf,
      },
      credentials: "include",
      body: JSON.stringify({username: this.state.username, password: this.state.password}),
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: true, username: "", password: "", error: ""});
    })
    .catch((err) => {
      console.log(err);
      this.setState({error: "Wrong username or password."});
    });
  }

  logout = () => {
    fetch("http://localhost:8000/api/logout", {
      credentials: "include",
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: false});
      this.getCSRF();
    })
    .catch((err) => {
      console.log(err);
    });
  };

export default store;
