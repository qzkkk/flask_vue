<template>
<div id="page">
  <a-button @click='get'>获取dcs分类</a-button>
  <a-button @click='send'>添加分类</a-button>
  <a-button @click='change'>修改名字</a-button>
  <a-button @click='del'>删除</a-button>
</div>

</template>
<script>
export default {
  data() {
    return {
      
    };
  },
  methods:{
    get(){
      this.$api.Categories.getCategories().then(r=>{
        console.log("获取到的分类",r)
      })
    },
    send(){
      this.$api.Categories.addCategory({
        category: {
          title: '测试3',
          description: "测试描述"
          }
      })
    },
    change(){
      this.$api.Categories.change({
        id:'60fbfd7e9bcfd02b1c314603',
        title:"新名字"
      }).then(r=>{
        console.log("修改结果\r\n", r)
      })
    },
    del(){
      this.$api.Categories.del({id:'60fbfce0e26d7206481422ff'}).thne(r=>{
        console.log("删除结果", r);
      })
    }
  }
};
</script>
<style lang='less' scoped>
#page{
  padding: 30px;
}
</style>