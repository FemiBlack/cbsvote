<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">Categories</router-link> |
    <router-link to="/about">Register</router-link> |
    <router-link to="/about">Login</router-link>
  </div>
</template>

<style lang="scss">
#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
