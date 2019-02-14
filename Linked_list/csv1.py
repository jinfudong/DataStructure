import csv

# files = csv.reader(open('123.csv', 'r', encoding='utf-8'))
# for i in files:
#     print(i)
#打开文件，追加a
out = open('123.csv','a', newline='')
#设定写入模式
csv_write = csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow([1,2,3,4])
csv_write.writerow([1,2,3,4])
print ("write over")
