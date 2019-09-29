import os
import glob
#全テキストファイル取得
txt_list = glob.glob("/home/ozawa/keio/research/0901/tfidf/*.txt")
for txt_file in txt_list:
    #ファイル読み込み部
    f = open(txt_file, 'r')
    line = f.readline()
    tmp_list = []

    #重複内容を排除
    while line:
        line = line.replace('\n', '')
        tmp_list.append(line)
        line = f.readline()
    f.close()
    os.remove(txt_file)

#重複排除したリストを書き込み
    main_list = list(set(tmp_list))
    del tmp_list
    with open(txt_file, 'a') as f:
        for txt in main_list:
            print(txt, file = f)
            print("SB")
    del main_list



