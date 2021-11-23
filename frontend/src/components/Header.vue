<template>
  <div id="header">
    <a-row>
      <a-col :xs="6" :md="3" :lg="6">
        <div id="logo">
          <img src="../img/logo.jpg" @click="goto('/Index')" title="树洞" />
        </div>
      </a-col>
      <a-col :xs="14" :md="18" :lg="12" id="content">
        <a-menu v-model="current" mode="horizontal">
          <a-menu-item key="index" @click="goto('/Index')">
            <a-icon type="home" />首页</a-menu-item
          >
          <a-menu-item key="article" @click="goto('/Article')">
            <a-icon type="unordered-list" /> 全部文章
          </a-menu-item>
          <!-- <a-menu-item key="category" @click="goto('/Category')">
            <a-icon type="folder" /> 分类
          </a-menu-item> -->
          <!-- <a-menu-item key="tags" @click="goto('/Tags')">
            <a-icon type="tags" /> 归档
          </a-menu-item> -->
          <a-menu-item key="update" @click="goto('/Update')">
            <a-icon type="redo" /> 更新历程
          </a-menu-item>
          <a-menu-item key="user" @click="goto('/Mine')">
            <a-icon type="user" /> 关于我
          </a-menu-item>
          <a-menu-item key="edit" @click="GoToWrite">
            <a-icon type="edit" /> 写博客
          </a-menu-item>
        </a-menu>
      </a-col>
      <a-col :xs="4" :md="3" :lg="6">
        <div class="btn">
          <!-- 已登录 -->
          <div id="user" v-if="$store.state.isLogin">
            <a-dropdown>
              <a-avatar size="large" icon="user" />
              <a-menu slot="overlay">
                <a-menu-item>
                  <p>您好,{{$store.state.username}}</p>
                </a-menu-item>
                <a-menu-item  @click="goto('/User')">
                  <a href="javascript:;">个人中心</a>
                </a-menu-item>
                <a-menu-item>
                  <a href="javascript:;" @click="$store.dispatch('logout')"
                    >退出登录</a
                  >
                </a-menu-item>
              </a-menu>
            </a-dropdown>
          </div>
          <a-space v-else>
            <a-button @click="goto('/Login')">登录</a-button>
            <a-button @click="goto('/Register')">注册</a-button>
          </a-space>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      current: [],
    };
  },
  methods: {
    goto(param) {
      if (this.$router.history.current.fullPath === param) return;
      this.$router.push(param);
    },
    GoToWrite(){
      this.$message.info('正在前往后台管理')
      setTimeout(()=>{
        const a = document.createElement('a')
        a.href='./admin.html#/login'
        a.target = '_blank'
        a.click()
      },1000)
    }
  },
  watch: {
    $route(val){
      this.current = [val.fullPath.slice(1).toLowerCase()]
      console.log(this.current)
    }
  },
};
</script>

<style lang='less' scoped>
#header {
  border-bottom: 1px dotted #ccc;
}
#logo {
  img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-left: 30%;

    &:hover {
      -webkit-animation: logo 2s linear infinite;
      animation: logo 2s linear infinite;
    }
  }
}
#content {
  .ant-menu-horizontal {
    border-bottom: none;
  }

  li {
    &:hover {
      border-bottom: 1px;
    }
  }
}
.btn {
  line-height: 51px;
}

@keyframes logo {
  0% {
    transform: rotatey(0deg);
  }
  100% {
    transform: rotatey(360deg);
  }
}
</style>