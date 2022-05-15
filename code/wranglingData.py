# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:03:24 2022

@author: cg639
"""

# %%
Dir_rawData = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData"
Dir_indoorAq = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/ParticulateMatter"
Dir_cleanData = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/cleanData"
Dir_externalAq = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/External"
Dir_indoorVOC = "C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/VolatileOrganicCompounds"

import os
import pandas as pd
from tqdm import tqdm

# %%
def CleanFiles(directory, typeAq, sType):
    count = 0
    for filename in os.listdir(directory):
        splitName = filename.split(sep = '_')
        uprns = splitName[1]
        sid = splitName[2][3:10]
        df = pd.read_csv(f"{directory}/{filename}")
        
        if typeAq == "indoorAq":
            df.columns.values[1] = "PM2_5"
        elif typeAq == "externalAq":
            df.columns.values[1] = "humidity"
            df.columns.values[2] = "temperature"
            df.columns.values[3] = "VOC"
            df.columns.values[4] = "PM2_5"
            df.columns.values[5] = "PM10"
        elif typeAq == "indoorVOC":
            df.columns.values[1] = "VOC"
            
        df['sid'] = sid
        df['sid'] = df['sid'].astype(str)
        df['uprns'] = uprns
        df['uprns'] = df['uprns'].astype(str)
        df['sensType'] = sType
        df['sensType'].astype(str)
        df.to_csv(f"{Dir_cleanData}/{typeAq}/{filename}")
        print(f"Finished {filename}")
        count += 1
    
    print("Finished all files!")
    print(f"Number of files processed {count}/{len(os.listdir(directory))}")

# %%

def ConcatAllFiles(directory):
    failedFiles = []
    df=pd.DataFrame()
    totalCount = 0
    totalNum = 0
    for folder in os.listdir(directory):
        if totalCount == 0:
            print(os.listdir(directory))
        count = 0
        folderDir = os.listdir(f"{directory}/{folder}")
        for filename in folderDir:
            try:
                aux=pd.read_csv(f"{directory}/{folder}/{filename}")
                df=pd.concat([df, aux], sort = False)
                totalCount += 1
                count += 1
            except:
                print(f"{filename} failed to concatenate")
                failedFiles.append(filename)

            totalNum += 1
        print(f"Succesfully concatenated {count}/{len(folderDir)} files from {folder}")
    print(f"Concatenate Done! {totalCount}/{totalNum}")
    print(f"Failed files: {failedFiles}")
    return df, failedFiles

#df,failedFiles = ConcatAllFiles("C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/cleanData")

test, ff = ConcatAllFiles("C:/Users/cg639/Downloads/test")

# %%
  
CleanFiles(Dir_indoorAq, "indoorAq", "IN")
CleanFiles(Dir_externalAq, "externalAq", "EX")
CleanFiles(Dir_indoorVOC, "indoorVOC", "IN")


#%%
df = pd.read_csv("C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/rawData/ParticulateMatter/ts_0001_sid6322063.csv")
df.head()
    
#df = pd.read_csv("C:/Users/cg639/University of Exeter/MTHM604-Tackling Sustainability Challenges using Data and Models-TERM2 (2021-22) - Group 2 - Group 2/MTHM604_week_1/data/cleanData/indoorAq/ts_0001_sid6322063.csv")
#df.head()
    
    

    
