<template lang="pug">
  #app
    h1.title.has-text-info.p-t-2 即時存貨管理系統
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
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
