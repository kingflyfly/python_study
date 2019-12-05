#抓取自如房子价格
import re
import csv
import json
import requests
from queue import Queue
from aip import AipOcr
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

"""
conn = MongoClient('180.76.110.178', 27017)
db = conn.ziroom
my_ziroom = db.ziroom1
"""
class Ziroom(object):
    # 获取页码
    def get_pages(self,url):
        data = requests.get(url=url,headers=headers)
        data = pq(data.text)
        d1 = data("#page")
        str = d1.children("span").text()
        num = re.search("\d+",str)
        return int(num.group())

    # 获取房租详细信息
    def get_deail(self,url,doc):
        str = doc("#houseList .clearfix .txt")
        for i in str.items():
            c = dict()
            c["page"] = page
            c["url"] = i.find("h3").find("a").attr("href").lstrip("/")
            c["adress"] = i.find("h3").find("a").text()
            c["first_time"] = i.find("h4").find("span").text()
            c["detail"] = i.find(".detail").find("p").text()
            c["other"]  = i.find(".room_tags.clearfix").find("span").text()
            yield c

    # 获取每页的房屋价格，先获取图片，后根据偏移量获取价格
    def get_price(self,url,doc):
        str = doc("body script")
        value = re.search("ROOM_PRICE = (.*?);", str.text())
        #print(value)
        value1 = json.loads(value.group(1))
        #print(value1)
        png_url = "http:" + value1.get("image")
        reponse = requests.get(png_url)
        with open("d:/pic/{}.jpg".format(page), "wb") as f:
            f.write(reponse.content)
        with open("d:/pic/{}.jpg".format(page), 'rb') as fp:
            fp.read()
        image = self.get_file_content('d:/pic/{}.jpg'.format(page))
        result = client.basicAccurate(image)
        pri = result.get("words_result").pop().get("words")
        b = Queue() #创建队列
        for price in value1.get("offset"):
            a = ""
            for i in price:
                a += pri[i]
            b.put(a)
        return b

    # 写入数据库
    """
    def save_to_mongo(self,a):
        if my_ziroom.insert(a):
            print("ok")
    """
#baidu
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

# 测试
if __name__ == "__main__":
    base_url = "http://www.ziroom.com/z/nl/z3.html?"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    }
    house = Ziroom()
    page = 1
    address = "柳芳"
    data = {"qwd": address, "p": page}
    url = base_url + urlencode(data)
    nums = house.get_pages(url)
    """api-key"""
    APP_ID, API_KEY, SECRET_KEY = "16652935", "RdFmQ0Q3OaWAgpN9Hive3SPN", "Z35I68ykEBaYSwKPz6kd0COaQOXig0Qv"
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open("D:/pic/data.csv", "w",newline="") as f:
        file = ["page", "url", "adress", "first_time", "detail", "other", "price"]
        writer = csv.DictWriter(f, fieldnames=file)
        writer.writeheader()
    for page in range(1,nums+1):
        source = {"qwd": address, "p": page}
        url = base_url + urlencode(source)
        reponse = requests.get(url=url, headers=headers)
        doc = pq(reponse.text)
        n = house.get_deail(url,doc)

        n1 = house.get_price(url,doc)
        for i in n:
           i["price"] = n1.get()
           #print(i)
           #save_to_mongo(i)
           with open("D:/pic/data.csv","a",newline="") as f:
                file = ["page","url","adress","first_time","detail","other","price"]
                writer = csv.DictWriter(f,fieldnames=file)
                writer.writerow(i)



