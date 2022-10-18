import DashboardLayout from "../layout/DashboardLayout.vue";
import UserDashboardLayout from "../layout/UserDashboardLayout.vue";
// GeneralViews
import NotFound from "../pages/NotFoundPage.vue";

//Login page
import Login from "src/pages/Login.vue";

// Admin pages
import Overview from "src/pages/Admin/Overview.vue";
import AdminProduct from "src/pages/Admin/Product.vue";
import TableList from "src/pages/Admin/TableList.vue";
import Account from "src/pages/Admin/Account.vue";
import Analytics from "src/pages/Admin/analytics.vue";
import NewItem from "src/pages/Admin/NewItem.vue";
import EditItem from "src/pages/Admin/EditItem.vue";

// User pages
import User_overview from "src/pages/User/Overview.vue";
import User_Product from "src/pages/User/Product.vue";
import User_load from "src/pages/User/Load.vue";

import store from "src/Store";

const routes = [
    {
        path: "/",
        component: Login,
        redirect: "/login",
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    // The admin paths
    {
        path: "/admin",
        component: DashboardLayout,
        beforeEnter: (to, from, next) => {
            const is_admin = store.getters.get_isAdmin;
            const is_logged_in = store.getters.get_isAuthenticated;

            if (!is_admin) {
                console.log(
                    "Attempting to access admin level page, without privileges. Currently logged in as " +
                        store.getters.get_user
                );
                if (is_logged_in) {
                    return next("/user");
                } else {
                    return next("/login");
                }
            } else {
                return next();
            }
        },
        redirect: "/admin/overview",
        children: [
            {
                path: "overview",
                name: "Overview",
                component: Overview,
            },
            {
                path: "product",
                name: "Product",
                component: AdminProduct,
            },
            {
                path: "newItem",
                name: "NewItem",
                component: NewItem,
            },
            {
                path: "editItem",
                name: "EditItem",
                component: EditItem,
            },
            {
                path: "table-list",
                name: "Table List",
                component: TableList,
            },
            {
                path: "account",
                name: "Account",
                component: Account,
            },
            {
                path: "analytics",
                name: "Analytics",
                component: Analytics,
            },
        ],
    },
    // User Paths
    {
        path: "/user",
        component: UserDashboardLayout,
        beforeEnter: (to, from, next) => {
            const logged_in = store.getters.get_isAuthenticated;

            if (!logged_in) {
                next("/login");
            } else {
                next();
            }
        },
        redirect: "/user/overview",
        children: [
            {
                path: "overview",
                name: "User_overview",
                component: User_overview,
            },
            {
                path: "product",
                name: "Product",
                component: User_Product,
            },
            {
                path: "load",
                name: "Load",
                component: User_load,
            },
        ],
    },
    { path: "*", component: NotFound },
];

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
