<template>
  <div>
    <div class="add-nominee">
      <h1>Nominee Form</h1>
      <!-- <input
        type="text"
        v-model="reg_no"
        required="required"
        minlength="6"
        maxlength="7"
        class="nom-regno"
        placeholder="enter nominee regno"
      /><br /> -->
      <input
        type="text"
        v-model="name"
        required
        autofocus
        minlength="4"
        maxlength="65"
        class="nom-name"
        placeholder="enter nominee name"
      /><br />
      <select name="department" v-model="department" id="department">
        <option value="">Choose Department</option>
        <option value="interel">International Relations</option>
        <option value="accounting">Accounting</option>
        <option value="bfn">Banking and Finance</option>
        <option value="busadmin">Business Admin</option>
        <option value="eco">Economics</option>
        <option value="masscom">Mass Communication</option>
        <option value="sos">SOS</option></select
      ><br />
      <select name="categories" v-model="category" id="categories">
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
      ><br />
      <uploadcare publicKey="d0c1fab0b4eecafd5f0f" @success="onSuccess" @error="onError">
        <button>Pick an Image</button>
      </uploadcare>
      <!-- <a @click="personImage" class="btn btn-primary btn-send-message" :disabled="disabled">
        Pick an Image
      </a> -->
      <span id="imageSelected" v-html="imagePreview"></span>
      <button @click="Nominate" class="btn btn-primary btn-send-message" v-html="nominate"></button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert2';
import Uploadcare from 'uploadcare-vue';

export default {
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
    onSuccess(event) {
      console.log('Success: ', event);
    },
    onError(event) {
      console.log('Error: ', event);
      Swal.fire('Oops', 'There has been an error, try again later', 'warning');
    },
    Nominate(e) {
      e.preventDefault();
      let add;
      const { name } = this.name;
      const { category } = this.category;
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
            person: name,
            category,
            personImage: this.imageSelected,
          };
          this.disabled = true;
          this.nominate = 'Nominating...';
          axios
            .post('/add', { ...add })
            .then((res) => {
              this.disabled = false;
              this.nominate = 'Nominate';
              const result = res.data;
              if (result.success) {
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
