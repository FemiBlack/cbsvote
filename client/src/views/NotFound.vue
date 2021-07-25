<template>
  <div class="limiter">
    <section class="login-container">
      <div class="side-overlay --sm">
        <img
          style="position: absolute;bottom: 0;animation-duration: 0s;"
          :src="require(`@/assets/images/Saly-17.svg`)"
          alt="floating_sally"
        >
      </div>

      <div class="wrap-login">
        <div class="container">
          <div>
            <h1>Not Found</h1>
            <p>
              Oops, We couldn't find that page.Try going
              <router-link :to="{ name: 'Home' }">
                Home
              </router-link>
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  title: 'CBS Vote - 404 Page Not Found',
};
</script>
