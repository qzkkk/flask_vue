<template>
  <div>
    <a-card :bordered="false" title="服务器信息">
      <a-row>
        <a-col id='progress' :span="10">
            <h3>开发进度条</h3>
            <br />
            <a-progress
              :stroke-color="{
                '0%': '#108ee9',
                '100%': '#87d068',
              }"
              :percent="99.9"
            />
        </a-col>
        <a-col :span='4'></a-col>
        <a-col :span="10">
          <div ref="pie" id="pie"></div>
        </a-col>
      </a-row>
    </a-card>
  </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-liquidfill";
export default {
  name: "Admin",
  data() {
    return {
      $echarts1: null,
      option: null,
      value: 0.45,
    };
  },
  mounted() {
    this.init();
    window.onresize = ()=>{
      this.$router.go(0)
    }
  },
  methods: {
    init() {
      console.log(this.$refs.pie);
      this.$echarts1 = echarts.init(this.$refs.pie);
      this.update();
    },
    update() {
      this.option = {
        title: {
          text: (0.3 * 100).toFixed(0) + "{a|%}",
          textStyle: {
            fontSize: 50,
            fontFamily: "Microsoft Yahei",
            fontWeight: "normal",
            color: "#bcb8fb",
            rich: {
              a: {
                fontSize: 28,
              },
            },
          },
          x: "center",
          y: "35%",
        },
        graphic: [
          {
            type: "group",
            left: "center",
            top: "60%",
            children: [
              {
                type: "text",
                z: 100,
                left: "10",
                top: "middle",
                style: {
                  fill: "#aab2fa",
                  text: "服务器内存",
                  font: "20px Microsoft YaHei",
                },
              },
            ],
          },
        ],
        series: [
          {
            type: "liquidFill",
            radius: "80%",
            center: ["50%", "50%"],
            data: [0.3, 0.2],
            color: ["rgba(68, 145, 253, .25)", "rgba(68, 145, 253, 1)"],
            outline: {
              borderDistance: 0,
              itemStyle: {
                borderWidth: 20,
                borderColor: {
                  type: "linear",
                  x: 0,
                  y: 0,
                  x2: 0,
                  y2: 1,
                  colorStops: [
                    {
                      offset: 0,
                      color: "rgba(69, 73, 240, 0)",
                    },
                    {
                      offset: 0.5,
                      color: "rgba(69, 73, 240, .25)",
                    },
                    {
                      offset: 1,
                      color: "rgba(69, 73, 240, 1)",
                    },
                  ],
                  globalCoord: false,
                },
                shadowBlur: 10,
                shadowColor: "#000",
              },
            },

            label: {
              normal: {
                formatter: "",
              },
            },
          },
        ],
      };
      this.paint();
    },
    paint() {
      this.$echarts1.setOption(this.option);
    },
  },
};
</script>

<style scoped lang='less'>
#pie {
  width: 50%;
  height: 350px;
}
/deep/ #progress{
  line-height: 45px;
}

</style>