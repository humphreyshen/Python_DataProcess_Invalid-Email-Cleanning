import pandas as pd
import numpy as np

print('\n\n==============================================\n歡迎使用由HumphreyShen所設計之電子信箱比對程式\n==============================================\n')
print('請依序輸入「預計比對的檔案路徑」與「與經過整理的失效電子信箱檔案路徑」')
print('請注意，本程式所截取之檔案預設為CSV檔！如您輸入錯誤系統會主動提醒您！')

Original_Path=()
Compare_Path=()

while True:
    temp_input_1 = input ('\n\n >> 請先輸入您預計更新的檔案路徑：')
    if (temp_input_1 != 'Y') and ('.csv' in temp_input_1):
        Original_Path=temp_input_1
        print('\n初步驗證正確，請在下方鍵入"Y"以做為確認')
    elif temp_input_1 == 'Y':
        break
    else:
        print('您似乎輸入了錯誤路徑或檔案，請檢查後重新輸入！\n')

while True:
    temp_input_2 = input('\n\n >> 請輸入您整理彙整失效電子信箱的檔案路徑：')
    if (temp_input_2 != 'Y') and ('.csv' in temp_input_2):
        Compare_Path=temp_input_2
        print('\n初步驗證正確，請在下方鍵入"Y"以做為確認')
    elif temp_input_2 == 'Y':
        break
    else:
        print('您似乎輸入了錯誤路徑或檔案，請檢查後重新輸入！\n')
    

personal=pd.read_csv(Original_Path)
org_gmail=pd.read_csv(Compare_Path)

invalid_email=org_gmail['Email'].replace("(錯誤)",'',regex=True).str.replace("(","",regex=True).str.replace(")","",regex=True)

result=[]
for i in personal.email:
    for x in invalid_email:
        if i == x:
           result.append(i)

result_frame=pd.DataFrame(result,columns=['email'])

final_result=personal.merge(result_frame, on='email', how='inner')

final_result_id=final_result.loc[:,['id']].drop_duplicates(subset=['id']).values.tolist()

print('\n\n\n--------以下編號是由系統為您比對出需要刪除之錯誤電子信箱的ID序號--------')
print(final_result_id)