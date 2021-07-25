<template>
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
          type="button"
          to="/categories"
          class="cat_btn"
        >
          View Categories <i class="feather-chevron-right" />
        </router-link>
      </main>
    </div>
    <Leads />
  </div>
</template>

<script>
import Leads from '../components/Leads.vue';

export default {
  title: 'CBS Vote - Home Page',
  components: {
    Leads,
  },
};
</script>

<style scoped>
@import '../assets/css/home.css';
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
}
</style>
