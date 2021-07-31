<template>
  <section id="leads">
    <h1>LEADS</h1>
    <div class="lead-container">
      <div class="lead-card" v-for="(lead,i) in leads" :key="i">
        <div class="lead-img" style="height: 200px;"
        :style="{ backgroundImage: 'url(' +lead.img+')' }"></div>
        <div class="lead-bottom">
          <span class="lead-name">{{ lead.name }}</span>
          <router-link tag="span"
          :to="{name: 'CatType', params: { cat_type: lead.category.name }}"
          class="lead-category"
          style="cursor:pointer;">
            {{ catTypes[lead.category.name] }}
          </router-link>
          <span class="lead-category">Leading by {{ lead.category.votes }} votes</span>
        </div>
      </div>
    </div>
  </section>
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
  sportspersonmale: 'Sportsperson of the year(male)',
  sportspersonfemale: 'Sportsperson of the year(female)',
  innovativemale: 'Most Innovative(male)',
  innovativefemale: 'Most Innovative(female)',
});

export default {
  data() {
    return {
      leads: [],
      catTypes,
      count: 0,
    };
  },
  // computed: {
  //   const max = this.leads.category.reduce((prev,curr) => (prev.votes > curr.votes) ? prev : curr, null)
  //   return max;
  // },
  methods: {
    // getCatVote(catItem){
    //   var keys = Object.keys(this.catTypes);
    //   var currCat = catItem.find(x => x.name == keys[this.count]);
    //   console.log(this.count, currCat);
    //   // this.count += 1;
    //   return currCat.votes;
    // },
    // getCatName(catItem){
    //   var keys = Object.keys(this.catTypes);
    //   var currCat = catItem.find(x => x.name == keys[this.count]);
    //   // console.log(this.count, currCat);
    //   this.count += 1;
    //   return currCat.name;
    // },
    getLeads() {
      axios
        .get('/api/leads')
        .then((response) => {
          let count = this.count;
          const leadRes = response.data;
          const keys = Object.keys(this.catTypes);

          // console.log(JSON.parse(leadRes[0]))
          leadRes.map(lead => {
            this.leads.push({
              id: JSON.parse(lead)._id.$oid,
              name: JSON.parse(lead).name,
              category: JSON.parse(lead).category.find(x => x.name === keys[count]),
              img: JSON.parse(lead.img),
            });
            count+=1;
            return true;
          });
        })
        .catch((error) => {
          console.log('error: '+ error);
        });
        console.log(this.count)
    },
  },
  created() {
    this.getLeads();
  },
};
</script>

<style scoped>
#leads h1 {
  padding: 1.875rem 0rem 1.25rem 3.75rem;
  position: relative;
}
#leads h1::after {
  content: "";
  position: absolute;
  background-color: #000;
  height: 0.3125rem;
  width: 6.25rem;
  bottom: 0;
  left: 0;
  margin-left: 3.75rem;
}
.lead-img {
  background-color: #777;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
}
.lead-container {
  justify-items: center;
  font-family: Poppins;
  padding: 3.75rem;
  display: grid;
  /* grid-template-columns: repeat(auto-fill, minmax(calc(10% + 7.5rem), 1fr)); */
  /* grid-template-columns: repeat(auto-fit, minmax(min(10rem, 100%), 1fr)); */
  grid-template-columns: repeat(auto-fit, 350px);
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
