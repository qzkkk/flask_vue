<template>
  <div>
    <a-row>
      <a-col :md='4' :xs='0'></a-col>
      <a-col :md='15'>
        <a-card title="登录" id="main">
          <a-form
            id="login"
            :form="form"
            class="login-form"
            @submit="handleSubmit"
          >
            <a-form-item label="用户名" labelAlign="left" required hasFeedback>
              <a-input
                v-decorator="[
                  'userName',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please input your username!',
                      },
                    ],
                  },
                ]"
                placeholder="Username"
              >
                <a-icon
                  slot="prefix"
                  type="user"
                  style="color: rgba(0, 0, 0, 0.25)"
                />
              </a-input>
            </a-form-item>
            <a-form-item label="密码" labelAlign="left" required hasFeedback>
              <a-input
                v-decorator="[
                  'password',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please input your Password!',
                      },
                    ],
                  },
                ]"
                type="password"
                placeholder="Password"
              >
                <a-icon
                  slot="prefix"
                  type="lock"
                  style="color: rgba(0, 0, 0, 0.25)"
                />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-checkbox
                v-decorator="[
                  'remember',
                  {
                    valuePropName: 'checked',
                    initialValue: true,
                  },
                ]"
              >
                Remember me
              </a-checkbox>
              <br />
              <a-button type="primary" html-type="submit"> 登录 </a-button>
              Or
              <a href="javascript:;" @click="$router.push('/Register')">
                注册
              </a>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>

export default {
  name: "Login",
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "normal_login" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields( async (err, values) => {
        if (!err) {
          const { userName: username, password } = values
          let res = await this.$api.User.login({
            username,
            password
          })
          const { data: {msg, flag} } = res
          console.log("登录结果res",res)
          if( flag === true ){
            this.$message.success("登录成功").then(()=>{
              this.$store.dispatch("login", res.data ).then(() => {
                this.$router.push("/Index");
              });
            })
          }else{
            this.$message.error(msg)
          }
          }
      });
    },
  },
};
</script>
<style lang='less'>
.main{
  max-width: 500px;
}
</style>