<template>
  <div>
    <div class="add-nominee">
      <!-- <input
        type="text"
        v-model="reg_no"
        required="required"
        minlength="6"
        maxlength="7"
        class="nom-regno"
        placeholder="enter nominee regno"
      /><br /> -->
        <!-- </div> -->
        <div class="wrap-login">
    <p style="cursor:pointer;" @click="goBack">back to previous page</p>
      <h1>Nominee Form</h1>

        <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
          <i class="feather-user icon" />
      <input
        type="text"
        v-model="name"
        class="input100"
        required
        autofocus
        minlength="4"
        maxlength="65"
        placeholder="Enter nominee name"
      />
        </div>
        <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
          <i class="feather-globe icon" />
      <select name="department" v-model="department" id="department" class="input100">
        <option value="">Choose Department</option>
        <option value="interel">International Relations</option>
        <option value="accounting">Accounting</option>
        <option value="bfn">Banking and Finance</option>
        <option value="busadmin">Business Admin</option>
        <option value="eco">Economics</option>
        <option value="masscom">Mass Communication</option>
        <option value="soc">Sociology</option></select
      >
        </div>
        <div class="wrap-input100 validate-input animate__animated animate__bounceInDown">
          <i class="feather-layers icon" />
      <select name="categories" v-model="category" id="categories" class="input100">
        <option value="">Choose Category</option>
        <option value="facemale">Face of CBS(male)</option>
        <option value="facefemale">Face of CBS(female)</option>
        <option value="sociablemale">Most Sociable(male)</option>
        <option value="sociablefemale">Most Sociable(female)</option>
        <option value="nextgenmale">CBS Next Gen(male)</option>
        <option value="nextgenfemale">CBS Next Gen(female)</option>
        <option value="entrepreneurmale">Entrepreneur(male)</option>
        <option value="entrepreneurfemale">Entrepreneur(female)</option>
        <option value="fashionablemale">Most Fashionable(male)</option>
        <option value="fashionablefemale">Most Fashionable(female)</option>
        <option value="sportspersonmale">Sportsperson(male)</option>
        <option value="sportspersonfemale">Sportsperson(female)</option>
        <option value="innovativemale">Most Innovative(male)</option>
        <option value="innovativefemale">Most Innovative(female)</option></select
      >
        </div>
      <uploadcare publicKey="d0c1fab0b4eecafd5f0f" @success="onSuccess" @error="onError">
        <button class="input100">Pick an Image</button>
      </uploadcare>
      <!-- <a @click="personImage" class="btn btn-primary btn-send-message" :disabled="disabled">
        Pick an Image
      </a> -->
      <span id="imageSelected" v-html="imagePreview"></span>
      <div
          class="container-login100-form-btn
          animate__animated animate__bounceInUp animate__delay-1s"
        >
      <button @click="Nominate" class="login100-form-btn" v-html="nominate"></button>
      </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import Uploadcare from 'uploadcare-vue';

export default {
  title: 'CBS Vote - Admin Page',
  data() {
    return {
      name: '',
      department: '',
      category: '',
      disabled: false,
      nominate: 'Nominate',
      imageSelected: null,
      imagePreview: '',
    };
  },
  components: {
    Uploadcare,
  },
  methods: {
    goBack() {
      window.history.length > 1 ? this.$router.go(-1) : this.$router.push("/");
    },
    onSuccess(event) {
      console.log('Success: ', event);
      let img = event.cdnUrl;
      localStorage.setItem('personImage', img);
      this.imagePreview = `<img src="${img}" width="50" >`;
    },
    onError(event) {
      console.log('Error: ', event);
      Swal.fire('Oops', 'There has been an error, try again later', 'warning');
    },
    Nominate(e) {
      e.preventDefault();
      let add;
      const name = this.name;
      const category = this.category;
      if (name === '' || category === '') {
        Swal.fire('Warning', 'You need to finish before submitting', 'warning');
      } else if (name < 3) {
        Swal.fire('Oops', 'Name too short to proceed', 'error');
      } else {
        this.imageSelected = localStorage.getItem('personImage');
        if (this.imageSelected == null) {
          Swal.fire('Hey', `Please upload an image for ${name}`, 'warning');
        } else {
          add = {
            name: name,
            category: [{name: this.category, votes: 0}],
            department: this.department,
            img: this.imageSelected,
          };
          this.disabled = true;
          this.nominate = 'Nominating...';
          axios
            .post('/api/addnominee', { ...add }, {
              headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`,
              },})
            .then((res) => {
              this.disabled = false;
              this.nominate = 'Nominate';
              const result = res.data;
              if (result.id) {
                Swal.fire('👌👌', `${result.success.success_text}`, 'success');
                this.name = '';
                this.category = '';
                this.imageSelected = null;
                localStorage.removeItem('personImage');
                this.imagePreview = '';
              } else {
                this.disabled = false;
                this.nominate = 'Nominate';
                Swal.fire({
                  title: `Coudn't nominate ${name}`,
                  icon: 'error',
                });
              }
            })
            .catch(() => {
              this.disabled = false;
              this.nominate = 'Nominate';
              Swal.fire({
                title: 'No connection to server',
                icon: 'error',
              });
            });
        }
      }
    },
  },
};
</script>
<style scoped>
select {
  border: 1px solid var(--blueTheme);
  border-radius: 8px;
}
</style>