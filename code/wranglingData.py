# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:24 2022

@author: cg639
"""
Dir_rawData = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData"
Dir_indoorAq = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/ParticulateMatter"
Dir_cleanData = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/cleanData"
Dir_externalAq = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/External"


import os
import pandas as pd

def CleanFiles(directory, typeAq):
    for filename in os.listdir(directory):
        splitName = filename.split(sep = '_')
        uprns = splitName[1]
        sid = splitName[2][3:10]
        file = pd.read_csv(f"{directory}/{filename}")
        file['sid'] = sid
        file['sid'] = file['sid'].astype(str)
        file['uprns'] = uprns
        file['uprns'] = file['uprns'].astype(str)
        file.to_csv(f"{Dir_cleanData}/{typeAq}/{filename}")
        print(f"Finished {filename}")
    print("Finished all files!")
    
#CleanFiles(Dir_indoorAq, "indoorAq")
CleanFiles(Dir_externalAq, "externalAq")

#%%
df = pd.read_csv("C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/indoorAq/ts_0001_sid6322063.csv")
df.head()
    
    
    

    
