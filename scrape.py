import socket
import time
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import pandas as pd


def get_a_html_from_url(url, soup=False, retry=True):
    try:
        ret = requests.get(url)
    except socket.gaierror as e:
        print(f"gaierror occured")
    time.sleep(0.1)
    if ret.status_code != 200:
        print(f"Invalid return from requests")

        if retry is True:
            get_a_html_from_url(url, retry=False)
        else:
            print(f"Could not get HTML from {url}")

    html = ret.content

    if soup:
        return BeautifulSoup(html, "lxml")

    return html


def df_from_html_table(html, class_tag="table table-orders table-bordered table-striped table-responsive", only_df=True):
    
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", class_=class_tag)
    df_html = pd.read_html(table.prettify(), header=0)[0]
    if only_df:
        return df_html
    else:
        return df_html, table


if __name__ == "__main__":
    code = sys.argv[1] if len(sys.argv) == 2 else ""
    # url = "https://maonline.jp/pro/shareholding_reports?utf8=%E2%9C%93&query%5Bfildate_gteq%5D=2016-02-01&query%5Bfildate_lteq%5D=2019-02-06&query%5Bisname_or_issyokencode_or_company_iscode_start%5D={}&query%5Bcompany_edgyosyucode_in%5D%5B%5D=&query%5Bholdingname_or_holdingcode_start%5D=".format(code)
    url = "https://maonline.jp/pro/shareholding_reports?page=1&query%5Bcompany_edgyosyucode_in%5D%5B%5D=&query%5Bfildate_gteq%5D=2016-02-01&query%5Bfildate_lteq%5D=2019-02-06&query%5Bholdingname_or_holdingcode_start%5D=&query%5Bisname_or_issyokencode_or_company_iscode_start%5D=&utf8=%E2%9C%93"
    html = get_a_html_from_url(url)
    df = df_from_html_table(html)
    df.to_csv("smpl.csv")
    import pdb;pdb.set_trace();