<template lang="pug">
article.media.p-t-3.p-x-1.is-boxed
  figure.media-left
    p.image.is-64x64
      img(v-if="pic" :src="url+'/'+pic")
  .media-content
    .content(@click="click")
      p
        strong {{name}}
        br
        | {{description}}
    nav.level.is-mobile
      .level-left
        p 庫存量： {{stock_}}
        //- button.button.is-primary 增加
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
      url:'http://127.0.0.1:8000/media'
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