<template lang="pug">
.container
  .p-1
    p.control.has-icons-left
      input.input(type='text', placeholder='搜尋', v-model="search_text")
      span.icon.is-left
        i.fas.fa-search(aria-hidden='true')
  div(v-for="item in items" :key="item.id")
    Item(:id="item.id", 
          :name="item.name", 
          :description="item.description", 
          :stock="item.stock"
          :pic="item.picture")
</template>

<script>
import Item from "../components/Item"
import axios from 'axios'

export default {
  components:{Item},
  data(){
    return{
      items:[],
      search_text:"",
      no_item:true
    }
  },
  beforeCreate() {
    axios('/get_items')
    .then(res=>{
      this.items = res.data
    })
  },
  watch: {
    search_text(value){
      axios('/get_items?query='+value)
      .then(res=>{
        this.items = res.data
      })
    }
  },
}
</script>

<style lang="sass">
@media (min-width:768px)
  .container
    width:40%
</style>