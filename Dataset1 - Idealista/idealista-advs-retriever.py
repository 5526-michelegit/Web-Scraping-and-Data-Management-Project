import pandas as pd
import pandas as pd

from adv_single_retriever import *

# Import the urls
urls = pd.read_csv('csvs/idealista-filters-urls.csv')['URL'].tolist()

#Retrieve all the advs
for index, item in enumerate(urls):
    print(f'Retrieving advs from {item}')
    items = get_advs(item)
    df = pd.DataFrame(items)
    df.to_csv(f'csvs/advs/idealista_urls_{index + 1}.csv')

print('Retrieve Completed')