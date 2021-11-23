<template>
  <div id='update'>
    <a-timeline mode="alternate">
      <a-timeline-item>2021-7-14 开始架构博客网站</a-timeline-item>
      <a-timeline-item color="green">
        2021-7-21 完成登录注册，以及markdown编译器模块
      </a-timeline-item>
      <a-timeline-item color="green">
        2021-7-22 更改md文件的渲染方式，由转换成html变为直接渲染md
      </a-timeline-item>
      <a-timeline-item>
        <a-icon slot="dot" type="clock-circle-o" style="font-size: 16px" />
        2021-7-23：完成分类并修复头部当前路由对active的影响
      </a-timeline-item>
      <a-timeline-item color='blue'>
        2021-7-24： 先给自己放个小假
      </a-timeline-item>
      <a-timeline-item>
        <a-icon slot="dot" type="clock-circle-o" style="font-size: 16px" />
          2050-1-1 最理想的生活
      </a-timeline-item>
    </a-timeline>
  </div>
</template>


<script>
export default {
  name: "Update",
};
</script>

<style lang='less' scoped>
#update{
  padding:50px;
  min-height: 80vh;
}
</style>