function fetchData() {
    const formData = {
        querySetting: [
            {"name":"XKSZDWDM","caption":"所在院系","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":"008","value_display":"计算机科学与技术学院（软件学院）"},
            {"name":"_gotoFirstPage","value":true,"linkOpt":"AND","builder":"equal"}
        ],
        pageSize: 10,
        pageNumber: 3
    };

    return fetch("https://yjszs.zjut.edu.cn/gsapp/sys/dszszgxxykfwappzjut/modules/dszsxx/dszsxx_lbcx.do", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('网络响应异常');
        }
        return response.json();
    });
}

// 使用 .then() 处理结果
fetchData().then(data => {
    console.log('成功:', data);
}).catch(error => {
    console.error('错误:', error);
});

// 或者使用 async/await 语法
async function getData() {
    try {
        const data = await fetchData();
        console.log('成功:', data);
    } catch (error) {
        console.error('错误:', error);
    }
}

getData();
