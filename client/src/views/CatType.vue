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
          <!-- <img
            :src="require('@/assets/images/Saly-37.svg')"
            style="position: absolute;bottom: 0;left: 0;animation-duration: 0;"
            alt="ball_point"
          /> -->
        </figure>
      </div>
      <NavSm />
      <main>
        <h1 style="padding-left: 50px;padding-top: 100px;background:white;">
        {{ catTypes[cat_type].toUpperCase() }}
        </h1>
        <div class="wrap-login" v-if="nominees[0]">
          <div class="lead-card" v-for="(nominee,k) in nominees" :key="k" @dblclick="Vote(nominee.id,nominee.name)">
            <div class="lead-img"
            :style="{ backgroundImage: 'url(' +nominee.img+')' }"></div>
            <div class="lead-bottom">
              <span class="lead-name">{{ nominee.name }}</span>
              <span class="lead-category">{{ departments[nominee.department] }}</span>
              <div class="heart" v-if="!hasVoted" @click="Vote(nominee.id,nominee.name)">
                <span><i class="feather-heart"></i> Vote</span>
              </div>
              <div class="heart" v-else @click="Vote()">
                <i class="feather-lock"></i>
                <span>Vote</span>
              </div>
            </div>
          </div>
        </div>
        <div class="lead-container" v-if="nominees[0]">
          <p>No nominees have been added under this category...</p>
        </div>
      </main>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import { mapGetters } from 'vuex';
import NavSm from '@/components/layout/NavbarSm.vue';

const departments = Object.freeze({
  accounting: 'Accounting',
  bfn: 'Banking & Finance',
  busadmin: 'Business Admin',
  eco: 'Economics',
  interel: 'International Relations',
  masscom: 'Mass Communication',
  soc: 'Sociology',
});

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
      departments,
      hasVoted: false,
    };
  },
  components: {
    NavSm,
  },
  computed:{
    ...mapGetters({ user: "StateUser" }),
  },
  methods: {
    getTypes() {
      axios
        .get(`/api/category/${this.cat_type}`)
        .then((res) => {
          res.data.map((nominee) => {
            const item = nominee.category.find((item) =>item.name === this.cat_type);
            this.nominees.push({
              // eslint-disable-next-line no-underscore-dangle
              id: nominee._id.$oid,
              name: nominee.name,
              category: item.name,
              department: nominee.department,
              vote: item.votes,
              img: nominee.img,
            });
            return true;
          });
        })
        .catch((error) => {
          console.log('no connection to server',error);
        });
    },
    Vote(nomID, name) {
      if (this.hasVoted) {
        Swal.fire("🤗", 'Can\'t vote twice buddy', "info");
        return 0;
      }
      if (this.user_id === null || this.role < 3) {
        swal(
          "Sorry",
          "You just need to login or You can't vote as an admin",
          "error"
        );
      } else {
        var vote = {
          name: name,
          nominee_id: nomID.toString(),
          category: this.cat_type
        };
        axios
          .post('api/vote', { ...vote }, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`,
            },})
          .then(res => {
            const result = res.data;
            if (result.id) {
              Swal.fire("👌👌", 'Vote Successful', "success");
            } else {
              Swal.fire("🙄", 'Oops,(xx)', "error");
            }
          })
          .catch((error) => {
            const errorInfo = error.response
            if(errorInfo.status === 401) {
              Swal.fire({
                title: `You need to be logged in to Vote`,
                icon: "error"
              });
            }
          });
      }
      this.checkVote()
    },
    checkVote() {
      axios.get(`/api/getuser/${this.user.id}`, {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('token')}`,
            },})
      .then((res)=>{
        let resArray = res.data[0].voted_for;
        this.hasVoted = Boolean(resArray.filter(x => x === this.cat_type).length);
      })
    }
  },
  created() {
    this.getTypes();
    this.checkVote();
    setInterval(()=> {this.checkVote()},1000)
  },
};
</script>

<style scoped>
.lead-img {
    height: 200px;
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
    grid-template-columns: repeat(auto-fit, minmax(250px,1fr));
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
    line-height: 27px; */
    font-size: 14px;
    display: block;
    color: #4D4D4D;
}
.lead-bottom {
    font-size: 1rem;
    padding: 1.25rem;
}
.wrap-login{
    /* justify-self: center; */
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    column-gap: 20px;
    row-gap: 20px;
    background: transparent;
    /* grid-template-columns:minmax(1fr 1fr) */
    padding: 50px;
}
.heart {
    /* background-color: var(--blueTheme); */
    padding: 2px;
    cursor: pointer;
    /* color: white; */
    font-size: 14px;
    border-radius: 8px;
    width: 70px;
}
.heart:hover {
    color: rgb(243, 97, 122);
}
nav {
    position: absolute;
    padding-left: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    display: flex;
    width: 100%;
    justify-content: space-around;
    box-shadow: 0px 4px 4px 2px rgba(0, 0, 0, 0.25);
}
ul li a {
    font-weight: bold;
    color: black;
}
@media only screen and (max-width:760px){
    .wrap-login{
        grid-template-columns: 1fr;
    }
}
</style>
