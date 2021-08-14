import requests
import pandas
import csv

# X-Auth-Token Header
header = {
    "X-Auth-Token": "r43nld0gf1c7xlmtw2xygontzimy60f"
}

# Link creation
link = "https://api.bigcommerce.com/stores/q6xsfp1zsy/v3/catalog/products/"
store_id = "PRODUCT_ID"
value = "/options"
full_link = link + store_id + value

# List generation
data = pandas.read_csv("hoodie.csv")
list_id = data['product_id'].tolist()

# Create an Excel file to write
c = csv.writer(open('option_ids_list.csv', 'w'), lineterminator='\n')

# Link replacement and GET API
for item in list_id:
    replaced_full_link = full_link.replace(store_id, str(item))
    r = requests.get(replaced_full_link, headers=header).json()
    option_id = r['data'][0]['id']
    value_id = r['data'][0]['option_values'][0]['id']
    c.writerow([item, option_id, value_id])