<template>
  <div>
    <div class="admin-login">
      <h1>Admin Login</h1>
      <input type="text" placeholder="username" /><br />
      <input type="password" placeholder="password" /><br />
      <input type="submit" value="Submit" />
    </div>
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
        <option value="face">Face of CBS</option>
        <option value="sociable">Most Sociable</option>
        <option value="nextgen">CBS Next Gen</option>
        <option value="entrepreneur">Entrepreneur</option>
        <option value="fashionable">Most Fashionable</option>
        <option value="sportsperson">Sportsperson</option>
        <option value="innovative">Most Innovative</option></select
      ><br />
      <a
        @click="personImage"
        class="btn btn-primary btn-send-message"
        :disabled="disabled"
      >
        Pick an Image
      </a>
      <span id="imageSelected"></span>
      <button
        @click="Nominate"
        class="btn btn-primary btn-send-message"
        v-html="nominate"
      ></button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      // reg_no: "",
      department: "",
      category: "",
      disabled: false,
      nominate: "Nominate",
      imageSelected: null,
    };
  },
  methods: {
    personImage(event) {
      event.preventDefault();
      uploadcare
        .openDialog(null, {
          previewStep: true,
          imagesOnly: true,
          imageShrink: "1024x1024",
        })
        .done(function (file) {
          file.promise().done(function (fileInfo) {
            var img = fileInfo.cdnUrl;
            localStorage.setItem("personImage", img);
            $(() => {
              $("#imageSelected").html(`<img src="${img}" width="50" />`);
            });
          });
        });
    },
    Nominate(e) {
      e.preventDefault();
      let name = this.name,
        // reg_no = this.reg_no,
        category = this.category,
        re = /[0-9]/;
      if (name === "" || category === "") {
        Swal.fire("Warning", "You need to finish before submitting", "warning");
      } else if (name < 3) {
        Swal.fire("Oops", "Name too short to proceed", "error");
      } else {
        this.imageSelected = localStorage.getItem("personImage");
        if (this.imageSelected == null) {
          Swal.fire("Hey", "Please upload an image for " + name, "warning");
        } else {
          var add = {
            person: name,
            category: category,
            personImage: this.imageSelected,
          };
          this.disabled = true;
          this.nominate = "Nominating...";
          axios
            .post(`/add`, { ...add })
            .then((res) => {
              this.disabled = false;
              this.nominate = "Nominate";
              result = res.data;
              if (result.success) {
                Swal.fire("👌👌", `${result.success.success_text}`, "success");
                this.name = "";
                this.category = "";
                this.imageSelected = null;
                localStorage.removeItem("personImage");
                $(() => {
                  $("#imageSelected").html("");
                });
              } else {
                this.disabled = false;
                this.nominate = "Nominate";
                Swal.fire({
                  title: `Coudn't nominate ${name}`,
                  icon: "error",
                });
              }
            })
            .catch(() => {
              this.disabled = false;
              this.nominate = "Nominate";
              Swal.fire({
                title: `No connection to server`,
                icon: "error",
              });
            });
        }
      }
    },
  },
};
</script>