<template>
<div id="page">
  <a-list :grid="{ gutter: 16, column: 4 }" :data-source="data">
    <a-list-item slot="renderItem" slot-scope="item">
      <a-card :title="item.title">
          <a slot="extra" href="javascript:;" @click="showList(item.title)"
            >查看分类文章</a
          >
        {{ item.description }}
      </a-card>
    </a-list-item>
  </a-list>
</div>

</template>
<script>
export default {
  name:'Categories',
  data() {
    return {
      data: [],
    };
  },
  mounted(){
    this.get()
  },
  methods: {
    get(){
      this.$api.Categories.getCategories().then(r=>{
        this.$data.data = r.data.categories[0].categories
      })
    },
    showList(title){
      console.log(title)
    }
  }
};
</script>
<style lang='less' scoped>
#page{
  padding: 30px;
  min-height: 80vh;
}
</style>