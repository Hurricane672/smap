<template>
  <v-app>
    <v-main>
      <!-- <router-view v-if="isReloadAlive" /> -->
      <router-view v-if="isReloadAlive"></router-view>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  provide(){
    return{
      reload: this.reload
    }
  },
  data(){
     return{
      isReloadAlive: true
    }
  },
  methods: {
    reload() {
      this.isReloadAlive = false;
      this.$nextTick(function(){
        this.isReloadAlive = true;
      })
    }
  }
  // data: () => ({
  //   //
  // }),
};
</script>
