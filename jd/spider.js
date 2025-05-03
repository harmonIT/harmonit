let data; // 全局变量声明

function fetchData() {
    let searchStr = 'appid=pc-rate-qa&body=%7B%22requestSource%22%3A%22pc%22%2C%22shopComment%22%3A0%2C%22sameComment%22%3A0%2C%22channel%22%3Anull%2C%22extInfo%22%3A%7B%22isQzc%22%3A%220%22%2C%22spuId%22%3A%2210097625352914%22%2C%22commentRate%22%3A%221%22%2C%22needTopAlbum%22%3A%221%22%2C%22bbtf%22%3A%22%22%2C%22userGroupComment%22%3A%221%22%7D%2C%22num%22%3A%2210%22%2C%22pictureCommentType%22%3A%22A%22%2C%22scval%22%3Anull%2C%22shadowMainSku%22%3A%220%22%2C%22shopType%22%3A%220%22%2C%22firstCommentGuid%22%3A%2204e85a6876626352225dfc8bb355ec5b%22%2C%22sku%22%3A%2210097625352914%22%2C%22category%22%3A%229847%3B30503%3B30514%22%2C%22shieldCurrentComment%22%3A%221%22%2C%22pageSize%22%3A%2210%22%2C%22isFirstRequest%22%3Atrue%2C%22isCurrentSku%22%3Afalse%2C%22sortType%22%3A%225%22%2C%22tagId%22%3A%22%22%2C%22tagType%22%3A%22%22%2C%22type%22%3A%220%22%2C%22pageNum%22%3A%221%22%7D&client=pc&clientVersion=1.0.0&functionId=getCommentListPage&h5st=20250502140800064%3Bpd3axwi9gmqjmmj2%3B01a47%3Btk03wafe51bfc18naZxcpUMbXk06mHA3jgC_7mKNmjda_tJOGvCboe-3PLOX-ENqszs0Wu00I6ZlDhToUNcIE-S4uxs5%3B8cdb7b36a87e3fe9c91558600d3350f660c915cc7eb6656d44a2c0fea32dab8e%3B5.1%3B1746166077064%3BsmePkmsgAqLj_msm0mci5lImOuMsCmMiE5YTEpXTHJbU3NXW7eoSMuMgMuHVMusmk_sgOGLmAh4WMusmk_Mm3mLh_SbWNlrh_aoVJtbh7uriKVLV6uLW6ibVLZrV3iImOGLm_VqTHlYV3lsmOGujMaIW1ubhKRbh5eoh6eoi4OriLlbg6qoiIp7hMZIV4mIWMuMgMiXW41YWLlsmOGuj_uMgMebRMlsmOGujMiLj92ch4xZVCJIVPZrUMuMgMWHmOuMsCmMbbNae_K5b7i4ZMuMgM64TK1YW8lsmOGujMm7iAJ4ZMuMgMWoSMusmk_cPOuMs7uMgMqbi5lImOusmOGuj_qrm0msi9aHWMusmOuMsCObjOGLm8qbRMlsmOusmk_MmsFXStpnbcpHW6hLZXlsm0mcT-dITNlHmOusmOGuj_uMgMObRMlsmOusmk_siOGLm3aHWMusmOuMsCOLiOGLm4aHWMusmOuMsCurm0mch5lImOusmOGuj_uMgMebRMlsmOusmk_ci2qrm0m8i5lImOusmOGujMKLj92siMuMgMqbRMlsmOusmk_siOGLmDRHmOusmOGuj5uMgMinTMusmOuMsCurm0msTMusmOuMsCurm0msV3lsmOusmkCnm0msVAZoR2ZImOuMsC6nmOGOm4lpZ5VIT5R6ZBJnZPdIUMuMgMmrSMusmOuMsztMgMunSMusmk_Mm6WrQOCrh42YUXt8g_2si9usZgt8S3xoVAJ4ZMuMgMqYR7lsmOG_Q%3B0dda887daf57047af6b64029d1408a0cc513d5201e51bff26bca8fcda4558bed%3BtenjKJKT-JoRL1YRI9MT-J4S8ZIZ61YVF94WCeHTJJoTL9cQKxIWCeYU_tXW&loginType=3&t=1746166077048&uuid=17461438168051460715382';
    let formData = new FormData();
    let params = new URLSearchParams(searchStr);
    
    params.forEach((value, key) => {
        formData.append(key, value);
    });
    
    return fetch("https://api.m.jd.com/client.action", {
        method: "POST",
        body: JSON.stringify(formData),
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

// 输出：成功: {
//     "code": "1",
//     "echo": "required string parameter 'functionId' is not present"
//   }
//？？？？？？？？？？？可能有反扒，不知道什么原因


  

