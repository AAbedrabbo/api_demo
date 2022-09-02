# Imports 
import pandas as pd

import requests

import datetime

import schedule



def update_sheet(): 
    
    """
    Input: None
    
    Output: 
    
    """
    url = "https://api.openweathermap.org/data/2.5/weather?q=New%20York&units=metric&appid=6afed078490ecfc7c483c00353bb1d30"
    
    json_response = requests.get(url).json()
    
    variables_of_interest = [json_response['weather'][0]['main'], 
                             json_response['main']['temp'], 
                             json_response['main']['humidity']]
    
    # Date/Time stamps
    datetimestamp = datetime.datetime.now()
    
    month = datetime.datetime.now().month
    
    day = datetime.datetime.now().day
    
    hour = datetime.datetime.now().hour
    
    minute = datetime.datetime.now().minute
    
     
    df = pd.DataFrame(variables_of_interest).transpose()
        
    df['Date/Time stamp'] = datetimestamp
        
    df['Month'] = month
        
    df['Day'] = day
        
    df['Hour'] = hour
        
    df['Minute'] = minute
        
        
    df.columns = ["Desc", "Temp (C)", "Humidity", "Date/Time stamp", "Month", "Day", "Hour", "Minute"]
    

    # Read last version of data 
    last_version = pd.read_excel("API_demo_results.xlsx", index_col= 0)
    
    # Concat 
    concat = pd.concat([last_version, df])
    
    # Write back to Excel sheet
    concat.to_excel("API_demo_results.xlsx")
    
    return "job done at {}".format(datetime.datetime.now().strftime("%H : %M : %S")) 



if __name__ == "__main__":

    schedule.every(1).hour.do(update_sheet)

    while True:
        schedule.run_pending()

