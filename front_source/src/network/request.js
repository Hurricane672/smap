import axios from "axios"
// import router from "../router/index.js"

// axios.defaults.baseURL = "/api"
// axios.defaults.baseURL = "http://10.122.220.161:5000"
axios.defaults.baseURL = "http://localhost:5000"

// 配置拦截器
// 请求拦截器
// axios.interceptors.request.use(
// 	(config) => {
// 		console.log("请求拦截器", config)
// 		//1.1 获取到浏览器里面一直存储的token，并将它放到
// 		let uToken = localStorage.getItem("token")
// 		if (uToken) {
// 			//1.2 注意：给请求头里面添加u-token（后台判断就是取的这个请求头）请求头，并把随机数的token值也设置进去
// 			config.headers["u-token"] = uToken
// 		}
// 		// 注意这里修改完成之后需要返回config，否则无法进行后续工作
// 		return config
// 	},
// 	(err) => {
// 		// 拦截失败或者上述未返回config，则提示错误信息
// 		console.log(err)
// 	},
// )

// 响应拦截器
//2 使用axios设置后置拦截器，处理后台被拦截，没有登录的请求
// axios.interceptors.response.use(
// 	(result) => {
//         console.log("响应拦截器");
//         console.log(result)
// 		let data = result.data
//         console.log(data)
// 		//只要前台被拦截的请求里面含这两个参数，那么就跳转到登录界面
// 		if (data.code === 400 || data.msg === "没有验证信息或已失效") {
//             // 清理不正确的token，重新登录获取
//             window.localStorage.removeItem('token')
//             // 跳转到登录页面
// 			this.$router.push({
// 				path: "/login",
// 			})
// 		}
// 		return result
// 	},
// 	(error) => {
// 		Promise.reject(error)
// 	},
// )


//拓扑图接口
export function topoList(params) {
	return axios.post("/topoList", params)
}

//基本物理信息 接口
export function basicInform(param) {
	return axios.post("/basicInform", param)
}

//端口对应的服务信息 appInform
export function appInform(param) {
	return axios.post("/appInform", param)
}

// web应用信息 webInform
export function webInform(param) {
	return axios.post("/webInform", param)
}

//关键字查询接口 findVul
export function findVul(param) {
	return axios.post("/findVul", param)
}