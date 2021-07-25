<template>
<div class="limiter">
    <section class="login-container">
      <div
        class="side-overlay --sm"
        :style="
          `background-image: url(${require('@/assets/images/bg.png')});width: calc(100% - 900px);`
        "
      >
        <figure>
          <img
            :src="require('@/assets/images/Saly-37.svg')"
            style="position: absolute;bottom: 0;left: 0;animation-duration: 0;"
            alt="ball_point"
          />
        </figure>
      </div>
      <div class="wrap-login">
          <router-link to="/categories">back to categories</router-link>
        <h3>{{ catTypes[cat_type].toUpperCase() }}</h3>
      <!-- <header> -->
      <!-- </header> -->
        <div class="lead-card">
          <div class="lead-img" style="height: 200px;"></div>
          <div class="lead-bottom">
            <span class="lead-name">eku</span>
            <span class="lead-category">eme</span>
          </div>
        </div>
        <div class="lead-card">
          <div class="lead-img" style="height: 200px;"></div>
          <div class="lead-bottom">
            <span class="lead-name">eku</span>
            <span class="lead-category">eme</span>
          </div>
        </div>
        <div class="lead-card">
          <div class="lead-img" style="height: 200px;"></div>
          <div class="lead-bottom">
            <span class="lead-name">eku</span>
            <span class="lead-category">eme</span>
          </div>
        </div>
        <div class="lead-card">
          <div class="lead-img" style="height: 200px;"></div>
          <div class="lead-bottom">
            <span class="lead-name">eku</span>
            <span class="lead-category">eme</span>
          </div>
        </div>
      <!-- <div class="wrap-login" v-for="(nominee, k) in nominees" :key="k">
        <h3>{{ catTypes[cat_type].toUpperCase() }}</h3>
      <header>
      </header>
        <div class="lead-card">
          <div class="lead-img" style="height: 200px;" :style="Nominee.img"></div>
          <div class="lead-bottom">
            <span class="lead-name">{{ Nominee.name }}</span>
            <span class="lead-category">{{ Nominee.category }}</span>
          </div>
        </div> -->
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

const catTypes = Object.freeze({
  fashionablemale: 'Most Fashionable(male)',
  fashionablefemale: 'Most Fashionable(female)',
  nextgenmale: 'CBS Next Gen(male)',
  nextgenfemale: 'CBS Next Gen(female)',
  entreprenuermale: 'Entrepreneur of the year(male)',
  entreprenuerfemale: 'Entrepreneur of the year(female)',
  facemale: 'Face of CBS(male)',
  facefemale: 'Face of CBS(female)',
  sociablemale: 'Most Sociable(male)',
  sociablefemale: 'Most Sociable(female)',
  sportsperson: 'Sportsperson of the year(male)',
  sportspersonfemale: 'Sportsperson of the year(female)',
  innovativemale: 'Most Innovative(male)',
  innovativefemale: 'Most Innovative(female)',
});

export default {
  title: 'CBS Vote - Categories',
  name: 'CatType',
  props: {
    cat_type: {
      type: String,
      default: 'facemale',
    },
  },
  data() {
    return {
      nominees: [],
      catTypes,
    };
  },
  methods: {
    getTypes() {
      axios
        .get(`/api/category/${this.cat_type}`)
        .then((res) => {
          res.map((nominees) => {
            nominees.push({
              // eslint-disable-next-line no-underscore-dangle
              id: nominees._id.$oid,
              name: nominees.name,
              votes: nominees.vote[this.cat_type],
              reg_no: nominees.reg_no,
              img: `"background-image: url(${nominees.personImg})"`,
            });
            return true;
          });
        })
        .catch(() => {
          console.log('no connection to server');
        });
    },
  },
  created() {
    this.getTypes();
  },
};
</script>

<style scoped>
.lead-container {
  justify-items: center;
  font-family: Poppins;
  padding: 3.75rem;
  display: grid;
  /* grid-template-columns: repeat(auto-fill, minmax(calc(10% + 7.5rem), 1fr)); */
  /* grid-template-columns: repeat(auto-fit, minmax(min(10rem, 100%), 1fr)); */
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.25rem;
}
.lead-card {
  height: 18.75rem;
  width: 15.625rem;
  /* height: 267px; */
  /* border: .0625rem solid #777; */
  box-shadow: 0px 4px 4px 2px rgba(0, 0, 0, 0.25);
}
.lead-category {
  /* font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px; */
  display: block;
  color: #4d4d4d;
}
.lead-bottom {
  font-size: 1rem;
  padding: 1.25rem;
}
</style>
