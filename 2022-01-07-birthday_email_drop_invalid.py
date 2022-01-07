import pandas as pd
import numpy as np

personal=pd.read_csv('D:/Visual Code/Python/Python_Data_Cleaning_Birthday_Email/drive-download-20220107T142459Z-001/01-07_updated_csv拷貝/dDt_alumnidb_personal.csv')
org_gmail=pd.read_csv('D:/Visual Code/Python/Python_Data_Cleaning_Birthday_Email/drive-download-20220107T142459Z-001/生日賀卡錯誤Email名單匯出2021-12-30拷貝.csv')

invalid_email=org_gmail['Email'].replace("(錯誤)",'',regex=True).str.replace("(","",regex=True).str.replace(")","",regex=True)

result=[]
for i in personal.email:
    for x in invalid_email:
        if i == x:
           result.append(i)

result_frame=pd.DataFrame(result,columns=['email'])

final_result=personal.merge(result_frame, on='email', how='inner')

final_result_id=final_result.loc[:,['id']].drop_duplicates(subset=['id']).values.tolist()

print('update dDt_alumnidb_personal set email=NULL where id=%s' %final_result_id)