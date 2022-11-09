<!-- This is the dashboard layout  -->

<template>
    <div class="wrapper">
        <side-bar>
            <mobile-menu slot="content"></mobile-menu>
            <sidebar-link to="/admin/overview">
                <i class="nc-icon nc-chart-pie-35"></i>
                <p>Home</p>
            </sidebar-link>
            <sidebar-link to="/admin/product">
                <i class="nc-icon nc-circle-09"></i>
                <p>Products</p>
            </sidebar-link>
            <sidebar-link to="/admin/table-list">
                <i class="nc-icon nc-notes"></i>
                <p>Load</p>
            </sidebar-link>
            <sidebar-link to="/admin/account">
                <i class="nc-icon nc-paper-2"></i>
                <p>Account</p>
            </sidebar-link>
            <sidebar-link to="/admin/analytics">
                <i class="nc-icon nc-atom"></i>
                <p>Analytics</p>
            </sidebar-link>
        </side-bar>
        <div class="main-panel">
            <top-navbar></top-navbar>

            <dashboard-content @click="toggleSidebar"> </dashboard-content>

            <content-footer></content-footer>
        </div>
    </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
export default {
    components: {
        TopNavbar,
        ContentFooter,
        DashboardContent,
        // MobileMenu
    },
    methods: {
        toggleSidebar() {
            if (this.$sidebar.showSidebar) {
                this.$sidebar.displaySidebar(false);
            }
        },
    },
};
</script>
