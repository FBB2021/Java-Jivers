<!-- This is the dashboard layout for User -->

<template>
  <div class="wrapper">
    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/user/overview">
        <i class="nc-icon nc-chart-pie-35"></i>
        <p>Home</p>
      </sidebar-link>
      <sidebar-link to="/user/product">
        <i class="nc-icon nc-circle-09"></i>
        <p>Products</p>
      </sidebar-link>
      <sidebar-link to="/user/load">
        <i class="nc-icon nc-notes"></i>
        <p>Load</p>
      </sidebar-link>

      <template slot="bottom-links">
        <sidebar-link class="active"
                      to="/admin/NotFoundPage">
          <i class="nc-icon nc-settings-gear-64"></i>
          <p>Settings</p>
        </sidebar-link>
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click="toggleSidebar">

      </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">

</style>
<script>
  import TopNavbar from './TopNavbar.vue'
  import ContentFooter from './ContentFooter.vue'
  import DashboardContent from './Content.vue'
  export default {
    components: {
      TopNavbar,
      ContentFooter,
      DashboardContent,
      // MobileMenu
    },
    methods: {
      toggleSidebar () {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }

</script>
