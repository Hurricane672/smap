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
              :loading="loading"
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
      //   ????????????
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

      //   ???????????????
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
      loading: false,

      //?????????????????? basicInform
      // basicInform: this.$store.state.basicInform,
      basicInform: [],

      //web???????????? webInform
      // webInform:this.$store.state.webInform,
      webInform: [],

      //??????????????????????????? appInform

      //port??????
      // headers: this.$store.state.headers,
      headers: [],

      //scan result??????
      // headers1: this.$store.state.headers1,
      headers1: [],

      //port??? ??????
      desserts: [],

      //result??? ??????
      // desserts1: this.$store.state.desserts1,
      desserts1: [],

      editedIndex: -1,

      //???????????????????????????port
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
      //1.????????????nodes??????
      _this.nodes = new Vis.DataSet(_this.nodesArray);
      //2.????????????edges??????
      _this.edges = new Vis.DataSet(_this.edgesArray);
      _this.container = document.getElementById("network_id");
      _this.data = {
        nodes: _this.nodes,
        edges: _this.edges,
      };
      _this.options = {
        autoResize: true, //????????????????????????????????????????????????????????????????????????
        locale: "cn", //????????????????????????????????????
        //????????????
        locales: {
          cn: {
            //?????????????????????
            edit: "??????",
            del: "???????????????????????????",
            back: "??????",
            addNode: "????????????",
            addEdge: "????????????",
            editNode: "????????????",
            editEdge: "????????????",
            addDescription: "??????????????????????????????",
            edgeDescription: "??????????????????????????????????????????????????????",
            editEdgeDescription: "???????????????????????????",
            createEdgeError: "???????????????????????????",
            deleteClusterError: "??????????????????.",
            editClusterError: "??????????????????'",
          },
        },

        // ??????????????????
        nodes: {
          // shape: "circle",
          shape: "dot",
          size: 9,
          font: {
            //????????????
            size: 16,
            color:"white"
          },
          color: {
            border: "white", //??????????????????
            background: "black", //??????????????????
            highlight: {
              //???????????????????????????
              border: "#2B7CE9",
              background: "white",
            },
            hover: {
              //?????????????????????????????????
              border: "#2B7CE9",
              background: "#D2E5FF",
            },
          },
          borderWidth: 1, //??????????????????????????????px
          borderWidthSelected: 2, //?????????????????????????????????????????????px
        },
        // ????????????
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
            //??????????????????????????????????????????
            enabled: true, //?????????true????????????false?????????????????????????????????????????????????????????????????????????????????
          },
          arrows: { to: false }, //????????????to
        },

        //??????????????????????????????????????????????????????
        physics: {
          enabled: true, //?????????true????????????false??????????????????????????????????????????????????????????????????????????????
          barnesHut: {
            gravitationalConstant: -4000,
            centralGravity: 0.3,
            springLength: 120,
            springConstant: 0.04,
            damping: 0.09,
            avoidOverlap: 0,
          },
        },
        //???????????????????????????????????????????????????????????????????????????????????????????????????
        interaction: {
          hover: true,
          dragNodes: true, //?????????????????????
          dragView: true, //?????????????????????
          //   hover: true, //??????????????????????????????????????????
          multiselect: true, //??? ctrl ??????
          selectable: true, //????????????????????????
          selectConnectedEdges: true, //????????????????????????????????????
          hoverConnectedEdges: true, //??????????????????????????????????????????
          zoomView: true, //?????????????????????
        },
        //????????????:?????? ?????????????????????????????????????????????????????????????????????????????????
        manipulation: {
          enabled: false, //??????????????????????????????????????????????????????
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
      //   network???????????????????????????????????????????????????????????????????????????
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

          // // ??????????????????vuex???????????????remove
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

        // // ??????????????????vuex???????????????remove
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
    //?????????????????????????????????
    this.network.on("selectNode", (params) => {
      console.log("??????", params.nodes);
      this.loading = true

      basicInform({
        ipAddress: params.nodes.join(","),
      }).then((response) => {
        let basicInform = response.data.basicInform;
        console.log(basicInform);

        // // ??????????????????vuex???????????????remove
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

        // // ??????????????????vuex???????????????remove
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

        // // ??????????????????vuex???????????????remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_webInform", webInform);
        this.webInform = webInform;
        this.loading = false;
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