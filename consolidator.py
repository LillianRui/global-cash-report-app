# consolidator.py

import csv
import os
import datetime
import pandas
import glob

print("""
-------------------------------------------------------
              Global Weekly Cash Report
-------------------------------------------------------
""")
print("Produced as of "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))


csv_filenames = os.listdir("submissions")
csvfiles = glob.glob('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/*.csv')
wf = csv.writer(open('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/all.csv','w'),delimiter = ",")

for files in csvfiles:
    rd = csv.reader(open(files,'r'),delimiter = ',')
    next(rd)
    for row in rd:
        wf.writerow(row)

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
