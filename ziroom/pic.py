import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
a,b,c,d,e = [],[],[],[],[]
with open("D:/pic/data.csv") as f:
    reader = csv.reader(f)
    #print(type(reader))
    header = next(reader)
    #print(header)
    #for index,column_header in enumerate(header):
        #print(index,column_header)
    y_data = [x[6] for x in reader]
    for x  in y_data:
        x = int(x)
        if x <=3000:
            a.append(x)
        elif 3000 < x <= 4000:
            b.append(x)
        elif 4000 <x <= 5000:
            c.append(x)
        elif 5000 < x <= 6000:
            d.append(x)
        else:
            e.append(x)
zhfont1 = matplotlib.font_manager.FontProperties(fname="./SimHei.ttf")
for i  in a,b,c,d,e:
    plt.plot(i,".b")
plt.title("自如测试用例")
plt.ylabel("数量")
plt.show()
