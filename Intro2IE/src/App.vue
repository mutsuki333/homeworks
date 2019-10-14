<template lang="pug">
  #app
    #nav.is-size-4
      router-link(to="/") 首頁
      |  | 
      router-link(to="/stock") 庫存瀏覽
      |  | 
      router-link(to="/modify") 新增商品
    router-view

</template>

<script>
import "babel-polyfill"
import "src/theme.sass"

</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
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
