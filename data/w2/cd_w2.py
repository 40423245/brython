#import os
#讀取w2b_cadlab.txt的檔案將其儲存為adata，並設定encoding為utf-8
adata = open("w2b_cadlab.txt", encoding="utf-8").read()
#讀取w2b_registered.txt的檔案將其儲存為rdata，並一行一行隔開，並設定encoding為utf-8
rdata = open("w2b_registered.txt", encoding="utf-8").read().splitlines()
#print(adata)
#利用splitlines將adata一行一行隔開並其儲存為alist
alist = adata.splitlines()
#print(alist[2])
#將變數n儲存為0
n = 0
#將列從0開始算起
row = 0
#將final_list儲存為一個空的數列
final_list = []
#將w2_list儲存為一個空的數列
w2_list = []
#執行一個for迴圈從第二列開始
for stud_num in alist[2:]:
    #每執行完一次迴圈列數+1
    row = row + 1
    #執行完迴圈後用\將其隔開並儲存為blist
    blist = stud_num.split("\t")
    #print(blist)
    #將行從0開始算起
    column = 0
    #執行一個for迴圈去取得blist裡的數列
    for i in range(len(blist)):
         #每執行完一次迴圈行數+1
        column = column + 1
        #假如blist數列裡不是空白
        if blist[i] != "":
            #print(blist[i])
            #將組序有用_隔開的儲存為clist 
            clist = blist[i].split("_")
            #將組序+_+學號+_+列+行的資料儲存為stud_data
            stud_data = clist[0]+"_"+clist[1]+"_"+str(row)+"_"+str(column)
             #將stud_data結果附加在final_list的資料裡
            final_list.append(stud_data)
            #將clist[1]結果附加在w2_list的資料裡
            w2_list.append(clist[1])
            #每執行完一次迴圈n+1
            n = n +1
# 根據數列前導字串排序, 目的在建立分組數列
group_list = sorted(final_list)
#列印出分組名單
print("分組名單:")
#執行一個for迴圈去取得group_list裡的數列
for i in range(len(group_list)):
    #列印出 group_list[i]的資料
    print(group_list[i])
#列印出座位列表
print("座位列表:")
#執行一個for迴圈去取得final_list裡的數列
for i in range(len(final_list)):
    #列印出 final_list[i]的資料
    print(final_list[i])
#執行一個for迴圈去取得rdata裡的數列
for i in range(len(rdata)):
    #假如有在rdata裡但沒有在w2_list裡，目的在找出缺席學生
    if rdata[i] not in w2_list:
        #列印出 rdata[i]的資料，缺席學生
        print("缺席學生:", rdata[i])
#列印出學生總數n個
print("學生總數:", n)
#print(os.environ)
