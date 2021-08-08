<template>
  <div class="limiter">
    <section class="login-container">
      <div class="side-overlay --sm" style="z-index:2;">
        <figure style="position: absolute;bottom: 0;right: -40px;">
          <img
            src="https://ucarecdn.com/aebdda3a-15d6-47a0-8f21-7def967d803c/Saly1.svg"
            class=""
            alt="floating_sally"
          >
        </figure>
      </div>
      <NavSm />
      <main>
      <div class="wrap-login">
        <form
          class="login100-form validate-form"
          method="post"
          @submit.prevent="handleLogin()"
        >
          <span class="login100-form-title animate__animated animate__fadeInLeft">
            Login
            <img
              :src="require(`@/assets/images/Futurama_Zoidberg.svg`)"
              alt="futurama"
            >
          </span>
          <span class="login-subtitle animate__animated animate__flipInX">
            You only vote once per category
          </span>

          <span
            id="login-error"
            class="login-error"
          >
          <!-- Invalid username! -->
          </span>
          <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
            <i class="feather-mail icon" />
            <input
              id="email"
              v-model="email"
              class="input100"
              type="text"
              name="email"
              placeholder="Enter Webmail"
            >
          </div>

          <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
            <i class="feather-lock icon" />
            <span class="btn-show-pass">
              <span>Show</span>
            </span>
            <input
              id="password"
              v-model="password"
              class="input100 mo100"
              type="password"
              name="pass"
              placeholder="Enter Password"
            >
          </div>

          <div
            class="container-login100-form-btn
          animate__animated animate__bounceInUp animate__delay-1s"
          >
            <button
              id="login_button"
              name="login_button"
              class="login100-form-btn"
              :disabled="isActive"
            >
              {{ login }}
            </button>
            <p>
              Not registered? <router-link to="/signup">
                Sign Up
              </router-link>
            </p>
          </div>
        </form>
      </div>
      </main>
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import Swal from 'sweetalert2';
import NavSm from '@/components/layout/NavbarSm.vue';
import axios from 'axios';

export default {
  title: 'CBS Vote - Login',
  name: '',
  data() {
    return {
      email: '',
      password: '',
      isActive: false,
      login: 'Login',
    };
  },
  components: {
    NavSm,
  },
  methods: {
    ...mapActions(['LogIn']),
    async handleLogin() {
      this.login = 'Logging In...';
      this.isActive = true;
      const User = {
        email: this.email,
        password: this.password,
      };
      const re = /[a-zA-Z.]+@[lmu.edu.ng]/;
      if(this.email == '' || this.password == ''){
        Swal.fire('😒', 'Cant leave blank fields!', 'warning');
        this.login = 'Login';
        this.isActive = false;
      } else if (!re.test(this.email)) {
        Swal.fire('🤔', 'Your webmail seems weird', 'warning');
        this.login = 'Login';
        this.isActive = false;
      } else {
        await axios.post('/api/auth/login', User)
          .then((res) => {
            Swal.fire('Success', 'Logged In', 'success');
            const payload = { res, User };
            this.LogIn(payload);
            this.login = 'Login';
            this.isActive = false;
            this.$router.push('/categories');
          })
          .catch((error) => {
            const result = error.response.data;
            if (error.response.status === 404) {
              Swal.fire('🛸!', 'Seems like the server is down!', 'warning');
            } else if(error.response.status !== 400) {
              Swal.fire('Oops', `${result.message || result.error}`, 'warning');
            } else {
              Swal.fire('?', 'Something\'s wrong try again', 'warning');
            }
            this.login = 'Login';
            this.isActive = false;
          });
      }
    },
  },
};
</script>

<style scoped>
nav{
  background:white;
  z-index: 1;
}
</style>
