phone_number = "135 819 5813"
print(phone_number.replace(phone_number[3:],"*" * 7))
print("beijing\nshanghai\nnanjing")
city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
