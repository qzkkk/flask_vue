"use strict";

import axios from 'axios'
import store from '~/store'
import Vue from 'vue';

const instance = axios.create({
  baseURL:'/api',

})
instance.interceptors.request.use(
  async config =>{
    // console.log(store)
    config.headers['Content-Type'] = 'application/json; charset=utf-8',
    config.headers.responseType = "json"
    config.headers.authorization = `Bearer ${store.state.token}`
    return config
  },
  error=>{
    return Promise.reject(error)
  }
)

instance.interceptors.response.use(
  response=>{
    if (response.status) switch(response.status){
      case 403:
        Vue.$message.warning("您的权限不足哦");
        break;
      case 402:
        Vue.$message.warning("请先登录");
        break;
      case 500:
        Vue.$message.warning("服务器发生错误");
        break;
    }
    return Promise.resolve(response)
  },
  error=>{
    Promise.reject(error)
  }
)

export default instance