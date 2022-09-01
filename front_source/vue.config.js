module.exports = {
  // 执行 npm run build 统一配置文件路径（本地访问dist/index.html需'./'）
  publicPath: './',
  
  transpileDependencies: [
    'vuetify'
  ],
  // 选项...
	// devServer: {
  //     // Paths
  //     open: true,
  //     host: 'localhost',
  //     // host: '0.0.0.0',
  //     port: 8080,
  //     proxy: {
  //       '/api': {
  //         // target: 'http://localhost:8082/',
  //         target: 'http://10.122.220.161:5000/',
  //         changeOrigin: true,
  //         ws: true,
  //         pathRewrite: {
  //           '^/api': '',
  //         },
  //       },
  //     },
  // },
}
