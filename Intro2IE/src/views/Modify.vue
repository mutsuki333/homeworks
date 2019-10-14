<template lang="pug">
.container.p-x-1.has-text-left
  .field
    label.label 品名
    .control
      input.input(type='text', placeholder='e.g DUALSHOCK4', v-model="name")
  .field
    label.label 備註
    .control
      input.input(type='text', placeholder='e.g. ps4專用', v-model="description")
  .field
    label.label 庫存量
    .control
      input.input(type='number',v-model="stock")
  .file.has-name
    label.file-label
      input.file-input(type='file', name='resume', ref="pic")
      span.file-cta
        span.file-icon
          i.fas.fa-upload
        span.file-label
          | 上傳照片
      span.file-name(v-if="file_name")
        | {{file_name}}

  .level.p-t-4.is-mobile(v-if="id")
    .level-left
      button.button.is-danger(@click="del") 刪除
    .level-right
      button.button.is-primary(@click="clear") 取消
      button.button.is-info.m-l-1(@click="send") 確定

  .level.p-t-4.is-mobile(v-else)
    .level-left
      button.button.is-primary(@click="clear") 取消
    .level-right
      button.button.is-info(@click="send") 確定

</template>

<script>
import axios from 'axios'
export default {
  props:['id'],
  data() {
    return {
      name:"",
      description:"",
      stock:0,
      file_name:""
    }
  },
  watch: {
    id(){
      this.clear()
    }
  },
  mounted(){
    this.$refs.pic.onchange = ()=>{
      if(this.$refs.pic.files.length > 0){
        this.file_name = this.$refs.pic.files[0].name;
      }
    }
    
    if(this.id != undefined){
      axios(`/get_item?id=${this.id}`)
      .then(res=>{
        this.name = res.data[0].name
        this.description=res.data[0].description
        this.stock=res.data[0].stock
        this.file_name=res.data[0].picture
      })
    }
    else this.clear()
  },
  methods: {
    clear(){
      this.name=""
      this.description=""
      this.stock=0
      this.file_name=""
    },
    del(){
      axios(`/del_item?id=${this.id}`)
      .then(res=>{
        this.$router.push('/stock')
      })
    },
    send(){
      if(this.name==""){
        alert("請填入品名")
        return
      }
      let payload = {
        name:this.name,
        description:this.description,
        stock:this.stock
      }
      axios.post('/new_item',payload)
      .then(res=>{
        if(res.status == 404)alert('錯誤')
        else{
          if(this.file_name==""){
            alert("成功")
            this.$router.push('/stock')
            return
          }
          let formData = new FormData();
          formData.append('file', this.$refs.pic.files[0])
          axios.post(`/set_pic?id=${res.data}`,formData,{
            headers:{
              'Content-Type': 'multipart/form-data'
            }
          })
          .then(response=>{
            if(response.status == 200){
              this.$router.push('/stock')
            }
          })
        }
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