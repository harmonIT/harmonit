const formData = {
    querySetting: [
        {"name":"XKSZDWDM","caption":"所在院系","linkOpt":"AND","builderList":"cbl_m_List","builder":"m_value_equal","value":"008","value_display":"计算机科学与技术学院（软件学院）"},
        {"name":"_gotoFirstPage","value":true,"linkOpt":"AND","builder":"equal"}
    ],
    pageSize: 10,
    pageNumber: 3
};

fetch("https://yjszs.zjut.edu.cn/gsapp/sys/dszszgxxykfwappzjut/modules/dszsxx/dszsxx_lbcx.do", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(formData)
})
.then(response => response.json())
.then(data => {
    console.log('成功:', data);
})
.catch((error) => {
    console.error('错误:', error);
});