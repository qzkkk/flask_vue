<template>
  <div id="footer">
    <a-button @click="backTop">回到顶部</a-button>
    <p>
      <a-icon type="copyright" />
      2021-2050 程序猿 CSJerry <br />
      <a-icon type="link" />dcs 版权所有
    </p>
    <p>本博客已启动 {{ day }} 天</p>
    <p>粤ICP备2021082063号</p>
    <div ref="wave" id="wave"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-liquidfill";
export default {
  name: "Footer",
  data() {
    return {
      day: 0,
      $echarts2: null
    };
  },
  created() {
    this.$api.Utils.getDate().then((r) => {
      this.day = r.data.day;
    });
  },
  mounted(){
    window.onresize = ()=>{
      this.$router.go(0)
    }
    this.draw()
  },
  methods: {
    backTop() {
      document.body.scrollTop = document.documentElement.scrollTop = 0;
    },
    draw(){
      this.$echarts2 = echarts.init(this.$refs.wave);
      const option = {
        series:[{
          // 声明是水波图
          type:'liquidFill',
          // 水波数量以及占比
          data: [0.7,{
            value:0.8,
            direction:'left',
            itemStyle:{
              color:'rgba(100,123,231,0.3)'
            }
          },0.5],
          // 水波颜色
          color:['#409EFF', 'rgba(135,206,250,0.6)'],
          shape: 'container',
          label:{
            show:false
          },
          outline: {
            show: false
          }
        }]
      }
      this.$echarts2.setOption(option);
    }
  },
};
</script>

<style lang='less' scoped>
#wave{
  position: absolute;
  left:0;
  width: 99vw;
  height: 100px;
}
#footer {
  padding: 20px;
  text-align: center;
}
</style>