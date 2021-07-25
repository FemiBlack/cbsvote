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
      <!-- <header>
                <h3>Categories</h3>
            </header> -->
      <div class="wrap-login">
          <div v-for="(category, name) in categories" :key="name"  class="cat-border">
        <router-link :to="{name: 'CatType', params: {cat_type: name}}" class="cat-name">
            {{ category }}
        </router-link>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
const categories = {
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
};

export default {
  title: 'CBS Vote - Categories',
  name: 'Categories',
  data() {
    return {
      categories,
    };
  },
};
</script>
<style scoped>
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
    }
}
</style>
