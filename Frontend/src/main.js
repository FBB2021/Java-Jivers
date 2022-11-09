/*!

 =========================================================
 * Vue Light Bootstrap Dashboard - v2.0.0 (Bootstrap 4)
 =========================================================

 * Product Page: http://www.creative-tim.com/product/light-bootstrap-dashboard
 * Copyright 2019 Creative Tim (http://www.creative-tim.com)
 * Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard/blob/master/LICENSE.md)

 =========================================================

 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 */
import Vue from "vue";
import Vuex from "vuex";
import VueRouter from "vue-router";
import App from "./App.vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import store from "./Store";
import echarts from "echarts";
import VueSimpleAlert from "vue-simple-alert";
import axios from "axios";

// LightBootstrap plugin
import LightBootstrap from "./light-bootstrap-main";
// import ApexCharts from 'apexcharts'
import VueApexCharts from "vue-apexcharts";

// router setup
import routes from "./routes/routes";

import "./registerServiceWorker";
// plugin setup
Vue.use(VueRouter);
Vue.use(LightBootstrap);
Vue.use(ElementUI);
Vue.use(Vuex);
Vue.use(VueSimpleAlert);
// Vue.use(ApexCharts)

Vue.component("apexchart", VueApexCharts);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "https://java-jivers-ims.herokuapp.com/";
axios.interceptors.response.use(undefined, function (error) {
    if (error) {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            store.dispatch("refresh_token");
        }
    }
});
Vue.prototype.$echarts = echarts;
Vue.prototype.$currentID = 0;

// configure router
const router = new VueRouter({
    routes, // short for routes: routes
    linkActiveClass: "nav-item active",
    scrollBehavior: (to) => {
        if (to.hash) {
            return { selector: to.hash };
        } else {
            return { x: 0, y: 0 };
        }
    },
});

/* eslint-disable no-new */
new Vue({
    el: "#app",
    render: (h) => h(App),
    store,
    router,
    data: function () {
        return {
            ITEMID: 0,
        };
    },
});
