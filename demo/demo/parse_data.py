import requests
import pandas as pd


def fetch_ssb_data():
    BASEURL = "https://data.ssb.no/api/v0/dataset/"
    RESOURCE = "1054.json?lang=en"

    BASEURL = "https://raw.githubusercontent.com/jbrownlee/Datasets/master"
    RESOURCE = "longley.csv"
    # url = f"{BASEURL}/{RESOURCE}"

    # r = requests.get(url)
    # r.raise_for_status()
    # data = r.json()
    # df = pd.DataFrame(data)

    # print(f"printing data {df.head()}")

    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/longley.csv"
    df = pd.read_csv(url, header=None)
    data = df.values
    # choose the input and output variables
    x, y = data[:, 4], data[:, -1]

    print(df.head())

    return df


fetch_ssb_data()
