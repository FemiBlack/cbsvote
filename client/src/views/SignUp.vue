<template>
  <div class="limiter">
  <section class="login-container">
    <div class="side-overlay --sm" style="z-index:2;">
      <figure style="position: absolute;bottom: 0;right: -40px;left:0;top:0;">
        <img
          src="https://ucarecdn.com/8f38df99-ef0a-4540-b3d9-2986e5b3d46e/saly28.svg"
          class=""
          alt="floating_sally"
        >
        <img
          style="position: absolute;bottom: 0;left:0;animation-duration: 0s;"
          src="https://ucarecdn.com/2f9793a5-a019-41eb-8020-44ff177e3058/Saly17.svg"
          alt="floating_sally"
        >
      </figure>
    </div>
    <NavSm size="56.4"/>
    <main>
    <div class="wrap-login">
      <form
        class="login100-form validate-form"
        method="post"
        @submit.prevent="Register()"
      >
        <span class="login100-form-title animate__animated animate__fadeInLeft">
          Sign-Up
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
            required
            placeholder="Enter Webmail"
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
            {{ signup }}
          </button>
          <p>
            Already have an account? <router-link to="/login">
              Login
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
import Swal from 'sweetalert2';
import NavSm from '@/components/layout/NavbarSm.vue';
import axios from 'axios';

export default {
  title: 'CBS Vote - Signup',
  name: '',
  data() {
    return {
      email: '',
      password: '',
      signup: 'Sign Up',
      isActive: false,
    };
  },
  components: {
    NavSm,
  },
  methods: {
    async Register() {
      this.signup = 'Signing Up...';
      this.isActive = true;
      const User = {
        email: this.email,
      };
      const re = /[a-zA-Z.]+@[lmu.edu.ng]/;
      if (!re.test(this.email)) {
        Swal.fire('Oops', 'You need to put a valid webmail', 'warning');
        this.signup = 'Sign Up';
        this.isActive = false;
      } else {
        await axios.post('/api/auth/signup', User)
          .then((res) => {
            console.log(res.data);
            Swal.fire('Success', 'Your account has been registered successfully. Please check your webmail for a login token!', 'success');
            this.signup = 'Sign Up';
            this.isActive = false;
          })
          .catch((error) => {
            const result = error.response.data;
            if (error.response.status === 404) {
              Swal.fire('Oops!', 'Seems like the server is down!', 'warning');
            } else if (error.response.status !== 400) {
              Swal.fire('Hey!', `${result.message}`, 'info');
            } else {
              Swal.fire('Oops', `${result.message}`, 'warning');
            }
            this.signup = 'Sign Up';
            this.isActive = false;
          });
      }
    },
    init() {
      this.email = '';
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
