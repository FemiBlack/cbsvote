<template>
  <div id="app">
    <!-- <Header /> -->
      <transition name="slide" mode="out-in">
        <router-view />
      </transition>
    <!-- </div> -->
    <!-- <Footer /> -->
  </div>
</template>

<script>
// import Header from '@/components/layout/Header.vue';
// import Footer from '@/components/layout/Footer.vue';

export default {
  components: {
    // Header,
    // Footer,
  },
};
</script>
<style lang="scss">
@import './assets/css/style.css';
// #app {
//   font-family: Spartan, Poppins, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }
.slide-enter-active,
.slide-leave-active {
  transition: opacity .5s, transform .5s;
}
.slide-enter,
.slide-leave-to{
  opacity: 0;
  transform: translateX(-30%)
}
</style>
