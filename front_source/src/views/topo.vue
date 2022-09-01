<template>
  <div id="app">
    <v-app id="inspire">
      <v-app id="keep">

        <v-navigation-drawer
          v-model="drawer"
          app
          clipped
          width="30%"
          right
          dark
          elevation="5"
        >
          <v-card class="mx-auto">
            <v-card class="mx-auto" color="black" dark>
              <v-card-title>
                <span class="title font-weight-bold" style="font-size: 100px; color: white;" 
                  >basic infomation</span
                >
              </v-card-title>

              <v-container>
                <v-row>
                  <v-col>
                    hostname: {{ basicInform.hostname }},<br />
                    mac_address: {{ basicInform.mac_address }},<br />
                  </v-col>
                  <v-col>
                    vendor: {{ basicInform.vendor }},<br />
                    delay: {{ basicInform.delay }},<br />
                  </v-col>
                </v-row>
              </v-container>
            </v-card>

            <v-divider></v-divider>

            <v-data-table
              :headers="headers"
              :items="desserts"
              :items-per-page="5"
              class="elevation-1"
              color="black"
            >
              <template v-slot:[`item.actions`]="{ item }">
                <v-icon small class="mr-2" @click="checkPort(item)">
                  mdi-eye
                </v-icon>
              </template>

              <template v-slot:top>
                <v-toolbar flat color="black" dark>
                  <!-- <v-toolbar-title>My CRUD</v-toolbar-title> -->
                  <v-card-title >
                    <span class="title font-weight-bold">appInform</span>
                  </v-card-title>

                  <v-divider class="mx-4" inset vertical></v-divider>

                  <v-spacer></v-spacer>

                  <v-dialog v-model="dialog" max-width="700px">
                    <v-card>
                      <v-card-title>
                        <span class="headline">Scan results</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.port"
                                label="port"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.service"
                                label="service"
                              ></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="editedItem.version"
                                label="version"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>

                        <v-data-table
                          :headers="headers1"
                          :items="desserts1"
                          :items-per-page="5"
                          class="elevation-1"
                        ></v-data-table>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close"
                          >Cancel</v-btn
                        >
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                </v-toolbar>
              </template>

              <!-- <template v-slot:no-data>
                <v-btn color="primary" @click="initialize">Reset</v-btn>
              </template> -->
            </v-data-table>

            <v-divider></v-divider>

            <v-card dark>
              <v-card-title>
                <span class="title font-weight-bold">webInform</span>
              </v-card-title>

              <v-tabs v-model="tab" background-color="black" dark>
                <v-tab v-for="item in webInform" :key="item">
                  port:{{ item.port }}
                </v-tab>
              </v-tabs>

              <v-tabs-items v-model="tab" dark>
                <v-tab-item v-for="item in webInform" :key="item">
                  <v-container>
                    <v-row>
                      <v-col>
                        <!-- <v-btn>cdn:{{ item.cdn }}</v-btn><br>
                        <v-btn>cms:{{ item.cms }}</v-btn><br>
                        <v-btn>framework:{{ item.framework }}</v-btn><br>
                        <v-btn>frontend:{{ item.frontend }}</v-btn><br> -->
                        <button @click="checkWeb('cdn',item.cdn)"> 
                          <v-icon small class="mr-2" >mdi-eye</v-icon>
                          cdn:{{ item.cdn }}
                        </button><br>

                        <button @click="checkWeb('cms',item.cms)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          cms:{{ item.cms }}
                        </button><br>

                        <button @click="checkWeb('framework',item.framework)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          fra:{{ item.framework }}
                        </button><br>

                        <button @click="checkWeb('frontend',item.frontend)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          fro:{{ item.frontend }}
                        </button><br>

                        <!-- cdn:{{ item.cdn }}<br /> -->
                        <!-- cms:{{ item.cms }}<br />
                        framework:{{ item.framework }}<br />
                        frontend:{{ item.frontend }}<br /> -->
                      </v-col>
                      <v-col>
                        <button @click="checkWeb('lang',item.lang)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          lang:{{ item.lang }}
                        </button><br>
                        <button @click="checkWeb('server',item.server)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          server:{{ item.server }}
                        </button><br>
                        <button @click="checkWeb('system',item.system)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          system:{{ item.system }}
                        </button><br>
                        <button @click="checkWeb('waf',item.waf)">
                          <v-icon small class="mr-2">mdi-eye</v-icon>
                          waf:{{ item.waf }}
                        </button><br>
                        
                        <!-- lang:{{ item.lang }},<br />
                        server:{{ item.server }},<br />
                        system:{{ item.system }},<br />
                        waf:{{ item.waf }}<br /> -->
                      </v-col>
                    </v-row>
                  <v-dialog v-model="dialog1" max-width="700px">
                    <v-card>
                      <v-card-title>
                        <span class="headline">{{ title }}</span>
                      </v-card-title>

                      <v-card-text>
                        <v-container>
                          <v-row>
                            <v-col cols="12" sm="6" md="4">
                              <v-text-field
                                v-model="titlecontent"
                              ></v-text-field>
                            </v-col>
                          </v-row>
                        </v-container>

                        <v-data-table
                          :headers="headers1"
                          :items="desserts1"
                          :items-per-page="5"
                          class="elevation-1"
                        ></v-data-table>
                      </v-card-text>

                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue darken-1" text @click="close"
                          >Cancel</v-btn
                        >
                      </v-card-actions>
                    </v-card>
                  </v-dialog>
                  </v-container>
                </v-tab-item>
              </v-tabs-items>
            </v-card>
          </v-card>
        </v-navigation-drawer>

        
          <v-main style="padding: 0;" :style="aBackground">
            <v-container fluid style="height:100%">
              <div class="text-h5 mb-2" style="color:white; height:10%">
                Network segment scanner
              </div>
              <br>
              <div id="network_id" class="network" style="height:90%" >

              </div>
            </v-container>

            
          </v-main>
      </v-app>
    </v-app>
  </div>
</template>

<script>
import Vis from "vis";
// import ipInfo from '../components/ipInfo.vue'

import { basicInform, appInform, webInform,findVul } from "../network/request.js";

export default {
  name: "topo-com",
  // inject: ['reload'],
  components: {
    // ipInfo
  },

  data() {
    return {
      dialogVisible: false,
      nodes: [],
      // network:null,
      container: null,
      //   节点数组
      nodesArray: [
        { id: 0, label: "192.168.215.1" },
        { id: 1, label: "192.168.215.2" },
        { id: 2, label: "192.168.215.3" },
        { id: 3, label: "192.168.215.4" },
        { id: 4, label: "192.168.215.5" },
        { id: 5, label: "192.168.215.6" },
        { id: 6, label: "192.168.215.7" },
        { id: 7, label: "192.168.215.8" },
        { id: 8, label: "192.168.215.9" },
        { id: 9, label: "192.168.215.10" },
        { id: "192.168.215.11", label: "192.168.215.11" },
      ],

      // nodesArray: this.$store.state.nodesArray,

      //   关系线数组
      edgesArray: [
        { from: 0, to: 1 },
        { from: 1, to: 2 },
        { from: 0, to: 2 },
        { from: 0, to: 3 },
        { from: 0, to: 4 },
        { from: 4, to: 5 },
        { from: 4, to: 6 },
        { from: 4, to: 7 },
        { from: 5, to: 8 },
        { from: 5, to: 9 },
        { from: 5, to: "192.168.215.11" },
      ],
      // edgesArray: this.$store.state.edgesArray,

      options: {},
      data: {},

      // *************************
      tab: null,
      dialog: false,
      dialog1: false,
      title:'',
      titlecontent:'',

      //基本物理信息 basicInform
      // basicInform: this.$store.state.basicInform,
      basicInform: [],

      //web应用信息 webInform
      // webInform:this.$store.state.webInform,
      webInform: [],

      //端口对应的服务信息 appInform

      //port表头
      // headers: this.$store.state.headers,
      headers: [],

      //scan result表头
      // headers1: this.$store.state.headers1,
      headers1: [],

      //port表 内容
      desserts: [],

      //result表 内容
      // desserts1: this.$store.state.desserts1,
      desserts1: [],

      editedIndex: -1,

      //当前选中，供查看的port
      editedItem: {
        port: 0,
        service: "",
        version: "",
      },

      defaultItem: {
        port: 0,
        service: "",
        version: "",
      },

      aBackground: {
        backgroundImage: "url(" + require("../assets/images/bk3.jpg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundColor: "#000",
        backgroundPosition: "center top",
      },
    };
  },
  watch: {
    dialog(val) {
      val || this.close();
    },

    dialog1(val1){
      val1 || this.close1();
    }
  },
  methods: {
    init() {
      let _this = this;
      //1.创建一个nodes数组
      _this.nodes = new Vis.DataSet(_this.nodesArray);
      //2.创建一个edges数组
      _this.edges = new Vis.DataSet(_this.edgesArray);
      _this.container = document.getElementById("network_id");
      _this.data = {
        nodes: _this.nodes,
        edges: _this.edges,
      };
      _this.options = {
        autoResize: true, //网络将自动检测其容器的大小调整，并相应地重绘自身
        locale: "cn", //语言设置：工具栏显示中文
        //设置语言
        locales: {
          cn: {
            //工具栏中文翻译
            edit: "编辑",
            del: "删除当前节点或关系",
            back: "返回",
            addNode: "添加节点",
            addEdge: "添加连线",
            editNode: "编辑节点",
            editEdge: "编辑连线",
            addDescription: "点击空白处可添加节点",
            edgeDescription: "点击某个节点拖拽连线可连接另一个节点",
            editEdgeDescription: "可拖拽连线改变关系",
            createEdgeError: "无法将边连接到集群",
            deleteClusterError: "无法删除集群.",
            editClusterError: "无法编辑群集'",
          },
        },

        // 设置节点样式
        nodes: {
          // shape: "circle",
          shape: "dot",
          size: 9,
          font: {
            //字体配置
            size: 16,
            color:"white"
          },
          color: {
            border: "white", //节点边框颜色
            background: "black", //节点背景颜色
            highlight: {
              //节点选中时状态颜色
              border: "#2B7CE9",
              background: "white",
            },
            hover: {
              //节点鼠标滑过时状态颜色
              border: "#2B7CE9",
              background: "#D2E5FF",
            },
          },
          borderWidth: 1, //节点边框宽度，单位为px
          borderWidthSelected: 2, //节点被选中时边框的宽度，单位为px
        },
        // 边线配置
        edges: {
          width: 1.5,
          length: 130,
          color: {
            color: "white",
            highlight: "white",
            hover: "white",
            inherit: "from",
            opacity: 1.0,
          },
          shadow: true,
          smooth: {
            //设置两个节点之前的连线的状态
            enabled: true, //默认是true，设置为false之后，两个节点之前的连线始终为直线，不会出现贝塞尔曲线
          },
          arrows: { to: false }, //箭头指向to
        },

        //计算节点之前斥力，进行自动排列的属性
        physics: {
          enabled: true, //默认是true，设置为false后，节点将不会自动改变，拖动谁谁动。不影响其他的节点
          barnesHut: {
            gravitationalConstant: -4000,
            centralGravity: 0.3,
            springLength: 120,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 0,
          },
        },
        //用于所有用户与网络的交互。处理鼠标和触摸事件以及导航按钮和弹出窗口
        interaction: {
          hover: true,
          dragNodes: true, //是否能拖动节点
          dragView: true, //是否能拖动画布
          //   hover: true, //鼠标移过后加粗该节点和连接线
          multiselect: true, //按 ctrl 多选
          selectable: true, //是否可以点击选择
          selectConnectedEdges: true, //选择节点后是否显示连接线
          hoverConnectedEdges: true, //鼠标滑动节点后是否显示连接线
          zoomView: true, //是否能缩放画布
        },
        //操作模块:包括 添加、删除、获取选中点、设置选中点、拖拽系列、点击等等
        manipulation: {
          enabled: false, //该属性表示可以编辑，出现编辑操作按钮
          addNode: false,
          addEdge: false,
          // editNode: undefined,
          editEdge: false,
          deleteNode: false,
          deleteEdge: false,
        },
      };

      _this.network = new Vis.Network(
        _this.container,
        _this.data,
        _this.options
      );
    },

    resetAllNodes() {
      let _this = this;
      _this.nodes.clear();
      _this.edges.clear();
      _this.nodes.add(_this.nodesArray);
      _this.edges.add(_this.edgesArray);
      _this.data = {
        nodes: _this.nodes,
        edges: _this.edges,
      };
      //   network是一种用于将包含点和线的网络和网络之间的可视化展示
      _this.network = new Vis.Network(
        _this.container,
        _this.data,
        _this.options
      );
    },
    resetAllNodesStabilize() {
      let _this = this;
      _this.resetAllNodes();
      _this.network.stabilize();
    },


    checkPort(item) {
        // console.log(item)
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)

        findVul({
           keywords:[this.editedItem.service,this.editedItem.version]
        }).then((response) => {
          let vuls = response.data.vuls;
          console.log(vuls);

          // // 登录时添加到vuex，退出时要remove
          // this.$store.commit("SET_USER", userData)
          // this.$store.commit("SET_TOKEN", token)

          this.$store.commit("SET_desserts1", vuls);
          this.desserts1 = vuls;
          this.dialog = true
        });
        // this.dialog = true

      },
    
    checkWeb(title,keyword){
      this.titlecontent = keyword;
      this.title = title;

      findVul({
          keywords:[keyword]
      }).then((response) => {
        let vuls = response.data.vuls;
        console.log(vuls);

        // // 登录时添加到vuex，退出时要remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_desserts1", vuls);
        this.desserts1 = vuls;
        this.dialog1 = true
      });

      // this.dialog1 = true
    },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      close1 () {
        this.dialog1 = false
      },
  },

  mounted() {
    this.init();
    //点击单个结点，触发事件
    this.network.on("selectNode", (params) => {
      console.log("点击", params.nodes);

      basicInform({
        ipAddress: params.nodes.join(","),
      }).then((response) => {
        let basicInform = response.data.basicInform;
        console.log(basicInform);

        // // 登录时添加到vuex，退出时要remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_basicInform", basicInform);
        this.basicInform = basicInform;
      });

      appInform({
        ipAddress: params.nodes.join(","),
      }).then((response) => {
        let appInform = response.data.appInform;
        console.log(appInform);

        // // 登录时添加到vuex，退出时要remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_desserts", appInform);
        this.desserts = appInform;
      });

      webInform({
        ipAddress: params.nodes.join(","),
      }).then((response) => {
        let webInform = response.data.webInform;
        console.log(webInform);

        // // 登录时添加到vuex，退出时要remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_webInform", webInform);
        this.webInform = webInform;
      });

      // this.dialogVisible = true;
    });
  },

  created() {
    this.nodesArray = this.$store.state.nodesArray;
    this.edgesArray = this.$store.state.edgesArray;

    this.basicInform = this.$store.state.basicInform;
    this.webInform = this.$store.state.webInform;

    this.headers = this.$store.state.headers;
    this.headers1 = this.$store.state.headers1;

    this.desserts = this.$store.state.desserts;
    this.desserts1 = this.$store.state.desserts1;
  },
};
</script>


<style lang="less">
</style>