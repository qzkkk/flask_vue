<template>
  <div id='page'>
    <a-row>
      <a-col :span='2'></a-col>
      <a-col :span='20'>
            <article-list />
      </a-col>
      <a-col :span='2'></a-col>
    </a-row>
  </div>
</template>

<script>
import ArticleList from '@/Articles/ArticleList'
export default {
name:'Article',
components:{
  ArticleList
}
}
</script>

<style lang='less' scoped>
#page{
  min-height: 80vh;
}
</style>