import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Overview from 'src/pages/Overview.vue'
import User_overview from 'src/pages/User/Overview.vue'
import UserProfile from 'src/pages/UserProfile.vue'
import TableList from 'src/pages/TableList.vue'
import Account from 'src/pages/Account.vue'
import Analytics from 'src/pages/analytics.vue'
import Login from 'src/pages/Login.vue'


const routes = [
  {
    path: '/',
    component: Login,
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/overview',
    children: [
      {
        path: 'overview',
        name: 'Overview',
        component: Overview
      },
      {
        path: 'user',
        name: 'User',
        component: UserProfile
      },
      {
        path: 'table-list',
        name: 'Table List',
        component: TableList
      },
      {
        path: 'account',
        name: 'Account',
        component: Account
      },
      {
        path: 'analytics',
        name: 'Analytics',
        component: Analytics
      }
    ]
  },
  {
    path: '/user',
    component: DashboardLayout,
    redirect: '/user/overview',
    children: [
      {
        path: 'overview',
        name: 'User_overview',
        component: User_overview
      },
      {
        path: 'user',
        name: 'User',
        component: UserProfile
      },
      {
        path: 'table-list',
        name: 'Table List',
        component: TableList
      },
      {
        path: 'account',
        name: 'Account',
        component: Account
      },
      {
        path: 'analytics',
        name: 'Analytics',
        component: Analytics
      }
    ]
  },
  { path: '*', component: NotFound }
];


/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/


export default routes
