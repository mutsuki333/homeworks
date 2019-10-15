<template lang="pug">
article.media.p-t-3.p-x-1.is-boxed
  figure.media-left
    p.image.is-64x64
      img(v-if="pic" :src="url+'/'+pic")
  .media-content
    nav.level.is-mobile
      .level-left
        .content
          p
            strong {{name}}
            br
            | {{description}}
      .level-right
        button.button.is-rounded.is-small.is-success(@click="click")
          | 修改
    nav.level.is-mobile
      .level-left
        p 庫存量： {{stock_}}
      .level-right
        button.button.is-primary.is-small.m-r-1(@click="inc") 增加
        button.button.is-danger.is-small(@click="dec") 減少

</template>

<script>
import axios from 'axios'
export default {
  props:['id','name','description','pic','stock'],
  data() {
    return {
      stock_:this.stock,
      url:axios.defaults.baseURL.replace('/api','/media')
    }
  },
  methods: {
    click(){
      this.$router.push(`/alter/${this.id}`)
    },
    inc(){
      axios(`/inc?id=${this.id}`)
      .then(res=>{
        if(res.data=="ok"){
          this.stock_+=1
        }else{
          alert("失敗")
        }
      })
    },
    dec(){
      if(this.stock_<=0){
        alert('已經沒有庫存')
      }
      else{
        axios(`/dec?id=${this.id}`)
        .then(res=>{
          if(res.data=="ok"){
            this.stock_-=1
          }else{
            alert("失敗")
          }
        })
      }
    }
  },
}
</script>