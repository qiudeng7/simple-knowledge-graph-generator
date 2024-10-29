import axios from "axios"
// !Session认证机制(常规页面)
const sesstionRequest = axios.create({

    //分别在.env.development和.env.production文件中设置开发环境和生产环境的baseURL
    //.env文件会被vite读取，并自动区分开发环境和生产环境
    baseURL: import.meta.env.VITE_BASE_URL,
    // baseURL: 'http://localhost:8000',
    withCredentials: false,
    timeout: 100000
})

export function create_knowledge_graph(data) {
    return sesstionRequest({
        url: '/knowledge-graph/',
        method: 'post',
        data: data,
        headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json',
        },
        timeout: 0
    })
}



// const knowledgeGraphData = {
//     text: 'Graph Name',
// };

// create_knowledge_graph(knowledgeGraphData).then(response=>{
//     console.log(response.data)
// })