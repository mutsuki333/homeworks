<template lang="pug">
article.media.p-b-2.p-x-1.is-boxed
  figure.media-left(@click="toggle")
    p.image.is-64x64
      img(v-if="pic" :src="url+'/'+pic")
  .media-content
    nav.is-mobile
      .content
        p.wrap
          strong {{name}}
          br
          | {{description}}
    .level.is-mobile
      .level-left 
      .level-right
        button.button.is-rounded.is-small.is-success(@click="click" v-if="!hide")
          | 修改
    nav.level.is-mobile
      .level-left
        p(v-if="stock_>0") 庫存量： {{stock_}}
        p(v-else).has-text-danger.has-text-weight-bold 庫存量： {{stock_}}
      .level-right
        button.button.is-primary.is-small.m-r-1(@click="inc") 增加
        button.button.is-danger.is-small(@click="dec" v-if="!hide") 減少
  .modal.is-clipped(v-bind:class="{ 'is-active': active}")
    .modal-background
    .modal-content
      p.image
        img(:src="url+'/'+pic", alt='')
    button.modal-close.is-large(aria-label='close' @click="toggle")
</template>

<script>
import axios from 'axios'
export default {
  props:['id','name','description','pic','stock','hide'],
  data() {
    return {
      stock_:this.stock,
      url:axios.defaults.baseURL.replace('/api','/media'),
      active:false
    }
  },
  methods: {
    click(){
      this.$router.push(`/alter/${this.id}`)
    },
    toggle(){
      this.active = !this.active
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
