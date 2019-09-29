import os
import glob

ld = open("wiki.txt")
lines = ld.readlines()
ld.close()

'''
txt_list = glob.glob("/home/ozawa/keio/research/0901/tfidf/*.txt")
main_list = []
for txt in txt_list:
    if("wiki.txt" in txt):
        continue
    else:
        main_list.append(txt) #TF-IDF対象のテキストファイル名
'''

txt = "food.txt"
#TF-IDF対象のテキストファイルをオープン
ld2 = open(txt, 'r')
line2 = ld2.readline()
tmp_list = []

while line2:
    line2 = line2.replace("\n", "")
    tmp_list.append(line2)
    line2 = ld2.readline()
ld2.close()
for r_txt in tmp_list: #ある文書の対象名(観光地など)
    flag = 0
    r_txt = r_txt.replace("\n", "")
    tmp = 'title="' + r_txt + '"'
    for line in lines:
        if ((tmp in line) & (flag == 0)):
            flag = 1
        if flag == 1:
            line = line.replace("\n", "")
            with open("sougou_" + txt, 'a') as f:
                print(line, file = f)
        if (("</doc>" in line) & (flag == 1)):
            flag = 0
            break
del tmp_list
del line2
del ld2
print("finish!!")
