<template>
  <div id="app">
    <Header />
      <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from '@/Header'
import Footer from '@/Footer'
export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style lang='less' >
#app{
  max-width: 1350px;
  margin: 0 auto;
}
</style>
