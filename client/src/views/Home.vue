<template>
<div>
    <NavbarSm />
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
          <p class="float float__three float__four">
            2021
          </p>
          <div class="circle circle_one" />
          <div class="circle circle_two" />
          <div class="circle circle_three" />
          <div class="circle circle_four" />
          <div class="circle circle_five" />
        </div>
        <figure>
          <img
            src="https://ucarecdn.com/b46a9351-edb0-4982-87b8-d63199aa8108/Saly33.svg"
            width="380px"
            height="370px"
            alt="bob"
          >
          <img
            src="https://ucarecdn.com/0c495959-e10c-4845-86a8-4bcf4e2ee31d/Saly35.svg"
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
import NavbarSm from '../components/layout/NavbarSm.vue';
import Swal from 'sweetalert2';

export default {
  title: 'CBS Vote - Home Page',
  components: {
    Leads,
    NavbarSm,
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
  bottom: 2.625rem;
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
    font-size: 6.125rem;
    left: 144px;
    top: 214px;
  }
  .float__two {
    font-size: 7.125rem;
    left: 496px;
    top: 302px;
  }
  .float__three {
    font-size: 5.125rem;
    left: 579px;
    top: 388px;
  }
  .float__four {
    font-size: 3.125rem;
    left: 782px;
    top: 450px;
  }
  .float__one::after {
    width: 7em;
  }
  .float__three::after {
    width: 181px;
  }
  .float__four::after {
    width: 90px;
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
  #leads h1{
    padding-left: 3.75rem;
  }
  #leads h1::after{
    margin-left: 0.75rem;
  }
}
</style>
