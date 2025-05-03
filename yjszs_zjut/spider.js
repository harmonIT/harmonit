let data; // 全局变量声明

function fetchData() {
    let searchStr = 'searchStr=%E8%AE%A1%E7%AE%97%E6%9C%BA&page=1&rows=18&orderStr=hot';
    let formData = new FormData();
    let params = new URLSearchParams(searchStr);
    
    params.forEach((value, key) => {
        formData.append(key, value);
    });
    
    return fetch("https://www.ptpress.com.cn/bookinfo/getBookListForEBTag", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: searchStr,
    })
}

async function getData() {
    try {
        resp = await fetchData();
        data=await resp.json(); 
        console.log('成功:', JSON.stringify(data,null,2));
    } catch (error) {
        console.error('错误:', error);
    }
}

getData();



  

