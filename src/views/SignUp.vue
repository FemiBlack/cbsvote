<template>
  <section class="login-container">
        <div class="side-overlay --sm">
            <figure style="position: absolute;bottom: 0;right: -40px;">
                <img :src="require(`@/assets/Saly-1.svg`)" class="" alt="floating_sally">
            </figure>
        </div>

        <div class="wrap-login">
            <form @submit.prevent="handleLogin()" class="login100-form validate-form" method="post">
                <span class="login100-form-title animate__animated animate__fadeInLeft">
                    Sign-Up
                    <img :src="require(`@/assets/Futurama_Zoidberg.svg`)" alt="futurama">
                </span>
                <span class="login-subtitle animate__animated animate__flipInX">
                    You only vote once per category
                </span>

                <span class="login-error" id="login-error">
                    <!-- Invalid username! -->
                </span>
                <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
                    <i class="feather-mail icon"></i>
                    <input class="input100" v-model="email" id="email" type="text" name="email" placeholder="Enter Webmail">
                </div>

                <div class="container-login100-form-btn animate__animated animate__bounceInUp animate__delay-1s">
                    <button id="login_button" name="login_button" class="login100-form-btn">
                        Sign Up
                    </button>
                    <p>Not already have an account? <router-link to="/login">Login</router-link></p>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import { mapActions } from "vuex";

export default {
    title: '',
    name:'',
    data() {
        return {
            email,
            password
        }
    },
    methods: {
        ...mapActions(['Login']),
        handleLogin() {
            const User = {
                email: this.email,
                password: this.password
            }
            try {
                await this.LogIn(User);
            } catch(error) {
                console.log(error)
            }
            this.init()
        },
        init() {
          this.email = ""
        }
    }
}
</script>

<style>

</style>