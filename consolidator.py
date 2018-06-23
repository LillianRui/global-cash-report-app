# consolidator.py

import csv
import os
import datetime
import pandas as pd
from pandas import Series, DataFrame
import glob

print("""
-------------------------------------------------------
              Global Weekly Cash Report
-------------------------------------------------------
""")
print("Produced as of "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

# print("Please enter current week's FX Rate for:")
# aud_fx_rate = input("AUD (Suggest: 0.7500): ")
# cad_fx_rate = input("CAD (Suggest: 0.7300): ")
# gbp_fx_rate = input("GBP (Suggest: 1.3200): ")
# eur_fx_rate = input("EUR (Suggest: 1.1600): ")
# jpy_fx_rate = input("JPY (Suggest: 0.0091): ")
# inr_fx_rate = input("INR (Suggest: 0.0150): ")
# usd_fx_rate = 1

#TODO: HOW TO VALIDATE INPUT IS POSTIVE NUMBER???????

csv_filenames = os.listdir("submissions")
csvfiles = glob.glob('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/*.csv')
wf = csv.writer(open('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/all.csv','w'),delimiter = ",")
wf.writerow(["entity name","bank name","account number","currency","lc balance"])
for files in csvfiles:
    rd = csv.reader(open(files,'r'),delimiter = ',')
    next(rd)
    for row in rd:
        wf.writerow(row)

df = pd.read_csv('all.csv')
df.groupby('currency')['lc balance'].sum()



# print(csv_filenames)
#
# for filename in csv_filenames:
#     filepath = f"submissions/{filename}"
#     print("-----------------------")
#     print("Entity Submissions: "+filepath)
#     with open(filepath,"r") as csv_file:
#         reader = csv.DictReader(csv_file)
#         all_sales = [float(row["lc balance"]) for row in reader]
#         monthly_sales = sum(all_sales)
#         monthly_sales_usd = "${0:,.2f}".format(monthly_sales)
#         print("... Total Sales: " + monthly_sales_usd)
#
# def mergeCsv():
#     csvx_list = glob.glob('*.csv')
#     print('here is %s CSV file'% len(csvx_list))
#     time.sleep(2)
#     print('running............')
#     for i in csvx_list:
#         fr = open(i,'r').read()
#         with open('add.csv','a') as f:
#             f.write(fr)
#         print('success')
#     print("success")
# mergeCsv()


#TODO: how to merge multiple csv into one file
#TODO: how to
