<template>
  <section id="leads">
    <h1>LEADS</h1>
    <div class="lead-container">
      <div class="lead-card">
        <div class="lead-img" style="height: 200px;" :style="lead.img"></div>
        <div class="lead-bottom">
          <span class="lead-name">{{ lead.name }}</span>
          <span class="lead-category">{{ lead.category }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      leads: [],
    };
  },
  methods: {
    getLeads() {
      axios
        .get('/leads')
        .then((response) => {
          const leads = response.data;
          leads.map((lead) => {
            this.leads.push({
              id: leads.id,
              personId: lead.personId,
              reg_no: lead.reg_no,
              person: lead.person,
              category: lead.category,
              likes: lead.likes,
              img: `background-image: url(${lead.personImage});`,
              link: `/categories/${lead.category}`,
            });
          });
        })
        .catch(() => {
          console.log('error');
        });
    },
  },
  created() {
    this.GetLeads();
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
