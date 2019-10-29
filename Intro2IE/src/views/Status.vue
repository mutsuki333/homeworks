<template lang="pug">
.container.p-y-1.p-x-1
  .box(v-if="items.length>0")
    .title.is-size-5.has-text-danger.has-text-left 
      | 缺貨中商品
    div(v-for="item in items" :key="item.id")
      Item(:id="item.id", 
          :name="item.name", 
          :stock="item.stock"
          :pic="item.picture"
          :hide="true")
  .box
    .title.is-size-5.has-text-info.has-text-left 
      | 交易紀錄
    table.table.is-striped.is-hoverable.is-bordered.is-fullwidth.is-narrow
      thead
        tr 
          th 品名
          th 增減
          th 日期
      tbody
        tr.has-text-weight-bold(v-for="record in records")
          th {{record.item_name}}
          td.has-text-success(v-if="record.alter>0") {{record.alter}}
          td.has-text-danger(v-else) {{record.alter}}
          td {{record.date}}

    

</template>


<script>
import Item from "../components/Item"
import axios from 'axios'

export default {
  components:{Item},
  data(){
    return{
      items:[],
      records:[]
    }
  },
  beforeCreate() {
    axios('/get_items?stock_level='+0)
    .then(res=>{
      this.items = res.data
    })
    axios('/records')
    .then(res=>{
      this.records = res.data
      for (const i of this.records) {
        i.date = new Date(i.date).toLocaleString()
      }
    })
  },
}
</script>