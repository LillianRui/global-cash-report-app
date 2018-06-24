# consolidator.py

import csv
import os
import datetime
import pandas as pd
from pandas import Series, DataFrame
import glob
import pandas as pd


from IPython.display import display

GLOBAL_PATH = './submissions/'
STD_COLS = ['']

print("""
-------------------------------------------------------
              Global Weekly Cash Report
-------------------------------------------------------
""")
print("Produced as of "+datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))



csv_filenames = os.listdir("submissions")
csvfiles = glob.glob('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/*.csv')
wf = csv.writer(open('/Users/Lillian/Desktop/global-cash-report-app/global-cash-report-app/submissions/all.csv','w'),delimiter = ",")
wf.writerow(["entity name","bank name","account number","currency","lc balance"])
for files in csvfiles:
    rd = csv.reader(open(files,'r'),delimiter = ',')
    next(rd)
    for row in rd:
        wf.writerow(row)

def _file_checker():
    files = os.listdir(GLOBAL_PATH)
    if len(files) < 6:
        raise ValueError("should have 6 files at least, but got {}".format(len(files)))

    for fname in files:
        abs_fpath = GLOBAL_PATH+fname
        col_names = pd.read_csv(abs_fpath).columns
        if len(col_names) != 5:
            raise ValueError('{} data should have 5 cols, but got {}'.format(abs_fpath, len(col_names)))


def _local_process(multiple_local_df, complete_df):
    companys = list(set(complete_df['entity name'].tolist()))
    currency = list(set(complete_df['currency'].tolist()))

    info_dic = {}
    for df_name in companys:
        df = complete_df[complete_data['entity name'] == df_name]
        statistic = df.groupby(['currency'])['lc balance'].sum()
        info_dic[df_name] =  statistic.to_dict()

    sub_company_df = []
    for key in companys:
        company_info = info_dic[key]
        currency_df = []
        for curr in currency:
            if curr not in company_info:
                val = 0
            else:
                val = company_info[curr]
            currency_df.append(val)
        sub_company_df.append(currency_df)

    sub_company_df = pd.DataFrame(sub_company_df, columns=currency)

    columns = zip(range(0,6), companys)
    col_dict = {}
    for item in columns:
        col_dict[item[0]] = item[1]

    sub_company_df = sub_company_df.T
    sub_company_df = sub_company_df.rename(columns=col_dict)

    sub_company_df['currency'] = sub_company_df.index
    return sub_company_df




def _global_process(complete_data, rate_df):

    total_local_currency = complete_data.groupby(['currency'])['lc balance'].sum()
    total_local_currency = total_local_currency.to_dict()
    tmp = []
    for key in total_local_currency.keys():
        princpal_currencies = key
        local_currency = total_local_currency[key]
        _tmp = [princpal_currencies, local_currency]
        tmp.append(_tmp)
    info_df = pd.DataFrame(tmp, columns=['currency','Total local currency'])
    info_df = info_df.merge(rate_df, on='currency', how='left')
    info_df = info_df.fillna(1)

    info_df['usd_equivelent'] = info_df['Total local currency']*info_df['rate']
    info_df['part_of_total'] = info_df['Total local currency']/info_df['Total local currency'].sum()

    return info_df



def process(glob, local):
    glob = glob.merge(local, on='currency', how='left')
    rename_dict = {'currency':'Principal Currendies',
                   'usd_equivelent':'USD Equivalant',
                   'part_of_total':'%of Total',
                   'rate':'Exchange Rate as $1=',
                   ' Total local currency':'Total Local Currency'}
    glob = glob.rename(columns=rename_dict)

    total_statistic = glob.drop(['Principal Currendies'], axis=1).sum()
    total_statistic = list(total_statistic)
    total_statistic.insert(0, 'USD Dollar Equivalant')

    glob.loc[glob.shape[0]] = total_statistic

    glob['%of Total'] = glob['%of Total'].round(2)
    glob = glob.astype(str)

    sort_cols = ['Principal Currendies' ,'Total local currency','Exchange Rate as $1=','USD Equivalant',
                'alpha','beta','delta','epsilon','gamma','zeta']
    glob = glob[sort_cols]
    return glob



def _bank_process(complete_df, rate):
    complete_df = complete_df.merge(rate, how='left', on='currency')
    complete_df = complete_df.fillna(1)
    complete_df['lc balance'] = complete_df['lc balance']*complete_df['rate']
    total_cash_usd = complete_df.groupby(['bank name'])['lc balance'].sum()

    bank_df = []
    for key in total_cash_usd.keys():
        tmp=[key, total_cash_usd[key]]
        bank_df.append(tmp)
    bank_df = pd.DataFrame(bank_df, columns=['Bank','Total Cash (USD)'])
    bank_df['% of Total'] = bank_df['Total Cash (USD)']/bank_df['Total Cash (USD)'].sum()
    ###############################################
    companys = list(set(complete_df['entity name'].tolist()))
    banks = list(set(complete_df['bank name'].tolist()))

    info_dic = {}
    for df_name in companys:
        df = complete_df[complete_data['entity name'] == df_name]
        statistic = df.groupby(['bank name'])['lc balance'].sum()
        info_dic[df_name] =  statistic.to_dict()

    sub_company_df = []
    for key in companys:
        company_info = info_dic[key]
        currency_df = []
        for curr in banks:
            if curr not in company_info:
                val = 0
            else:
                val = company_info[curr]
            currency_df.append(val)
        sub_company_df.append(currency_df)

    sub_company_df = pd.DataFrame(sub_company_df, columns=banks)

    columns = zip(range(0,6), companys)
    col_dict = {}
    for item in columns:
        col_dict[item[0]] = item[1]

    sub_company_df = sub_company_df.T
    sub_company_df = sub_company_df.rename(columns=col_dict)
    sub_company_df['Bank'] = sub_company_df.index
    bank_df = bank_df.merge(sub_company_df, how='left',on='Bank')


    total_statistic = bank_df.drop(['Bank'], axis=1).sum()
    total_statistic = list(total_statistic)
    total_statistic.insert(0, 'Total Cash')

    bank_df.loc[bank_df.shape[0]] = total_statistic
    bank_df['% of Total'] = bank_df['% of Total'].round(2)
    bank_df  = bank_df.astype(str)

    sort_cols = ['Bank','Total Cash (USD)','% of Total','alpha','beta','delta','epsilon','gamma','zeta']
    bank_df = bank_df[sort_cols]

    return bank_df



def query(sub_company, complete_data):
    sub_data = complete_data[complete_data['entity name']==sub_company]
    statistic = sub_data.groupby(['entity name','currency','bank name'])['bank name'].count()
    statistic = statistic.reset_index([0,1])
    statistic = statistic.rename({'bank name':'Number of Accounts'})
    statistic['Bank'] = statistic.index
    statistic = statistic.reindex()
    statistic.index = range(0,statistic.shape[0])

    return statistic



def _check_company(company_name):
    std_name = ['alpha','beta','delta','epsilon','gamma','zeta']
    upper_name = [x.upper() for x in std_name]
    std_name = std_name+upper_name

    if company_name not in std_name:
        return True







if __name__=="__main__":
    print("Welcome to Global Cash Report Consolidator\n")
    _file_checker()
    print("Processing submissions...\n")

    complete_data = pd.read_csv('./submissions/all.csv')
    rate = pd.read_csv('./fx_rate.csv', skiprows=[0], names=['currency', 'rate'])

    A = _global_process(complete_data, rate)
    B = _local_process(complete_data, complete_data)
    print("Cash by Currency by Division")
    display(process(A, B))
    print('\n\n\n')
    print("Cash by Bank by Division")
    display(_bank_process(complete_data,rate))

    print('Would you like to see Account Statistic?\n')
    ans = input("yes or no:")
    if ans == 'no':
        print('Ok, Thanks for using consolidator\n')
        exit()
    else:
        print("Input error, please enter 'yes' or 'no' ")

    while(1):
        que_company = input("input company:")
        if _check_company(que_company):
            print("invalid input, please enter a valid entity name")
            continue
        result = query(que_company.lower(), complete_data)
        display(result)

        is_stop = input('Would you like to search another entity? Enter STOP to end Consolidator, any other key to continue:')
        if is_stop == 'STOP':
            print('Ok, Thanks for using consolidator\n')
            break
        else:
            continue
