<template>
    <nav>
        <ul class="nav-list">
            <router-link to="/"></router-link>
            <router-link to="/categories"></router-link>
            <router-link to="/login"></router-link>
            <router-link v-if="isLoggedIn && role===2" to="/admin">Admin Panel</router-link>
            <router-link v-if="isLoggedIn" @click="logout"></router-link>
        </ul>
    </nav>
</template>
<script>
export default {
    computed: {
        ...mapGetters({ role: "StateUserRole" }),
        isLoggedIn() {
            return this.$store.getters.isAuthenticated;
        },
    },
    methods: {
        async logout() {
            await this.$store.dispatch("LogOut");
            this.$router.push("/");
        },
    }
}
</script>

<style lang="scss">
nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
