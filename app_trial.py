# Imports 
import pandas as pd

import datetime

import schedule

import numpy as np


# trial function

def trial():
    
    r1 = np.random.randint(0, 100)
    
    r2 = np.random.randint(0, 100)
    
    df = pd.DataFrame(data = [r1, r2]).transpose()
    
    df.columns = ['First_num', 'Second_num']
    
    # Read in old excel
    latest = pd.read_excel('random.xlsx', index_col= 0)
    
    # Concat 
    concatenate = pd.concat([latest, df])
    
    # Write back to Excel sheet
    concatenate.to_excel("random.xlsx")
    
    return "job done at {}".format(datetime.datetime.now().strftime("%H : %M : %S")) 

# from 87,64 --> ..... --> 76, 96  -->  92, 41 --> 76, 7

if __name__ == "__main__":
    schedule.every(10).seconds.do(trial)

    while (datetime.datetime.now().hour == 20) & (datetime.datetime.now().minute <= 59):
        schedule.run_pending()

    #trial()