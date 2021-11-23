<template>
  <div>
    <a-row>
      <a-col :md='4' :xs='0'></a-col>
      <a-col :md="15" >
        <a-card title="用户注册" content id="ucd">
          <a-form :form="form" @submit="handleSubmit">
              <a-form-item v-bind="formItemLayout">
              <span slot="label">
                昵称&nbsp;
                <a-tooltip title="What do you want others to call you?">
                  <a-icon type="question-circle-o" />
                </a-tooltip>
              </span>
              <a-input
                v-decorator="[
                  'nickname',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please input your nickname!',
                        whitespace: true,
                      },
                    ],
                  },
                ]"
              />
            </a-form-item>
            <!-- <a-form-item v-bind="formItemLayout" label="邮箱">
              <a-input
                v-decorator="[
                  'email',
                  {
                    rules: [
                      {
                        type: 'email',
                        message: 'The input is not valid E-mail!',
                      },
                      {
                        required: true,
                        message: 'Please input your E-mail!',
                      },
                    ],
                  },
                ]"
              />
            </a-form-item> -->
            <a-form-item v-bind="formItemLayout" label="密码" has-feedback>
              <a-input
                v-decorator="[
                  'password',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please input your password!',
                      },
                      {
                        validator: validateToNextPassword,
                      },
                    ],
                  },
                ]"
                type="password"
              />
            </a-form-item>
            <a-form-item v-bind="formItemLayout" label="确认密码" has-feedback>
              <a-input
                v-decorator="[
                  'confirm',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please confirm your password!',
                      },
                      {
                        validator: compareToFirstPassword,
                      },
                    ],
                  },
                ]"
                type="password"
                @blur="handleConfirmBlur"
              />
            </a-form-item>
            <!-- <a-form-item v-bind="formItemLayout" label="电话号码">
              <a-input
                v-decorator="[
                  'phone',
                  {
                    rules: [
                      {
                        required: true,
                        message: 'Please input your phone number!',
                      },
                    ],
                  },
                ]"
                style="width: 100%"
              >
                <a-select
                  slot="addonBefore"
                  v-decorator="['prefix', { initialValue: '86' }]"
                  style="width: 70px"
                >
                  <a-select-option value="86"> +86 </a-select-option>
                  <a-select-option value="87"> +87 </a-select-option>
                </a-select>
              </a-input>
            </a-form-item> -->
            <a-form-item v-bind="tailFormItemLayout">
              <a-button type="primary" html-type="submit"> 注册 </a-button>
              <a-divider type="vertical" />
              <a-button @click="$router.back(1)">返回</a-button>
            </a-form-item>
          </a-form>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      confirmDirty: false,
      autoCompleteResult: [],
      formItemLayout: {
        labelCol: {
          xs: { span: 24 },
          sm: { span: 8 },
        },
        wrapperCol: {
          xs: { span: 24 },
          sm: { span: 16 },
        },
      },
      tailFormItemLayout: {
        wrapperCol: {
          xs: {
            span: 24,
            offset: 0,
          },
          sm: {
            span: 16,
            offset: 8,
          },
        },
      },
    };
  },
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: "register" });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFieldsAndScroll( async (err, values) => {
        if (!err) {
          console.log("Received values of form: ", values);
          const { nickname:username, password } = values
          let res = await this.$api.User.register({ username, password })
          if( res.status !== 200 && res.status !== 201 ) return this.$message.warning("网络发生错误")
          const {flag , msg } = res.data
          if(flag){
            this.$message.success("注册成功").then(() => {
              this.$router.push("/Login");
            });
          }else{
            this.$message.error(msg)
          }
          
        }
      });
    },
    handleConfirmBlur(e) {
      const value = e.target.value;
      this.confirmDirty = this.confirmDirty || !!value;
    },
    compareToFirstPassword(rule, value, callback) {
      const form = this.form;
      if (value && value !== form.getFieldValue("password")) {
        callback("Two passwords that you enter is inconsistent!");
      } else {
        callback();
      }
    },
    validateToNextPassword(rule, value, callback) {
      const form = this.form;
      if (value && this.confirmDirty) {
        form.validateFields(["confirm"], { force: true });
      }
      callback();
    },
  },
};
</script>

<style>
</style>