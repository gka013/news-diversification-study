#from tkinter.tix import Select
from django import forms
from django.core.exceptions import ValidationError
from django.db import close_old_connections, models
from django.db.models import fields
from django.forms import widgets
from .models import FoodCategory, HealthyRecipe, Personal_info, UnhealthyRecipe,EvaluateChoices,EvaluateChoices2,EvaluateChoices3, EvaluateChoices4,EvaluateChoices5,EvaluateChoices6,EvaluateChoices7,EvaluateChoices8,EvaluateChoices9,EvaluateChoices10,Ghs_fk
from django_starfield import Stars
from django.forms import formset_factory, modelformset_factory


class Personal_infoForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        exclude = ('id', 'created', 'title', 'session_id')
        widgets = {
            'gender': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'age': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            'country': forms.Select(attrs={'class': 'form-select form-select-sm clabel', 'required': True}),
            'education': forms.Select(attrs={'class': 'form-select form-select-sm clabel'}),
            
            #'FK_1' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_2' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_3' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_4' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_5' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_6' : forms.RadioSelect(attrs={'label_suffix':'',}),
            #'FK_7' : forms.RadioSelect(attrs={'labels_suffix':''}),
            #'FK_8' : forms.RadioSelect(attrs={'labels_suffix':''})
        }
        labels = {
            'gender': 'Gender',
            'age': 'Age',
            'country': 'Country of residence',
            'education': 'Your highest completed education',

        # food knowledge

            #'FK_1': 'My diet is well-balanced and healthy',
            #'FK_2': 'The amount of sugar I get in my food is important',
            #'FK_3': 'I have the impression that I sacrifice a lot for my health',
            #'FK_4': 'My health does NOT depend on the foods I consume',
            #'FK_5': 'I am concerned about the quantity of salt that I get in my food',
            #'FK_6': 'It is important for me that my daily diet contains a lot of vitamins and minerals',
            #'FK_7': 'The healthiness of snacks makes no difference to me',
            #'FK_8': 'I do no avoid foods, even if they may raise my cholesterol'

        }

class Ghs_fkForm(forms.ModelForm):
    class Meta:
        model = Ghs_fk
        exclude = ('id','person','created','title','session_id')
        widgets = {
            'FK_1'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_2'  : forms.RadioSelect(attrs ={'label_suffix':'',}),
            'FK_3'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_4'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_5'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_6'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_7'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_8'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_9'  : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_10' : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_11' : forms.RadioSelect(attrs={'label_suffix':'',}),
            'FK_12' : forms.RadioSelect(attrs={'label_suffix':'',})
        } 

        labels = {
            'FK_1' : 'The balance of nature is very delicate and easily upset',
            'FK_2' : 'When humans interfere with nature, it often produces disastrous consequences',
            'FK_3' : 'Humans must live in harmony with nature in order to survive',
            'FK_4' : 'Mankind is severely abusing the environment',
            'FK_5' : 'We are approaching the limit of the number of people the earth can support',
            'FK_6' : 'The earth is like a spaceship with only limited room and resources',
            'FK_7' : 'There are limits to growth beyond which our industrialized society cannot expand',
            'FK_8' : 'To maintain a healthy economy we will have to develop a “steady state” economy \n where industrial growth is controlled',

            # Items for subjective knowledge

            'FK_9' : 'Mankind was created to rule over the rest of nature',
            'FK_10': 'Humans have the right to modify the natural environment to suit their needs',
            'FK_11': 'Plants and animals exist primarily to be used by humans',
            'FK_12': 'Humans do not need to adapt to the natural environment because they can remake it to suit their needs'
        }




likert_scale = [ 
('1','Strongly Disagree'),
('2','Disagree'),
('3','Neutral'),
('4','Agree'),
('5','Strongly Agree')
]
popularity_stars = [
    ('3.8','3 stars'),
    ('4','4 stars'),
    ('0','No preferences')
]

class FoodCategoryForm(forms.ModelForm):

    class Meta:
        model = FoodCategory
        exclude = ('id', 'created', 'person','session_id')
        widgets = {
            'category': forms.Select(attrs={'class': 'btn'}),
            'recipe_popularity':forms.RadioSelect(attrs={'label_suffix':''},choices=popularity_stars),
            'calories':forms.NumberInput(attrs={ 'placeholder':'min=200, max=1000'}),
            'recipe_size':forms.NumberInput(attrs={ 'placeholder':'min=1, max=10'}),
           # 'recipes_mood':forms.RadioSelect(attrs={'label_suffix':''},choices=likert_scale),
            'preparation_time':forms.NumberInput(attrs={ 'placeholder':'min=15, max=60'}),
            'n_ingredient':forms.NumberInput(attrs={'placeholder':'min=3, max=10'})

            
            }
        labels = {
            'category': 'Food Category',
            'recipe_popularity': 'I want recipes at least with ',
            'calories': 'Preferred amount of calories in my recipe',
            'recipe_size': 'The prefered number of servings in my recipes are',
            #'recipes_mood': 'I prefer to eat food that will enhance my mood',
            'preparation_time': 'The time I have availabe for cooking (in min)',
            'n_ingredient': 'The preferred number of ingredients in  my recipe'
        }


class ChoiceEvaluationForm(forms.ModelForm):
    class Meta:
        model = EvaluateChoices
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            
            # choice difficulty
            
            'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            
            # Choice difficulty 
            'many_to_choose': 'Which color is mentioned in the text above?',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }


class ChoiceEvaluationForm2(forms.ModelForm):
    class Meta:
        model = EvaluateChoices2
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }






class ChoiceEvaluationForm3(forms.ModelForm):
    class Meta:
        model = EvaluateChoices3
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }




class ChoiceEvaluationForm4(forms.ModelForm):
    class Meta:
        model = EvaluateChoices4
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }









class ChoiceEvaluationForm5(forms.ModelForm):
    class Meta:
        model = EvaluateChoices5
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }



class ChoiceEvaluationForm6(forms.ModelForm):
    class Meta:
        model = EvaluateChoices6
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }










class ChoiceEvaluationForm7(forms.ModelForm):
    class Meta:
        model = EvaluateChoices7
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }
















class ChoiceEvaluationForm8(forms.ModelForm):
    class Meta:
        model = EvaluateChoices8
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            'many_to_choose': 'Which color is mentioned in the text above?',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }















class ChoiceEvaluationForm9(forms.ModelForm):
    class Meta:
        model = EvaluateChoices9
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }





class ChoiceEvaluationForm10(forms.ModelForm):
    class Meta:
        model = EvaluateChoices10
        exclude = ('id', 'created', 'title','person','session_id')
        widgets = {

            # choice satisfaction
            'liked_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'trust_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'fit_preference': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'know_many': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            'recommend_news': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
            # choice difficulty
            
            #'many_to_choose': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'diet_restriction': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'easy_choice': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'choice_overwhelming': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),

            # Perceived effort
            #'sys_time': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'unders_sys': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            #'many_actions': forms.RadioSelect(attrs={'label_suffix': '', 'required': True}),
            
        }
        labels = {
            
            # Choice satisfaction 
            'liked_news':"I have read the entire news",
            'trust_news':"I trust the article's content ",
            'fit_preference': "I agree with the article's content",
            #'know_many': 'I know many recipes that I like more than the one I have chosen',
            'recommend_news': 'I would recommend the chosen article to others',
            
            # Choice difficulty 
            #'many_to_choose': 'I changed my mind several times before making a decision ',
            #'diet_restriction': 'Do you have any dietary restrictions',
            #'easy_choice': 'It was easy to make this choice ',
            #'choice_overwhelming': 'Making a choice was overwhelming ',

            # Perceived effort
            #'sys_time':'The system takes up a lot of time',
            #'unders_sys':'I quickly understood the functionalities of the system',
            #'many_actions':'Many actions were required to use the system'
        }