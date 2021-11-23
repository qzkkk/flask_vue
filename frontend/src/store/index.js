"use strict";
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    isLogin:false,
    token:null,
    uid: null,
    username: null
  },
  plugins: [createPersistedState()],
  mutations: {
    login( state, data){
      state.isLogin = true
      const { data: { _id: uid, username } , token } = data
      state.token = token
      state.uid = uid
      state.username = username
      // console.log("登录", state)
    },
    logout(state) {
      state.isLogin = false
      state.token = null
      state.uid = ""
      state.username = ""
      // console.log("退出登录")
    }
  },
  actions: {
    login(context, data){
      context.commit('login',data)
    },
    logout({commit}){
      commit('logout')
    }
  }
})

export default store