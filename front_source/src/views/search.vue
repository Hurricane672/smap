<template>
  <!-- <div class="search-background"></div> -->
  <div id="app">
    <v-app id="inspire">
      <v-app id="inspire">
        <v-main :style="Background">
          <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
              <v-col cols="12" sm="8" md="4">
                <v-form v-model="valid">
                  <v-col height="50%" align="center" justify="center">
                    <v-row align="center" justify="center">
                      <div class="text-h2 mb-2">Network segment scanner</div>
                      <br />
                    </v-row>
                    <br />
                    <v-row align="center" justify="center">
                      <v-col
                        cols="12"
                        md="4"
                       
                      >
                        <v-text-field
                          v-model="fromIp"
                          label="From"
                          required
                        ></v-text-field>
                      </v-col>

                      <v-col cols="12" md="4">
                        <v-text-field
                          v-model="toIp"
                          label="to"
                          required
                          
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <br />
                    <br />
                    <br />

                    <v-row align="center" justify="center" >
                      <v-btn @click="startScan" outlined style="background-color: rgba(255, 255, 255, 0.5)">SCAN START!</v-btn>
                    </v-row>
                  </v-col>
                </v-form>
              </v-col>
            </v-row>
          </v-container>
        </v-main>
      </v-app>
    </v-app>
  </div>
</template>

<script>
import { topoList } from "../network/request.js";

export default {
  name: "search",
  data() {
    return {
      valid: false,
      fromIp: "192.168.1.1",
      toIp: "192.168.1.5",
      Background: {
        backgroundImage: "url(" + require("../assets/images/bk1.jpg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundColor: "#000",
        backgroundPosition: "center top",
      },
    };
  },

  methods: {
    startScan() {
      console.log("发送");
      // this.$router.push({
      //     path: "/topo",
      // })

      topoList({
        fromIp: this.fromIp,
        toIp: this.toIp,
      }).then((response) => {
        let nodesArray = response.data.nodesArray;
        let edgesArray = response.data.edgesArray;
        console.log(nodesArray);
        console.log(edgesArray);
        // // 登录时添加到vuex，退出时要remove
        // this.$store.commit("SET_USER", userData)
        // this.$store.commit("SET_TOKEN", token)

        this.$store.commit("SET_nodesArray", nodesArray);
        this.$store.commit("SET_edgesArray", edgesArray);

        // this.$store.nodesArray = nodesArray
        // this.$store.edgesArray = edgesArray

        this.$router.push({
          path: "/topo",
        });
      });
    },
  },
};
</script>
