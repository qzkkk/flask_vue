<template>
  <div id='detail'>
    <a-card >  
        <div id='title'>
            <h1>{{ article.title }}</h1>
            <a-button @click='$emit("show")'>
                返回
            </a-button>
        </div>
        <div  class='context'>
            <vue-markdown class='markdown-body'>{{article.body}}</vue-markdown>
        </div>
    </a-card>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown';

export default {
name:'ArticleDetail',
components:{
    VueMarkdown
},
props:{
    article:{
        type: Object,
        required: true
    }
}
}
</script>

<style lang='less' scoped>
#detail{
    max-width: 985px;
    margin: 0 auto;
}
#title{
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ccc;
}
.context{
    min-height: 600px;
    // /deep/ img{
    //     width: 100%;
    // }
    // /deep/ pre{
    //     background: #000;
    // }
    // /deep/ code{
    //     color:rgba(154,220,254, 0.8);
    // }

}

</style>