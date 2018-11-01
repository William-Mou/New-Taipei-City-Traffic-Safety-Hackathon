
# coding: utf-8

# In[ ]:


#載入資料
import csv
import numpy as np

# 開啟 CSV 檔案
with open('106年樞紐分析表(有交叉路名及其他地點).csv', newline='',encoding="big5") as accident:
    accident = csv.reader(accident)
    accident = [row for row in accident]
    accident = np.array(accident)#rows是数据类型是‘list',转化为数组类型好处理
    print("資料格式=",type(accident),accident.shape)
    print("資料範本=",accident)
    
with open('路口經緯度對照表.csv', newline='',encoding="big5") as contrast:
    contrast = csv.reader(contrast)
    contrast = [row for row in contrast]
    contrast = np.array(contrast)#rows是数据类型是‘list',转化为数组类型好处理
    print("資料格式=",type(contrast),contrast.shape)
    print("資料範本=",contrast)


# In[51]:


#建立道路與座標映射表
contrasts = {}
for item in contrast[1:]:
    #print(item[8],item[7])
    if item[8] == "":
        continue
    contrasts[item[1]] = (float(item[8]),float(item[7]))
    


# In[52]:


#映射表檢查
contrasts


# In[61]:


#建立傷害計數
hurt = []
for row in accident:
    hurt.append(row[45])
print("24小時內死亡",hurt.count("24小時內死亡"))
print("受傷",hurt.count("受傷"))
print("未受傷",hurt.count("未受傷"))

#總件數
print("總件數",len(hurt))


# In[62]:


#手動直接複製貼上 24hr 30d內死亡的案件
# 路段 八里區中山路3段 八里區中山路3段 三芝區淡金公路 三重區 三重區仁美街 三重區自強路 三重區重新路2段 三重區集賢路 三峽區中正路3段 三峽區介壽路 三峽區介壽路 三峽區弘道路 三峽區弘道路 土城區中央路1段 土城區中央路2段 土城區中央路3段 土城區中央路4段 土城區金城路3段 土城區金城路3段 土城區裕民路 土城區擺接堡路 中和區 中和區中正路 中和區中正路 中和區中正路 中和區中和路 中和區民安街 中和區民德路 中和區光中路 中和區安平路 中和區安樂路 中和區宜安路 中和區員山路 中和區員山路 中和區景平路 中和區景平路 中和區新北環快道路 中和區環河西路 中和區環河西路3段 五股區中直路 五股區中港東路 五股區中興路2段 五股區成泰路1段 五股區成泰路1段 五股區疏洪一路 五股區疏洪一路 五股區疏洪一路 永和區中正橋道路 永和區環河東路1段 永和區環河東路3段 石門區台二線道路 石門區臺2線道路 石碇區 石碇區靜安路 汐止區大同路2段 汐止區民權街2段 汐止區同興路 汐止區汐萬路3段 汐止區福德一路 坪林區北宜公路 坪林區北宜路 坪林區北宜路 坪林區無名路 板橋區三民路2段 板橋區三民路2段 板橋區三民路2段 板橋區大觀路1段 板橋區中山路2段 板橋區中正路 板橋區文化路2段 板橋區民族路 板橋區板城路 板橋區南雅西路2段 板橋區國慶路 板橋區富山街 板橋區新崑路 板橋區新崑路 板橋區實踐路 板橋區漢生東路 板橋區漢生東路 板橋區漢生東路1段 板橋區臺65線道路 板橋區臺65線道路 板橋區臺65線道路 板橋區篤行路2段 板橋區篤行路3段 板橋區環河西路4段 板橋區環河西路4段 板橋區環河西路4段 板橋區環河西路5段 板橋區環河西路5段 板橋區環河西路5段 林口區106縣道 林口區文化一路2段 林口區忠孝路 金山區台二線道路 金山區台二線道路 泰山區文化街 泰山區泰山路 貢寮區臺2線道路 貢寮區臺2線道路 淡水區中正東路2段 淡水區中正東路2段 淡水區中正路2段 淡水區淡金路4段 新店區 新店區北宜路 新店區祥和路 新店區新北環快道路 新店區溪園路 新店區碧潭橋道路 新店區寶橋路 新莊區中平路 新莊區中正路 新莊區中正路 新莊區中正路 新莊區中和街 新莊區中原路 新莊區重新堤外道路 新莊區新五路 新莊區瓊林南路 瑞芳區魚桀魚坑路 瑞芳區臺62甲線道路 萬里區 萬里區臺二線道路 樹林區三俊街 樹林區三興路 樹林區佳園路2段 樹林區板林路 樹林區俊英街 樹林區柑園街2段 樹林區環漢路5段 樹林區環漢路5段 雙溪區臺2丙線道路 蘆洲區中正路 蘆洲區永樂街 蘆洲區復興路 蘆洲區環堤大道路 蘆洲區環堤大道路 鶯歌區尖山路 鶯歌區堤外道路 鶯歌區鶯桃路
# 轉換程死亡道路 list
dead_list = input().split()
dead_list


# In[65]:


# 應用上面的映射表，建立死亡作標 dict, list
dead_dict = {}
dead_pos = []
for i in dead_list[1:]:
    #print(i)
    i = i.replace('1段', '一段')
    i = i.replace('2段', '二段')
    i = i.replace('3段', '三段')
    i = i.replace('4段', '四段')
    i = i.replace('5段', '五段')    
    dead_dict[i] = contrasts[i]
    dead_pos.append(contrasts[i])
print("死亡字典", dead_dict)
print("死亡座標", dead_pos)

