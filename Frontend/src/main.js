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
import Vue from 'vue'
import Vuex from "vuex";
import VueRouter from 'vue-router'
import App from './App.vue'
import store from './Store'


// LightBootstrap plugin
import LightBootstrap from './light-bootstrap-main'

// router setup
import routes from './routes/routes'

import './registerServiceWorker'
// plugin setup
Vue.use(VueRouter)
Vue.use(LightBootstrap)
Vue.use(Vuex)

// configure router
const router = new VueRouter({
  routes, // short for routes: routes
  linkActiveClass: 'nav-item active',
  scrollBehavior: (to) => {
    if (to.hash) {
      return {selector: to.hash}
    } else {
      return { x: 0, y: 0 }
    }
  }
})


router.beforeEach((to, from, next) =>{
  const public_pages = ['/login', '/', '*']
  const auth_required = !public_pages.includes(to.path);
  const admin_required = ['/admin'];
  const logged_in = localStorage.getItem('isAuthenticated');
  const is_admin = localStorage.getItem('isAdmin');

  console.log(" " + logged_in)

  // Case for not logged in 
  if (auth_required && !logged_in){
    console.log("Not logged in");
    return next('/login');
  }
  // Case for logged in, but not admin
  else if (auth_required && admin_required && logged_in && !is_admin){
    return next('*');
  }
  // Admin can access any page, might make it so admin can only access user page
  next();
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  store,
  router
})
