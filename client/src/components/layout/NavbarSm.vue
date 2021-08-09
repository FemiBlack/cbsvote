<template>
        <nav>
            <div class="brand">
                CBS
            </div>
            <ul style="display: flex; justify-content: space-around;width: 50%;">
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li>
                    <a v-if="isLoggedIn" @click="logout" style="cursor:pointer;">Logout</a>
                    <router-link v-else to="/login">Login</router-link>
                </li>
                <li><router-link v-if="!isLoggedIn" to="/signup">Signup</router-link></li>
                <li><router-link v-if="isLoggedIn && user.role===2" to="/admin">Admin Panel</router-link></li>
            </ul>
        </nav>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    computed: {
        ...mapGetters({ user: "StateUser" }),
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

<style lang="scss" scoped>
a {
    font-weight: bold;
    color: black;

    &.router-link-exact-active {
        color: white;
      background: #2604F6;
      padding: 5px 6px;
      border-radius: 10px;
    }
  }
a.active.router-link-active {
    color: white;
    background: #2604F6;
    padding: 5px 6px;
    border-radius: 10px;
}
nav {
    position: absolute;
    padding-left: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    display: flex;
    width: 100%;
    justify-content: space-around;
    box-shadow: 0px 4px 4px 2px rgba(0, 0, 0, 0.25);
}
.brand {
    font-weight: bold;
}
@media only screen and (max-width: 47.5rem){
    nav{
        position: fixed;
        z-index:100;
        top:0;
        left:0;
        padding: 100px;
        background-color: var(--blueTheme);
        overflow-x: hidden;
        transition: all 0.5s ease;
        display: flex;
        width: 100%;
        justify-content: space-around;
        flex-direction: column;
    }
    nav .brand {
        text-align: center;
    }
    nav ul {
        display: flex;
        height: 80%;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
    }
    .hamburg {
        cursor: pointer;
        background-color: #fff;
        padding: 20px;
        width: 100%;
        z-index: 999;
        height: 10vh;
    }
    .line{
        height: .1875rem;
        width: 3.125rem;
        display: block;
        background-color: #000;
        margin-top: .5rem;
        /*create hamburger line*/
    }
    /*.line1{
        width: 4.0625rem;
    }*/
}
</style>
