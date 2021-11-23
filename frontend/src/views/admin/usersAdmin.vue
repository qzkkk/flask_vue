<template>
  <div id='page'>
    <a-card :bordered="false" title="用户管理">
      <div id='add'>
        <a-space>
            <a-input addonBefore="用户名：" v-model='obj.username' />
            <a-input-password addonBefore="密码：" v-model='obj.password' />
            <a-button @click='addUser'>添加用户</a-button>
        </a-space>
      </div>
        <a-table :columns="columns" :data-source="data" bordered rowKey='username' >
          <template slot='level' slot-scope="text">
              {{level[text]}}
          </template>
          <template slot="operation" slot-scope="text, record">
            <div class="editable-row-operations">
              <span ref='myedit'>
                <a @click="() => edit(record)">编辑</a>
              </span>
              <a-divider type="vertical" />
              <span>
                <a-popconfirm
                  title="确认删除该用户吗?"
                  ok-text="Yes"
                  cancel-text="No"
                  @confirm="del(record)"
              >
                  <a href="javascript:;">删除</a>
              </a-popconfirm>
              </span>
            </div>
          </template>
        </a-table>
        
        <a-popover id='popover'  v-model="visible" :title="'当前编辑用户：' + ( cache ? cache.username : '编辑')" trigger="click">
            <template slot='content'>
                <a-space>
                    <a-input addonBefore="用户名：" v-model='cache.username' />
                    <a-input addonBefore="密码：" v-model='cache.password' />
                    <a-select :default-value="cache? level[cache.level]: '普通用户'" style="width: 120px" @change="select">
                        <a-select-option value="0">
                            普通用户
                        </a-select-option>
                        <a-select-option value="1">
                            管理员
                        </a-select-option>
                    </a-select>
                    <a-button @click='save'>保存</a-button>
                    <a-button @click='$data.visible = false'>取消</a-button>
                </a-space>

            </template>
        </a-popover>
    </a-card>
  </div>
</template>

<script>
import columns from "./userColumn.js";
export default {
  name: "userAdmin",
  data() {
    return {
      api: null,
      columns,
      data: [],
      cache: {},
      visible: false,
      level:['普通用户','管理员'],
      obj: {
        username: null,
        password: null
      }
    };
  },
  mounted() {
    this.api = this.$api.User;
    this.get_list();
    window.onresize = ()=>{
      if(!this.$refs.edit) return ;
      if(this.visible) this.$refs.myedit.click()
    }
  },
  methods: {
    get_list() {
      this.api.get_list().then((r) => {
        this.data = r.data.users;
      });
    },
    edit(record) {
        // 深拷贝进行数据隔离
        this.cache = {...record};
        console.log('edit')
        const edit = this.$refs.myedit
        const pop = document.getElementById('popover')
        
        const e = edit.getBoundingClientRect()
        pop.style.width = '200px'
        pop.style.position = 'fixed'
        pop.style.left = (e.x - 100) + 'px'
        pop.style.top = e.y + 'px'        
        this.visible = true;
        

    },
    select(value){
        this.cache.level = Number(value)
    },
    save() {
        this.api.update(this.cache).then(r=>{
          if(r.status === 200){
            this.get_list()
            this.$message.success('更新成功')
            this.visible = false
          }
        }, ()=>{
          this.$message.error('更新失败')
        })
    },
    cancel() {
        console.log('cancel')
    },
    del(val) {
        this.api.del(val).then(r=>{
          if(r.status === 200){
            this.$message.success('删除成功')
            this.get_list()
          }
        },e=>{
          console.log(e)
        })
    },
    addUser(){
      const {obj, api} = this
      let {username, password} = obj
      if(!username) return this.$message.warning('请填写用户名')
      if(!password) return this.$message.warning('请填写密码')
      api.register(obj).then(r=>{
        if(r.data.flag ){
          this.get_list()
          return this.$message.success('添加成功')
        }
        this.$message.warning(r.data.msg)
      },()=>{
        this.$message.error('服务器发生错误')
      })
    }
  },
};
</script>

<style lang='less' scoped>


.editable-row-operations a {
  margin-right: 8px;
}
#add{
  margin-bottom: 20px;
}
</style>