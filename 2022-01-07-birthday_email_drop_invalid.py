import pandas as pd
import numpy as np

personal=pd.read_csv('/Users/humphreyshen/Desktop/2021 Database Project/001總表最新資料/2022-01-07_updated_csv/dDt_alumnidb_personal.csv')
org_gmail=pd.read_csv('/Users/humphreyshen/Desktop/2021 Database Project/003數據預處理/Birthday_email/2022-01-07_export_invalid_email/生日賀卡錯誤Email名單匯出2021-12-30.csv')

invalid_email=org_gmail['Email'].replace("(錯誤)",'',regex=True).str.replace("(","",regex=True).str.replace(")","",regex=True)

for i in personal['email']:
    for x in invalid_email:
        if i == x:
         print(i) 