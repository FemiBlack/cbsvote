<template>
  <div class="category">
    <section>
      <h3>CATEGORIES</h3>

      <div class="cat_type" v-for="(el, i) in catTypes" :key="i">
        <div class="card">
          <p>{{ el }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
const catTypes = ['Freshman of the Year', 'Final Year Fresh'];

export default {
  name: 'Category',
  data() {
    return {
      catTypes,
    };
  },
};
</script>
