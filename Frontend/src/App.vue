<template>
    <div :class="{ 'nav-open': $sidebar.showSidebar }">
        <notifications></notifications>
        <router-view></router-view>
    </div>
</template>

<script>
/*
import Axios from "axios";
const todoUrl = "http://localhost:3500/todo";
**/

import axios from "axios";

export default {
    /* beforeCreate based on https://github.com/SteinOveHelset/djackets_vue/blob/master/src/App.vue */
    beforeCreate() {
        this.$store.commit("initialiseStore");

        const token = this.$store.state.token;

        if (token) {
            axios.defaults.headers.common["Authorization"] = "Token " + token;
        } else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
};
</script>

<style lang="scss">
.vue-notifyjs.notifications {
    .list-move {
        transition: transform 0.3s, opacity 0.4s;
    }
    .list-item {
        display: inline-block;
        margin-right: 10px;
    }
    .list-enter-active {
        transition: transform 0.2s ease-in, opacity 0.4s ease-in;
    }
    .list-leave-active {
        transition: transform 1s ease-out, opacity 0.4s ease-out;
    }

    .list-enter {
        opacity: 0;
        transform: scale(1.1);
    }
    .list-leave-to {
        opacity: 0;
        transform: scale(1.2, 0.7);
    }
}
</style>
