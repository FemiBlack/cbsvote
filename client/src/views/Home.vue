<template>
<div>
    <nav>
        <div class="nav-list">
            <div class="brand">
                CBS
            </div>
            <ul>
                <li><router-link to="/" style="color: white;background: #2604F6; padding: 5px 6px;border-radius: 10px;">Home</router-link></li>
                <li><router-link to="/categories">Categories</router-link></li>
                <li><router-link to="/login">Login</router-link></li>
                <li><router-link to="/signup">Signup</router-link></li>
            </ul>
        </div>
    </nav>
  <div class="container">
    <div class="limiter">
      <main>
        <div class="des">
          <p class="float float__one">
            CBS official
          </p>
          <p class="float float__two">
            Voting
          </p>
          <p class="float float__three">
            site
          </p>
          <div class="circle circle_one" />
          <div class="circle circle_two" />
          <div class="circle circle_three" />
          <div class="circle circle_four" />
          <div class="circle circle_five" />
        </div>
        <figure>
          <img
            :src="require('@/assets/images/Saly-33.svg')"
            width="380px"
            height="370px"
            alt="bob"
          >
          <img
            :src="require('@/assets/images/Saly-35.svg')"
            alt="sally"
          >
        </figure>
        <router-link
          tag="button"
          to="/categories"
          class="cat_btn"
        >
          View Categories <i class="feather-chevron-right" />
        </router-link>
      </main>
    </div>
  </div>
  <Leads />
  </div>
</template>

<script>
import Leads from '../components/Leads.vue';
import Swal from 'sweetalert2';

export default {
  title: 'CBS Vote - Home Page',
  components: {
    Leads,
  },
  mounted(){
    Swal.fire('Man At Work!🔨🚧👷‍♂️', 'This site is currently under maintenance', 'info');
  }
};
</script>

<style scoped src="../assets/css/styles.css"></style>
<style scoped src="../assets/css/home.css"></style>
<style scoped>

.cat_btn {
  cursor: pointer;
  position: absolute;
  bottom: 0.625rem;
  left: 0.625rem;
  font-size: 0.75rem;
  line-height: 0.75rem;
  width: 8.125rem;
  height: 1.875rem;
  padding: 0.3125rem 0.5rem;
}
/* .cat_btn i{
    position: absolute;
    top: 38%;
    right: 1.875rem;
} */
figure {
  display: none;
}
@media only screen and (min-width: 33.75rem) {
  figure {
    display: block;
  }
  figure img:first-child {
    position: absolute;
    left: 20%;
    top: 25%;
  }
  figure img:nth-child(2) {
    position: absolute;
    left: 49.48%;
    right: 24.05%;
    top: 4%;
    bottom: 55.14%;
  }
  .cat_btn {
    width: 13.801875rem;
    height: 3.3125rem;
    left: 1.0625rem;
    bottom: 6%;
    font-size: 0.9375rem;
    line-height: 0.75rem;
  }
  .float__one {
    font-size: 3.125rem;
  }
  .float__two {
    font-size: 3.125rem;
  }
  .float__three {
    font-size: 3.125rem;
  }
  .float__one::after {
    width: 14em;
  }
  nav {
    padding: 10px;
    width:100%;
    height: 10vh;
    display: flex;
    position: relative;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    overflow: unset;
    background: transparent;
  }
  .brand {
      font-weight: bold;
  }
  .nav-list {
      flex-direction: row;
  }
  .nav-list ul{
      display: flex;
      justify-content: space-around;
      align-items: center;
      width: 50%;
  }
  .nav-list ul li a{
      color: #000;
      font-size: 14px;
  }
  .nav-list ul li::after{
      content: unset;
  }
}
</style>
