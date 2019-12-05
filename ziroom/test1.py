from aip import AipOcr

"""api-key"""
APP_ID,API_KEY,SECRET_KEY = "16652935","RdFmQ0Q3OaWAgpN9Hive3SPN","Z35I68ykEBaYSwKPz6kd0COaQOXig0Qv"
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('d:/pic/8.jpg')
""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicAccurate(image)
print(result)