from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import TitanicForm, StockForm,IplForm
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from datetime import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import pickle

trend = "stable"
test_data=[]
def titanic(request):
    if request.method == 'POST':
        form = TitanicForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['Gender'] == 'M':
                gender_final = 1
            else:
                gender_final = 0
            if form.cleaned_data['Embarked'] =='S':
                embarked_final = 2
            if form.cleaned_data['Embarked'] =='Q':
                embarked_final = 1
            if form.cleaned_data['Embarked'] =='C':
                embarked_final = 0
            Age = form.cleaned_data['Age']
            Gender = form.cleaned_data['Gender']
            Parch = form.cleaned_data['Parch']
            Pclass = form.cleaned_data['Pclass']
            SibSp = form.cleaned_data['SibSp']
            Embarked = form.cleaned_data['Embarked']
            Fare = form.cleaned_data['Fare']            
            test_data = [Pclass, gender_final, Age, SibSp, Parch, Fare,embarked_final ]            
#i wasn't aware of pickel at this time
            train_df = pd.read_csv('projects/train.csv')
            combine = [train_df]
            for dataset in combine:
                dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False) 
            for dataset in combine:
                dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	            'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
                dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
                dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
                dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')  
            train_df[['Title', 'Age']].groupby(['Title'], as_index=False)
            for index in range(0,len(train_df)):
                missing = train_df['Age'][index]
                if missing >=0:
                    pass
                else:
                    if train_df['Title'][index] == 'Master':
                       train_df['Age'][index]=3.5
                    if train_df['Title'][index] == 'Miss':
                       train_df['Age'][index]=21
                    if train_df['Title'][index] == 'Mr':
                       train_df['Age'][index]=30
                    if train_df['Title'][index] == 'Mrs':
                       train_df['Age'][index]=35
                    if train_df['Title'][index] == 'Rare':
                       train_df['Age'][index]=48.5    
            train_df['Embarked'] = train_df['Embarked'].replace(np.nan, 's')
            for index in range(0,len(train_df)):
                missing = train_df['Age'][index]
                if missing >=0:
                    pass
                else:
                    train_df['Age'][index]=35.6   
            labelencoder_x = LabelEncoder()
            train_df['Sex'] = labelencoder_x.fit_transform(train_df['Sex'])
            train_df['Embarked'] = labelencoder_x.fit_transform(train_df['Embarked'])
            train_df.drop(['PassengerId','Name','Cabin','Ticket','Title'],axis=1, inplace=True)
            train_df_x=train_df[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
            train_df_y=train_df[['Survived']]
            random_forest = RandomForestClassifier(n_estimators=100)
            random_forest.fit(train_df_x, train_df_y)
            y_pred = random_forest.predict([test_data])
            if y_pred[0]==1:
                survived = 'Congo buddy you will survive on titanic'
            else:
                survived = 'sorry, you will not surive'
            return render(request, 'projects/titanic_result.html', {'result': survived})
    else:
        form = TitanicForm()
        return render(request, 'projects/titanic.html', {'form': form})


##################################################################################################################
"""'toss_winner', 'toss_decision','inning', 'batting_team', 'bowling_team',
 'over', 'ball', 'expected_wickets_till_this_over','venue_choice'
"""
def ipl(request):
    if request.method == 'POST':
        form = IplForm(request.POST)
        if form.is_valid():
            main_x = [[0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0]]
            toss_winner = int(form.cleaned_data['toss_winner'])
            toss_decision = int(form.cleaned_data['toss_decision'])
            inning = int(form.cleaned_data['inning'])
            batting_team = int(form.cleaned_data['batting_team'])
            bowling_team = int(form.cleaned_data['bowling_team'])
            over = form.cleaned_data['over']
            
            ball = form.cleaned_data['ball']
            expected_wickets = form.cleaned_data['expected_wickets']
            venue_choice = int(form.cleaned_data['venue_choice'])
            with open('projects/over-by-over-score-lr-model.pkl','rb') as file:
                response = pickle.load(file)
            main_x = [[0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0, inning,over,ball,expected_wickets,11,toss_decision,venue_choice]]
            main_x[0][toss_winner] = 1
            main_x[0][batting_team] = 1
            main_x[0][bowling_team] = 1
            result = int(response.predict(main_x)[0][0])
            print(main_x)
            context = {
                    "result" : result,
                    "wickets" : expected_wickets,
                    "over" : over,
                    "balls":ball
            }
        return render(request, 'projects/IPL_result.html',context)
    else:
        form = IplForm()
        return render(request, 'projects/IPL.html', {'form': form})





def stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock_name=form.cleaned_data['stock_name']
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
                month=1 
            start_date=str(start_year)+'-'+str(start_month)+'-'+day
            duration = form.cleaned_data['day_hour']
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
            dataset_main_x = dataset_final.iloc[0,[0,2,3,4,5,6,7]]
            #FOR NEXT HOUR/DAY PREDICTION
            linear = LinearRegression()
            linear.fit(dataset_x, dataset_y)
            y_pred = linear.predict([dataset_main_x])
            twenty_day__moving_average = [0]*30
            fifty_day_moving_average = [0]*60

            for tw in range(30):
                twenty_day__moving_average[tw] = abs(dataset['Open'][tw]-dataset['Adj Close'][tw])
            avg1 = sum(twenty_day__moving_average)/30

            for tw in range(60):
                fifty_day_moving_average[tw] = abs(dataset['Open'][tw]-dataset['Adj Close'][tw])
            avg = sum(fifty_day_moving_average)/60

            if(avg1>avg):
                trend = "Bullish"
            else:
                trend = "Bearish"
            link="https://en.wikipedia.org/wiki/Market_trend"
            context =  {'y_pred': y_pred[0][0],
                        'stock_name':stock_name,
                        'trend':trend,
                        'link':link
                        }
        return render(request, 'projects/stock_result.html', context)
    else:
        form = StockForm()
        return render(request, 'projects/stock.html', {'form': form})



def url_shortner(request):
    return redirect('https://visit-to.herokuapp.com/')


