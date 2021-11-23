<template>
  <div id="app">
    <a-layout id="components-layout-demo-custom-trigger">
      <a-layout-sider v-model="collapsed" :trigger="null" collapsible>
        <div class="logo"></div>
        <a-menu theme="dark" mode="inline" :default-selected-keys="['1']">
          <a-menu-item key="1" @click="goto('/')">
            <a-icon type="dashboard" />
            <span>仪表盘</span>
          </a-menu-item>
          <a-menu-item key="2" @click="goto('/user')">
            <a-icon type="user" />
            <span>用户管理</span>
          </a-menu-item>
          <a-menu-item key="3" @click="goto('/article')">
            <a-icon type="book" />
            <span>文章管理</span>
          </a-menu-item>
          <a-menu-item key="4" @click="goto('/category')">
            <a-icon type="database" />
            <span>分类管理</span>
          </a-menu-item>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-layout-header style="background: #fff; padding: 0">
          <a-icon
            class="trigger"
            :type="collapsed ? 'menu-unfold' : 'menu-fold'"
            @click="() => (collapsed = !collapsed)"
          />
          <a-divider type="vertical" />
          <a-breadcrumb id="header">
            <a-breadcrumb-item>Admin</a-breadcrumb-item>
            <a-breadcrumb-item>{{ current }}</a-breadcrumb-item>
          </a-breadcrumb>
        </a-layout-header>
        <a-layout-content
          :style="{
            margin: '24px 16px',
            padding: '24px',
            background: '#fff',
            minHeight: '280px',
          }"
        >
          <router-view />
        </a-layout-content>
      </a-layout>
    </a-layout>
    <Footer />
  </div>
</template>

<script>
import Footer from '@/Footer'
export default {
  name: "Layout",
  components:{
      Footer
  },
  data() {
    return {
      collapsed: false,
      current: "",
    };
  },
  methods: {
    goto(param) {
      const temp = this.$router.history.current.fullPath;
      if (temp === param) return;
      this.$router.push(param);
      this.current = temp.substr(1);
    },
  },
};
</script>

<style lang='less' scoped >
#header {
  display: inline;
}
#components-layout-demo-custom-trigger {
  min-height: 75vh;
}
#components-layout-demo-custom-trigger .trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

#components-layout-demo-custom-trigger .trigger:hover {
  color: #1890ff;
}

#components-layout-demo-custom-trigger .logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px;
}
</style>
