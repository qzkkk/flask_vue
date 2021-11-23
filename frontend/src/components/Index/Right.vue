<template>
  <div class='right'>
     <a-card class= 'item' id='my' title='所有者'>
        <template slot="actions" class="ant-card-actions">
          <p @click='goto("https://github.com/csDeng")'><a-icon key="github" type="github" title='github' />Github</p>
          <p @click='goto("https://blog.csdn.net/qq_45704048?type=blog")'><a-icon key="CSDN" type="deployment-unit" title='CSDN' />CSDN博客</p>
          <p @click='girl'><a-icon key="ellipsis" type="ellipsis" title='更多信息请期待' />我的女孩</p>
      </template>
    <a-card-meta title="CSJerry" description="呆在优秀的圈子里成为优秀的人">
      <a-avatar
        slot="avatar"
        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
      />
    </a-card-meta>
     </a-card>
    <a-card class= 'item'>
      <div :style="{ width: '100%', border: 'none', borderRadius: '4px' }">
        <a-calendar :fullscreen="false"  />
      </div>
    </a-card>
     <a-card class= 'item' id='comment' title="最新留言">
      开发中
     </a-card>
  </div>
</template>

<script>
export default {
name:'Right',
methods: {
  goto(val){
    console.log('goto')
    window.location.href = val
  },
  girl(){
    this.$message.warning("你没有权限查看哦")
  }
}
}
</script>

<style lang='less' scoped>
.right{
  padding: 30px;
  max-width: 385px;
  float: left;

}
.item{
  margin-bottom:50px;
  border-radius: 8px;
  box-shadow: 0 0 10px #ccc;
}

</style>