<template>
    <div>
        <div class="hamburg">
            <div class="lines" @click="toggleSidebar()">
                <span class="line line1"></span>
                <span class="line line2"></span>
                <span class="line line3"></span>
                <span class="line line4"></span>
            </div>
        </div>
        <nav :class="{show:isSidebar}">
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
        </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data(){
        return {
            isSidebar: false,
        }
    },
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
        toggleSidebar() {
            this.isSidebar = !this.isSidebar
        }
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
.show {
    padding: 100px;
    width: 100%;
}
@media only screen and (max-width: 47.5rem){
    nav{
        position: fixed;
        z-index:100;
        top:0;
        left:0;
        padding: 0px;
        background-color: var(--blueTheme);
        overflow-x: hidden;
        transition: all 0.5s ease;
        display: flex;
        width: 0px;
        justify-content: space-around;
        flex-direction: column;
        align-items: center;
        opacity: 0.95;
        height: 100%;
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
    a {
        color: white;
    }
    .hamburg {
        background-color: #fff;
        padding: 20px;
        width: 100%;
        height: 10vh;
    }
    .lines {
        z-index: 999;
        cursor: pointer;
        position: absolute;
    }
    .line{
        height: .1875rem;
        width: 3.125rem;
        display: block;
        background-color: #000;
        margin-top: .3rem;
        /*create hamburger line*/
    }
    /*.line1{
        width: 4.0625rem;
    }*/
}
</style>
