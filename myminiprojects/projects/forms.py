from django import forms

class TitanicForm(forms.Form):
    Age = forms.IntegerField(label='Your age', max_value=999,min_value=0, initial=0)
    Gender = forms.CharField(label='Your Gender As M & F (as male and female)', initial='M')
    Parch = forms.IntegerField(label='Number of parents/children you might take to titanic with you', max_value=999,min_value=0, initial=0)
    Pclass = forms.IntegerField(label = 'Enter your class category 1 or 2 or 3',min_value=1, max_value=3, initial=3)
    SibSp = forms.IntegerField(label='Number of siblings/spouses you might take to titanic with you',max_value=8, min_value=0, initial=0)
    Embarked = forms.CharField(label = 'Port of Embarkation as Q(for Queenstown), S(for Southampton) & C (for Cherbourg)', initial='Q')
    Fare = forms.IntegerField(label = 'your price in $ btw 7$ to 150$', initial=7)
    class Meta:
        fields = ['Age', 'Gender', 'Parch', 'SibSp', 'Embarked', 'Fare']


class StockForm(forms.Form):
    stock_name = forms.CharField(label='Enter NYSE Stock Initials (e.g tsla, NFLX, amzn)')
    day_hour = forms.CharField(label = 'Enter 1d or 1h (for 1 day or 1 hour)')
    class Meta:
        fields = ['stock_name', 'day_hour']


innings_choice =(
    ("1", "first innings"),
    ("2", "second innings"))
toss_decision =(
    ("0", "Batting"),
    ("1", "Fielding"))
toss_winner_team = (
    ('0','Chennai Super Kings'),
    ('1','Delhi Capitals'),
    ('2','Delhi Daredevils'),
    ('3','Kings XI Punjab'),
    ('4','Kolkata Knight Riders'),
    ('5','Mumbai Indians'),
    ('6','Rajasthan Royals'),
    ('7','Royal Challengers Bangalore'),
    ('8','Sunrisers Hyderabad'))
batting_team = (
    ('9','Chennai Super Kings'),
    ('10','Delhi Capitals'),
    ('11','Delhi Daredevils'),
    ('12','Kings XI Punjab'),
    ('13','Kolkata Knight Riders'),
    ('14','Mumbai Indians'),
    ('15','Rajasthan Royals'),
    ('16','Royal Challengers Bangalore'),
    ('17','Sunrisers Hyderabad'))
bowling_team = (
    ('18','Chennai Super Kings'),
    ('19','Delhi Capitals'),
    ('20','Delhi Daredevils'),
    ('21','Kings XI Punjab'),
    ('22','Kolkata Knight Riders'),
    ('23','Mumbai Indians'),
    ('24','Rajasthan Royals'),
    ('25','Royal Challengers Bangalore'),
    ('26','Sunrisers Hyderabad'))



venue_choice =(
    ('25','Rajiv Gandhi International Stadium, Uppal'),
    ('19','Maharashtra Cricket Association Stadium'),
    ('19','Vidarbha Cricket Association Stadium, Jamtha'),
    ('11','Holkar Cricket Stadium'),
    ('4','Saurashtra Cricket Association Stadium'),
    ('15','M Chinnaswamy Stadium'),
    ('35','Wankhede Stadium'),
    ('7','Eden Gardens'),
    ('8','Feroz Shah Kotla'),
    ('23','Punjab Cricket Association IS Bindra Stadium, Mohali'),
    ('28','Sawai Mansingh Stadium'),
    ('18','MA Chidambaram Stadium, Chepauk'),
    ('5','Dr DY Patil Sports Academy'),
    ('16','Sardar Patel Stadium, Motera'),
    ('5','Himachal Pradesh Cricket Association Stadium'),
    ('2','Shaheed Veer Narayan Singh International Stadium'))

class IplForm(forms.Form):
    toss_winner = forms.ChoiceField(label='Toss winner',choices = toss_winner_team)
    toss_decision = forms.ChoiceField(label='Toss decision',choices = toss_decision)
    inning = forms.ChoiceField(label='Select inning',choices = innings_choice)
    batting_team = forms.ChoiceField(label='Select batting team',choices = batting_team)
    bowling_team = forms.ChoiceField(label='select bowling team',choices = bowling_team)
    over = forms.IntegerField(label='select over to be predicted',min_value=1, max_value=19)
    ball = forms.IntegerField(label='select ball for above over',min_value=1, max_value=6)
    expected_wickets = forms.IntegerField(label='Expected wickets falled till above overs',min_value=0, max_value=10)
    venue_choice = forms.ChoiceField(label='select venue',choices = venue_choice)
    class Meta:
        fields = [ 'toss_winner', 'toss_decision','inning', 'batting_team', 'bowling_team', 'over', 'ball', 'expected_wickets','venue_choice']

