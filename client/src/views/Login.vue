<template>
  <div class="limiter">
    <section class="login-container">
      <div class="side-overlay --sm">
        <figure style="position: absolute;bottom: 0;right: -40px;">
          <img
            :src="require(`@/assets/images/Saly-1.svg`)"
            class=""
            alt="floating_sally"
          >
        </figure>
      </div>

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
    </section>
  </div>
</template>

<script>
import { mapActions } from 'vuex';
import Swal from 'sweetalert2';
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
  methods: {
    ...mapActions(['LogIn']),
    async handleLogin() {
      this.login = 'Logging In...';
      this.isActive = false;
      const User = {
        email: this.email,
        password: this.password,
      };
      const re = /[a-zA-Z.]+@[lmu.edu.ng]/;
      if (!re.test(this.email)) {
        Swal.fire('Oops', 'You need to put a valid webmail', 'warning');
        this.login = 'Login';
        this.isActive = true;
      } else {
        await axios.post('/api/auth/login', User)
          .then((res) => {
            console.log(res.data);
            Swal.fire('Success', 'Logged In', 'success');
            const payload = { res, User };
            this.LogIn(payload);
            this.login = 'Login';
            this.isActive = false;
            this.$router.push('/categories');
          })
          .catch((error) => {
            const result = error.response.data;
            if (error.response.status !== 400) {
              Swal.fire('Oops!', `${result.error}`, 'warning');
            } else {
              Swal.fire('Oops', `${result.error}`, 'warning');
            }
            this.login = 'Login';
            this.isActive = false;
          });
      }
    },
  },
};
</script>

<style></style>
