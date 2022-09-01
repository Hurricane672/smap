import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  /* vuex数据持久化配置 */
  plugins: [
    createPersistedState({
      // 存储方式：localStorage、sessionStorage、cookies
      storage: window.sessionStorage,
      // 存储的 key 的key值
      key: "store",
      render(state) {
        // 要存储的数据：本项目采用es6扩展运算符的方式存储了state中所有的数据
        return {
          ...state
        };
      }
    })
  ],

  // 状态
  state: {
    nodesArray:[
        {"id":"192.168.1.1", label:"192.168.1.1"},
        {"id":"192.168.1.2", label:"192.168.1.2"},
        {"id":"192.168.1.3", label:"192.168.1.3"},
        {"id":"192.168.1.4", label:"192.168.1.4"},
        {"id":"192.168.1.5", label:"192.168.1.5"},
        {"id":"192.168.1.6", label:"192.168.1.6"},
        {"id":"192.168.1.7", label:"192.168.1.7"},
    ],
    edgesArray:[
        {"from":"192.168.1.1", "to":"192.168.1.3"},
        {"from":"192.168.1.1", "to":"192.168.1.6"},
        {"from":"192.168.1.2", "to":"192.168.1.1"},
        {"from":"192.168.1.3", "to":"192.168.1.1"},
        {"from":"192.168.1.3", "to":"192.168.1.4"},
        {"from":"192.168.1.3", "to":"192.168.1.5"},
        {"from":"192.168.1.3", "to":"192.168.1.7"}
    ],

    basicInform:{
        "hostname":"uknown",
        "mac_address":"uknown",
        "vendor":"uknown",
        "delay":"uknown"
    },

    webInform:[
        {
            "port":"uknown",
            "cdn":"uknown",
            "cms":"uknown",
            "framework":"uknown",
            "frontend":"uknown", 
            "lang":"uknown",
            "server":"uknown",
            "system":"uknown",
            "waf":"uknown"
        },
        {
            "port":"uknown",
            "cdn":"uknown",
            "cms":"uknown",
            "framework":"uknown",
            "frontend":"uknown", 
            "lang":"uknown",
            "server":"uknown",
            "system":"uknown",
            "waf":"uknown"
        },
        {
          "port":"uknown",
          "cdn":"uknown",
          "cms":"uknown",
          "framework":"uknown",
          "frontend":"uknown", 
          "lang":"uknown",
          "server":"uknown",
          "system":"uknown",
          "waf":"uknown"
        },
      ],

      headers: [
          { text: 'Port', value: 'port' },
          { text: 'Service', value: 'service', sortable: false },
          { text: 'Version', value: 'version', sortable: false },
          { text: 'Actions', value: 'actions', sortable: false },
      ],

      headers1: [
          { text: 'cve_id', value: 'cve_id',sortable: false, width: '28%' },
          { text: 'info', value: 'info', sortable: false , width: '52%'},
          { text: 'date', value: 'date', sortable: false , width: '20%'}
      ],

    desserts: [
          {
              "port":"uknown",
              "service":"uknown",
              "version":"uknown"
          },
          {
              "port":"uknown",
              "service":"uknown",
              "version":"uknown"
          },
          {
              "port":"uknown",
              "service":"uknown",
              "version":"uknown"
          },
          {
              "port":"uknown",
              "service":"uknown",
              "version":"uknown"
          },
          {
            "port":"uknown",
            "service":"uknown",
            "version":"uknown"
          },
      ],

      desserts1: [
        {
            cve_id: "CVE-2022-34305",
            info: 'Apache Tomcat 跨站脚本漏洞（CVE-2022-34305）',
            date: '2022-06-24'
        },
        {
            cve_id: "CVE-2022-34305",
            info: 'Apache Tomcat 跨站脚本漏洞（CVE-2022-34305）',
            date: '2022-06-24'
        }
         
    ],

  },

  // 设置属性状态，处理数据的唯一途径，state的改变或赋值只能在这里
  mutations: {
    SET_nodesArray(state, data) {
      state.nodesArray = data
      // sessionStorage中存的是字符串，所以这里需要转化
      // window.sessionStorage.setItem("user", JSON.stringify(data))
    },

    SET_edgesArray(state,data){
      state.edgesArray = data
    },

    SET_basicInform(state,data){
      state.basicInform = data
    },

    SET_webInform(state,data){
      state.webInform = data
    },

    SET_headers(state,data){
      state.headers = data
    },

    SET_headers1(state,data){
      state.headers1 = data
    },

    SET_desserts(state,data){
      state.desserts = data
    },
    
    SET_desserts1(state,data){
      state.desserts1 = data
    },

  },

  // 应用mutations，数据的异步操作
  actions: {
  },
  modules: {
  }
})
