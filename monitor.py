#!/home/ubuntu/Python_Projects/degewo_monitor/venv/bin/python
import requests
import pandas as pd
from datetime import datetime
import os

def fetchData(url):
    '''
    Raises get request and when successfull returns the json data 

    inputs:
        url: url to which request is raised
    outputs:
        dict containing the json response from url 
        OR
        None when the response did not have status code 200
    '''
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Received status {response.status_code} when trying to access {url}")
        return None

if __name__ == "__main__":
    # Initialise variables
    base_url = "https://immosuche.degewo.de"
    next_pg = base_url + "/de/search.json"
    ftimestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_file = 'extract.parquet.gzip'

    if os.path.exists(output_file):
        df = pd.read_parquet(output_file)
    else:
        df = pd.DataFrame()
    
    while next_pg is not None:

        # Gets the data from url and converts it to dataframe, merges it with output df
        print(f"Getting Data from {next_pg}")

        r = fetchData(next_pg)
        temp = pd.json_normalize(r['immos'])
        temp['collection_timestamp'] = ftimestamp

        df = pd.concat([df, temp], ignore_index=True)

        # Checks if next_page is present to query if not breaks the loop
        try:
            next_pg = base_url + r['pagination']['next_page']
        except KeyError:
            break
    
    df.to_parquet("extract.parquet.gzip", compression = 'gzip')
