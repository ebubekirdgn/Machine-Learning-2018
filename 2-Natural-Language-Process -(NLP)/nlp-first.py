# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:09:59 2018

@author: EbubekirDogan
"""

import pandas as pd

#%% import twitter data

data = pd.read_csv(r"gender-classifier.csv",encoding="latin1") #burada r oku anlamında latin1 dediğimiz ise latin harflarine göre işlem yap demektir.
data = pd.concat([data.gender,data.description],axis=1)
data.drop(axis=0,inplace =True)  #axis 0 dediğimiz şey listede nan olan satırları drop et demek. inplace ise datayı direk içine eşitliyoruz.
data.gender = [1 if each == "female" else 0 for each in data.gender] # twitter csvmizden kadın ve erkek (male and female) ayırdık.

#%% bu bölümde cleaning data yapılacak
# regular expression kullanılarak
import re 

first_description = data.description[4]
description =re.sub("[^a-zA-Z]"," ",first_description) # ^ bu işaret a-dan z-ye olmayanları bulma demektir.