import pandas as pd


class HomesUrl():
    
    def __init__(self):
        homes_url = pd.read_csv("/home/dario/anaconda3/envs/funda_1/funda_KHNB_AMS/funda_KHNB_AMS/spiders/homes_url.csv")
        self.homes_url = homes_url.link.unique()

class EachHomeUrl():
    def __init__(self):
        each_home_url = pd.read_csv("/home/dario/anaconda3/envs/funda_1/funda_KHNB_AMS/funda_KHNB_AMS/spiders/each_home_url.csv")
        self.each_home_url = each_home_url.home_link.unique()
