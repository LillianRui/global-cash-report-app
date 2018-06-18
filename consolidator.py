# consolidator.py

print("PROCESSING SOME CSV FILES HERE")

import csv
import os


csv_filenames = os.listdir("submissions")


print(csv_filenames)

for filename in csv_filenames:
    filepath = f"submissions/{filename}"
    print("-----------------------")
    print("Entity Submissions: "+filepath)
    with open(filepath,"r") as csv_file:
        reader = csv.DictReader(csv_file)
        all_sales = [float(row["lc balance"]) for row in reader]
        monthly_sales = sum(all_sales)
        monthly_sales_usd = "${0:,.2f}".format(monthly_sales)
        print("... Total Sales: " + monthly_sales_usd)
