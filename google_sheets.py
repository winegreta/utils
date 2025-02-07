import pandas as pd 


def read_google_sheets(doc_id, sheet_name = '0'):
    return pd.read_csv('https://docs.google.com/spreadsheets/d/' + doc_id + '/export?gid=0&format=csv&sheet={' + sheet_name + '}',
                       index_col=0
                      )

#test = read_google_sheets('1toSrMuP-HE9JexRdMzegNV5xcXKyHK3dUU1Y3NRw89Q')