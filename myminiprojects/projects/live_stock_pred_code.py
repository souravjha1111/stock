from sklearn.linear_model import LinearRegression
from datetime import datetime
import yfinance as yf
import pandas as pd
stock_name='AMZN'
current_date_time=datetime.now()
current_date_time = datetime.now() 
year = current_date_time.strftime("%Y")
month = current_date_time.strftime("%m")
day = current_date_time.strftime("%d")
time = current_date_time.strftime("%H:%M:%S")
time_hour = current_date_time.strftime("%H")
time_hour = current_date_time.strftime("%m")
time_hour = current_date_time.strftime("%S")
date_time = current_date_time.strftime("%m/%d/%Y, %H:%M:%S")
end_date=year+'-'+month+'-'+day
start_year=int(year)-1
start_month=int(month)
if start_month<12:
    start_month=start_month+1
else:
    month=1;
start_date=str(start_year)+'-'+str(start_month)+'-'+day
duration = '1d'   
dataset_new = yf.download(stock_name, 
                      start=start_date,
                      end=end_date,
                      interval=duration,
                      progress=False)
start_year_more=int(year)-2
start_month_more=int(month)
if start_month_more<12:
    start_month_more=start_month_more+1
else:
    month=1; 
end_date_more = start_date
start_date_more=str(start_year_more)+'-'+str(start_month_more)+'-'+day
dataset_older = yf.download(stock_name, 
                      start=start_date_more, 
                      end=end_date_more,
                      interval=duration,
                      progress=False)
dataset = dataset_older.append(dataset_new)
dataset['year'] = pd.DatetimeIndex(dataset.index).year
dataset['month'] = pd.DatetimeIndex(dataset.index).month
dataset['day'] = pd.DatetimeIndex(dataset.index).day
unique_values = dataset['year'].unique()
for value in range(0,len(unique_values)):
  for dataset_number in range(0,len(dataset['year'])):
    if dataset['year'][dataset_number] == unique_values[value]:
       dataset['year'][dataset_number] = value
dataset= dataset.drop('Close',axis = 1)
dataset_final = dataset.iloc[::-1]
dataset_final['High']=dataset_final['High'].shift(1)
dataset_x = dataset_final.iloc[1:,[0,2,3,4,5,6,7]]
dataset_y = dataset_final.iloc[1:,[1]]
dataset_main_y = dataset_final.iloc[1,[1]]
dataset_main_x = dataset_final.iloc[1,[0,2,3,4,5,6,7]]
linear = LinearRegression()
linear.fit(dataset_x, dataset_y)
y_pred = linear.predict([dataset_main_x])

print("y_pref is: " ,y_pred , '\n')
print("now for bull of bear")
twenty_day__moving_average = [0]*20
fifty_day_moving_average = [0]*50

for tw in range(20):
    twenty_day__moving_average[tw] = abs(dataset['Open'][tw]-dataset['Adj Close'][tw])
avg1 = sum(twenty_day__moving_average)/20

for tw in range(20):
    fifty_day_moving_average[tw] = abs(dataset['Open'][tw]-dataset['Adj Close'][tw])
avg = sum(fifty_day_moving_average)/50

if(avg1>avg):
    print("bearish",avg1 - avg)
    