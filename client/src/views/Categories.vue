<template>
  <div class="limiter">
    <section class="login-container">
      <div
        class="side-overlay --sm"
        :style="
          `background-image: url(${require('@/assets/images/nathan-anderson-9o-VrJSwGuw-unsplash.jpg')});
          width: calc(100% - 900px);z-index:2;`
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
      <NavSm />
      <main>
        <h1 style="padding-left: 130px;padding-top: 100px;">Categories</h1>
			  <div class="wrap-login" style="padding-left: 130px;">
          <div v-for="(category, name) in categories" :key="name"  class="cat-border">
            <router-link :to="{name: 'CatType', params: {cat_type: name}}" class="cat-name">
                {{ category }}
            </router-link>
          </div>
        </div>
      </main>
    </section>
  </div>
</template>
<script>
import NavSm from '@/components/layout/NavbarSm.vue';

const categories = {
  fashionablemale: 'Most Fashionable(male)',
  fashionablefemale: 'Most Fashionable(female)',
  nextgenmale: 'CBS Next Gen(male)',
  nextgenfemale: 'CBS Next Gen(female)',
  entrepreneurmale: 'Entrepreneur of the year(male)',
  entrepreneurfemale: 'Entrepreneur of the year(female)',
  facemale: 'Face of CBS(male)',
  facefemale: 'Face of CBS(female)',
  sociablemale: 'Most Sociable(male)',
  sociablefemale: 'Most Sociable(female)',
  sportspersonmale: 'Sportsperson of the year(male)',
  sportspersonfemale: 'Sportsperson of the year(female)',
  innovativemale: 'Most Innovative(male)',
  innovativefemale: 'Most Innovative(female)',
};

export default {
  title: 'CBS Vote - Categories',
  name: 'Categories',
  data() {
    return {
      categories,
    };
  },
  components: {
    NavSm,
  },
};
</script>
<style scoped>
main h1::after {
  content: "";
  position: absolute;
  background-color: #000;
  height: 0.3125rem;
  width: 6.25rem;
  bottom: 0;
  left: 0;
  margin-left: 3.75rem;
}
nav{
  background:white;
  z-index: 1;
}
.wrap-login{
  display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 20px;
    /* grid-template-columns:minmax(1fr 1fr) */

}
.cat-border {
  border: 1.5px solid #2604F6;
  border-radius: 15px;
  padding: 10px;
  width: 281px;
  display: flex;
  height: 66px;
  margin-bottom: 26px;
  overflow-wrap: break-word;
  transition: all .3s ease-in;
}
.cat-border a{
  color: rgb(54, 52, 52);
}
.cat-border:hover {
    /* box-shadow: 0px 4px 4px 2px rgba(0, 0, 0, 0.25); */
  	box-shadow: 0rem .25rem .625rem .1875rem rgba(0, 0, 0, 0.11);

}
.cat-name {
    margin: auto;
    font-family: Montserrat, sans-serif;
    font-weight: bold;
    /* font-size: 20px; */
    /* line-height: 26px; */
    /* or 40% */

    text-align: center;

}
@media only screen and (max-width:760px){
    .wrap-login{
        grid-template-columns: 1fr;
	padding-left: .9375rem;
	width:auto;
    }
    h1{
    	padding-left:90px;
    }
}
</style>
