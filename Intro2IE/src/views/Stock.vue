<template lang="pug">
  div
    //- h1 stock
    div(v-for="item in items" :key="item.id")
      //- p {{item.name}}
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
      items:[]
    }
  },
  beforeCreate() {
    axios('/get_items')
    .then(res=>{
      this.items = res.data
    })
  },
}
</script>