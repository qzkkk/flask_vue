<template>
  <div id='show'>
    <div v-if="show">
      <div v-for="article in articles" :key="article._id">
        <a-card :title="article.title">
          <a slot="extra" href="javascript:;" @click="showDetail(article)"
            >查看全部内容</a
          >
          <div class='tips'>
            <div class="time">
              创建时间：{{ article.date.slice(0,10)}}
            </div>
            <div class="categories">
              类别：
              <a-tag v-for="t in article.categories" :key="t">{{t}}</a-tag>
            </div>
            <div class="tags">
              标签：
               <a-tag v-for="t in article.tags" :key="t">{{t}} </a-tag>
            </div>
          </div>
          <div class="context">
            <vue-markdown class='markdown-body'>{{article.body}}</vue-markdown>
          </div>
        </a-card>
        <div class="kong"></div>
      </div>
    </div>
    <div v-else>
        <Detail :article='currentArticle' @show="$data.show = true; $data.currentArticle = null " />
    </div>
  </div>
</template>

<script>
// const md = require("markdown-it")().use(require("markdown-it-mark"));
import Detail from "@/articleDetail";
import VueMarkdown from 'vue-markdown'
export default {
  name: "Show",
  components: {
    Detail,
    VueMarkdown
  },
  data() {
    return {
      articles: [],
      show: true,
      currentArticle:null
    };
  },
  async mounted() {
    console.log("show");
    await this.$api.Article.get_list().then((r) => {
      this.articles = r.data.articles;
    });
  },
  methods: {
    showDetail(article){
        this.currentArticle = article 
        this.show = false
    }
  },
};
</script>

<style lang='less' scoped>
#show{
  max-width: 600px;
}
.kong {
  height: 20px;
}
.context {
  height: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
}
.tips{
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #ccc;
  padding-bottom: 20px;
}
</style>