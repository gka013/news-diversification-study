from django.forms import formset_factory
from django.db.models import Count
import datetime
import pandas as pd
from random import choice, sample
import random
from sys import prefix
from django import forms
from django.db import reset_queries
from django.forms.models import ModelForm
from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from pandas.core.indexes import category
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import models
#from Labels_Nudges.app import get_top_recommendations
from .forms import Personal_infoForm, FoodCategory, FoodCategoryForm,ChoiceEvaluationForm, ChoiceEvaluationForm2,ChoiceEvaluationForm3,ChoiceEvaluationForm4,ChoiceEvaluationForm5,ChoiceEvaluationForm6,ChoiceEvaluationForm7,ChoiceEvaluationForm8,ChoiceEvaluationForm9,ChoiceEvaluationForm10,Ghs_fkForm
# from django.forms import formset_factory, modelformset_factory
from .models import  ClimateNews, Personal_info, HealthyRecipe, UnhealthyRecipe, SelectedRecipe,EvaluateChoices,EvaluateChoices2, EvaluateChoices3, EvaluateChoices4,EvaluateChoices5,EvaluateChoices6,EvaluateChoices7,EvaluateChoices8,EvaluateChoices9,EvaluateChoices10,Recommendations, Ghs_fk
 # from .app import *
# Create your views here.
# person_id = 0
import string
import random
import re
#def home(request):
 #   request.session['person_id'] = 0
  #  return render(request, 'Labels_Nudges/homes.html', context={})

def home(request):
    request.session['person_id'] = 0
    #prolific_id = , msg)
    #prolific_id = str(prolific_id.group(1))
    full_url = request.get_full_path()
    #request.GET['PROLIFIC_PID']
    print('Full',request.get_full_path())
    print(full_url)
    if 'PROLIFIC_PID' in full_url:
        prolific_id = re.search("PROLIFIC_PID=(.*?)&STUDY_ID",full_url)
        request.session['prolific_id'] = str(prolific_id.group(1))
        print("----------",prolific_id.group(1))
    else:
        request.session['prolific_id'] = '500'
        
        print(request.session['prolific_id'])
    return render(request, 'Labels_Nudges/homes.html')


def personal_info(request):
    try:
        user_selected = Personal_info.objects.filter(id = request.session['person_id'])
    
        if user_selected:
            Personal_info.objects.filter(id=request.session['person_id']).delete()
        if request.method == 'POST':
            personl_info = Personal_infoForm(request.POST)
            if personl_info.is_valid():
                answer = personl_info.save(commit=False)
                
                rd_str =''.join(random.choice(string.ascii_lowercase) for _ in range(5))
                time_now = datetime.datetime.now().strftime('%H%M%S')
                gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
                personl_info.instance.session_id = gene_session

                answer = personl_info.save(commit=True)
                
                request.session['person_id'] = answer.id
                gene_session = 'dars'+time_now +'_'+str(answer.id)+rd_str
                personl_info.instance.session_id = request.session['prolific_id']
                
                request.session['session_id'] = gene_session
                answer = personl_info.save(commit=True)

                request.session['person_id'] = answer.id
                return redirect('Labels_Nudges:ghs_fk')
        else:
            personl_info = Personal_infoForm()

    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')
    return render(request, 'Labels_Nudges/personal_info.html', context={'form': personl_info})

def ghs_fk(request):
    global Sub_100Articals
    Sub_100Articals = []
    Sub_100Articals= sample(range(1, 101), 10)
    #Sub_100Articals= sample(range(101, 201), 10)
    print (Sub_100Articals)
    
    try:
        user_selected = Ghs_fk.objects.filter(id = request.session['person_id'])
    
        if user_selected:
            ghs_fk.objects.filter(id=request.session['person_id']).delete()
        if request.method == 'POST':
            ghs_fk_form = Ghs_fkForm(request.POST)
            #print('------- Here')
            if ghs_fk_form.is_valid():
                answer = ghs_fk_form.save(commit=False)

                rd_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
                time_now = datetime.datetime.now().strftime('%H%M%S')
                gene_session = 'dars' +  time_now + '_' + str(answer.id) + rd_str
                ghs_fk_form.instance.session_id = gene_session
                ghs_fk_form.instance.person_id = request.session['person_id']
                #print(';;;;;;;;;;;here')
                answer = ghs_fk_form.save(commit = True)

                #request.session['person_id'] = answer.id
                return redirect('Labels_Nudges:choice_evaluation')
                #return redirect('Labels_Nudges:select_category')
        else:
            ghs_fk_form = Ghs_fkForm()

    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')
    return render(request, 'Labels_Nudges/healthy_knowledge.html', context={'form':ghs_fk_form})

def random_recipes(category):
    size = len(HealthyRecipe.objects.filter(category = category))
    ten_pr = size // 10
    if ten_pr < 5:
        ten_pr = size // 2
    h_recipes = HealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id', flat=True)[:ten_pr]
    uh_recipes = UnhealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id',flat=True)[:ten_pr]
    # print(f'len ------------------------- {len(h_recipes)} {size}')
    # unh_recipes = UnhealthyRecipe.objects.filter(category = category).order_by('-NumberRatings').values_list('id', flat=True)[:ten_pr]
    h_5 = sample(list(h_recipes), 5)
    uh_5 = sample(list(uh_recipes),5)
    return h_5, uh_5

    





def select_category(request):
    user_selected = FoodCategory.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        FoodCategory.objects.filter(person_id=request.session['person_id']).delete()
    categoryForm = FoodCategoryForm()
    if request.method == "POST":
        categoryForm = FoodCategoryForm(request.POST)
        if categoryForm.is_valid():
            category = categoryForm.save(commit=False)
            category.person_id = request.session['person_id']
            categoryForm.instance.session_id = request.session['session_id']
            category = categoryForm.save()

            user_category = FoodCategory.objects.filter(
            person_id=request.session['person_id']).values_list('category', flat=True)
            user_category = user_category[0]
            recipes, un_recipes = random_recipes(user_category)

        #------------------------- Save user inputs-----------------

            request.session['rcp'] = recipes
            request.session['un_rcp'] = un_recipes
            return redirect('Labels_Nudges:recipe_recommendations')
    else:
        categoryForm = FoodCategoryForm()
    return render(request, 'Labels_Nudges/select_category.html', context={'form': categoryForm})


# --- Boost presentation -------
def nutrition_labels(request): 
    if request.method == "POST":
            return redirect('Labels_Nudges:recipe_recommendations')
    else:        
            return render(request, 'Labels_Nudges/boost.html')



def mtl_color(cnt):
    colors = ['green','orange','red']
    level = ['Low','Medium','High']
            # 5 salts (color, level)
    return [ (colors[cnt[0]-1], level[cnt[0]-1]), (colors[cnt[1]-1], level[cnt[1]-1]), (colors[cnt[2]-1], level[cnt[2]-1]), (colors[cnt[3]-1], level[cnt[3]-1]), (colors[cnt[4]-1], level[cnt[4]-1])    ]

# This function is for Jeng's testing code
def list_news(request):

    newsAttributes = ClimateNews.objects.get(pk=2)
    newsList = [newsAttributes.id,newsAttributes.image_url]
        #context = {'image':image[1],'title':image[1][1]}
    return render(request, 'Labels_Nudges/list_news.html',context = {'newsList':newsList})
    
    # this used to Random: num_instances = ClimateNews.objects.all().count()
    # context = {'num_instances':num_instances}

    # This used to send the image and title information to template:
        #image = ClimateNews.objects.all()  
        #context = {'imageKey':image}
        #context = {'image':image[1],'title':image[1][1]}
        #return render(request, 'Labels_Nudges/list_news.html',context = context) # notice here we are adding 

        
def list_img(request):
    
    # this used to Random: num_instances = ClimateNews.objects.all().count()
    # context = {'num_instances':num_instances}

    # This used to send the image and title information to template:
        #image = ClimateNews.objects.all()  
        #context = {'imageKey':image}
        
        #return render(request, 'Labels_Nudges/list_news.html',context = context) # notice here we are adding         
    
    # This used to send the image and title information to template:
        newsAttributes = ClimateNews.objects.get(pk=2)
        newsList = [newsAttributes.id,newsAttributes.image_url]
        #context = {'image':image[1],'title':image[1][1]}
        return render(request, 'Labels_Nudges/list_img.html',context = {'newsList':newsList}) # notice here we are adding         
    #image = ClimateNews.objects.all()  

 
    #allnews = ClimateNews.objects.filter(category = type).values_list('title', flat=True)[:10]
 
    #return render(request, 'Labels_Nudges/list_news.html',context = allnews) # notice here we are adding 

# This function is for Jeng's testing code


    #user_data = models.ClimateNews.objects.all()
    #objects = ClimateNews.objects.filter(title=request.GET['title'])
    #return render(request, "list_news.html", context={'objects': objects})
    
    
    #all_news = []
    #for x in user_data:
        #all_news.append(x.title)
    #my_var = {'somelist':all_news}
    #return render(request,'Labels_Nudges/list_news.html', content = my_var)

def recipe_recommendations(request):

    # add rating of current user to rating matrix
    person = request.session['person_id']

    

    # extract the user input and food category
    
    real_user_input = FoodCategory.objects.filter(
        person_id = person
    ).values_list('category','recipe_popularity','calories','recipe_size','preparation_time','n_ingredient')

    user_category = real_user_input[0][0]
    
    # print(real_user_input)

    # Jeng: the code below is saving the user's cookies data from above to the dictionaries
    user_input_FoodKnowledge = {
        'Average Rating':float(real_user_input[0][1]), 
        'calories_kCal':float(real_user_input[0][2]), 
        'Servings':float(real_user_input[0][3]),
        'recipe_prep_time':float(real_user_input[0][4]), 
        '#ingredient':float(real_user_input[0][5])}
    
    healthyRecommendations_id = get_top_recommendations(user_input_FoodKnowledge, 'Healthy', user_category)
    
    UnhealthyRecommendations_id = get_top_recommendations(user_input_FoodKnowledge, 'Unhealthy', user_category)

    # print('-----------',healthyRecommendations_id)

    
    

    # get recommendation
    recom_size = 5
    htop_n_for_target_user = healthyRecommendations_id
    
    unhtop_n_for_target_user  = UnhealthyRecommendations_id
 
    id_h_recipes = [] 


    [id_h_recipes.append(int(i)) for i in htop_n_for_target_user]

    id_unh_recipes = []
    [id_unh_recipes.append(int(i)) for i in unhtop_n_for_target_user]

    print("top healthy recommendation------",htop_n_for_target_user)
    print("top unhealthy recommendation-------", unhtop_n_for_target_user)

#  Extract recipes


    # extract 5 healthy recipes
    h_0_recipe = HealthyRecipe.objects.get(id=id_h_recipes[0])
    h_1_recipe = HealthyRecipe.objects.get(id=id_h_recipes[1])
    h_2_recipe = HealthyRecipe.objects.get(id=id_h_recipes[2])
    h_3_recipe = HealthyRecipe.objects.get(id=id_h_recipes[3])
    h_4_recipe = HealthyRecipe.objects.get(id=id_h_recipes[4])
    # extract 5 unhhealthy recipes
    unh_0_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[0])
    unh_1_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[1])
    unh_2_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[2])
    unh_3_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[3])
    unh_4_recipe = UnhealthyRecipe.objects.get(id=id_unh_recipes[4])
    
    # selected recipe model
    selected_recipe = SelectedRecipe() 

    # initialise healthy forms with extracted data
    if request.method == "POST":
                # if the user already select a recipe
        person = request.session['person_id']
        user_selected = SelectedRecipe.objects.filter(person_id = person)
        if user_selected:
            SelectedRecipe.objects.filter(person_id=person).delete()

        user_selected = Recommendations.objects.filter(person_id = request.session['person_id'])
        if user_selected:
            Recommendations.objects.filter(person_id=request.session['person_id']).delete()


        # print('Request POST------------',request.POST)
        recipe_name = request.POST.get('recipe_name')
        recipe_id = request.POST.get('recipe_id')
        recipe_h  = request.POST.get('healthiness')

        if recipe_h == 'healthy':
            nutri__fsa = HealthyRecipe.objects.filter(id=recipe_id).values_list('Nutri_score','Fsa_new')
        else:
            nutri__fsa = UnhealthyRecipe.objects.filter(id=recipe_id).values_list('Nutri_score','Fsa_new')
        selected_recipe.Nutri_score = nutri__fsa[0][0]
        selected_recipe.fsa_score = nutri__fsa[0][1]
        selected_recipe.person_id= person
        selected_recipe.recipe_name = recipe_name
        selected_recipe.recipe_id = recipe_id
        selected_recipe.healthiness = recipe_h
        selected_recipe.session_id = request.session['session_id']
        selected_recipe.save()

             # save recommendations
        h_recommendations = Recommendations()
      
        h_recommendations.person_id = person
        h_recommendations.recommended_recipes = [h_0_recipe.id,h_1_recipe.id,h_2_recipe.id,h_3_recipe.id,h_4_recipe.id]
        h_recommendations.healthiness = 'Healthy'
        h_recommendations.save()

        unh_recommendations = Recommendations()
        
        unh_recommendations.person_id = person
        unh_recommendations.recommended_recipes = [unh_0_recipe.id,unh_1_recipe.id,unh_2_recipe.id,unh_3_recipe.id,unh_4_recipe.id]
        unh_recommendations.healthiness = 'Unhealthy'
        unh_recommendations.save()

        return redirect('Labels_Nudges:choice_evaluation')
    else:
      
        
        h_0 = [h_0_recipe.Name, id_h_recipes[0], 'healthy', h_0_recipe.image_link, int(float(h_0_recipe.calories_kCal)),
                                 int(float(h_0_recipe.Servings)),int(float(h_0_recipe.size_g) // float(h_0_recipe.Servings)), h_0_recipe.salt_g,h_0_recipe.sugar_g,h_0_recipe.fat_g,h_0_recipe.saturate_g]
        
        h_1 = [h_1_recipe.Name, id_h_recipes[1], 'healthy', h_1_recipe.image_link, int(float(h_1_recipe.calories_kCal)),
                                 int(float(h_1_recipe.Servings)),int(float(h_1_recipe.size_g) // float(h_1_recipe.Servings)), h_1_recipe.salt_g,h_1_recipe.sugar_g,h_1_recipe.fat_g,h_1_recipe.saturate_g]
        
        h_2 = [h_2_recipe.Name, id_h_recipes[2], 'healthy', h_2_recipe.image_link, int(float(h_2_recipe.calories_kCal)), 
                               int(float(h_2_recipe.Servings)),int(float(h_2_recipe.size_g) // float(h_2_recipe.Servings)), h_2_recipe.salt_g,h_2_recipe.sugar_g,h_2_recipe.fat_g,h_2_recipe.saturate_g]
        
        h_3 = [h_3_recipe.Name, id_h_recipes[3], 'healthy', h_3_recipe.image_link, int(float(h_3_recipe.calories_kCal)),
                                 int(float(h_3_recipe.Servings)),int(float(h_3_recipe.size_g) // float(h_3_recipe.Servings)), h_3_recipe.salt_g,h_3_recipe.sugar_g,h_3_recipe.fat_g,h_3_recipe.saturate_g]
        
        h_4 = [h_4_recipe.Name, id_h_recipes[4], 'healthy', h_4_recipe.image_link, int(float(h_4_recipe.calories_kCal)), 
                                int(float(h_4_recipe.Servings)),int(float(h_4_recipe.size_g) // float(h_4_recipe.Servings)), h_4_recipe.salt_g,h_4_recipe.sugar_g,h_4_recipe.fat_g,h_4_recipe.saturate_g]
        
        
     
        

        h_salt =[int(float(h_0_recipe.salt_count)),int(float(h_1_recipe.salt_count)),int(float(h_2_recipe.salt_count)),int(float(h_3_recipe.salt_count)),int(float(h_4_recipe.salt_count))]
        h_sugar = [int(float(h_0_recipe.sugar_count)),int(float(h_1_recipe.sugar_count)),int(float(h_2_recipe.sugar_count)), int(float(h_3_recipe.sugar_count)), int(float(h_4_recipe.sugar_count))]
        h_fat =[int(float(h_0_recipe.fat_count)), int(float(h_1_recipe.fat_count)), int(float(h_2_recipe.fat_count)),int(float(h_3_recipe.fat_count)),int(float(h_4_recipe.fat_count))]
        h_satfat =[ int(float(h_0_recipe.satfat_count)),int(float(h_1_recipe.satfat_count)),int(float(h_2_recipe.satfat_count)),int(float(h_3_recipe.satfat_count)), int(float(h_4_recipe.satfat_count))]


        salt_h = [mtl_color(h_salt),h_0[7], h_1[7], h_2[7], h_3[7], h_4[7]] 
        sugar_h = [ mtl_color(h_sugar),h_0[8],h_1[8], h_2[8], h_3[8], h_4[8]] 
        fat_h = [mtl_color(h_fat),h_0[9], h_1[9], h_2[9], h_3[9], h_4[9]] 
        satfat_h = [ mtl_color(h_satfat),h_0[10], h_1[10], h_2[10], h_3[10], h_4[10]]



        unh_0 = [unh_0_recipe.Name, id_unh_recipes[0], 'unhealthy', unh_0_recipe.image_link, int(float(unh_0_recipe.calories_kCal)), int(float(unh_0_recipe.Servings)),int(float(unh_0_recipe.size_g) // float(unh_0_recipe.Servings)),unh_0_recipe.salt_g,unh_0_recipe.sugar_g,unh_0_recipe.fat_g,unh_0_recipe.saturate_g]
       
        unh_1 = [unh_1_recipe.Name, id_unh_recipes[1], 'unhealthy', unh_1_recipe.image_link, int(float(unh_1_recipe.calories_kCal)),int(float(unh_1_recipe.Servings)),int(float(unh_1_recipe.size_g) // float(unh_1_recipe.Servings)),unh_1_recipe.salt_g,unh_1_recipe.sugar_g,unh_1_recipe.fat_g,unh_1_recipe.saturate_g]
       
        unh_2 = [unh_2_recipe.Name, id_unh_recipes[2], 'unhealthy', unh_2_recipe.image_link, int(float(unh_2_recipe.calories_kCal)), int(float(unh_2_recipe.Servings)),int(float(unh_3_recipe.size_g) // float(unh_3_recipe.Servings)),unh_2_recipe.salt_g,unh_2_recipe.sugar_g,unh_2_recipe.fat_g,unh_2_recipe.saturate_g]
       
        unh_3 = [unh_3_recipe.Name, id_unh_recipes[3], 'unhealthy', unh_3_recipe.image_link, int(float(unh_3_recipe.calories_kCal)), int(float(unh_3_recipe.Servings)),int(float(unh_3_recipe.size_g) // float(unh_3_recipe.Servings)),unh_3_recipe.salt_g,unh_3_recipe.sugar_g,unh_3_recipe.fat_g,unh_3_recipe.saturate_g]
       
        unh_4 = [unh_4_recipe.Name, id_unh_recipes[4], 'unhealthy', unh_4_recipe.image_link, int(float(unh_4_recipe.calories_kCal)), int(float(unh_4_recipe.Servings)),int(float(unh_4_recipe.size_g) // float(unh_4_recipe.Servings)),unh_4_recipe.salt_g,unh_4_recipe.sugar_g,unh_4_recipe.fat_g,unh_4_recipe.saturate_g]
        
    
        unh_salt =[int(float(unh_0_recipe.salt_count)),int(float(unh_1_recipe.salt_count)),int(float(unh_2_recipe.salt_count)),int(float(unh_3_recipe.salt_count)),int(float(unh_4_recipe.salt_count))]
        unh_sugar = [int(float(unh_0_recipe.sugar_count)),int(float(unh_1_recipe.sugar_count)),int(float(unh_2_recipe.sugar_count)), int(float(unh_3_recipe.sugar_count)), int(float(unh_4_recipe.sugar_count))]
        unh_fat =[int(float(unh_0_recipe.fat_count)), int(float(unh_1_recipe.fat_count)), int(float(unh_2_recipe.fat_count)),int(float(unh_3_recipe.fat_count)),int(float(unh_4_recipe.fat_count))]
        unh_satfat =[ int(float(unh_0_recipe.satfat_count)),int(float(unh_1_recipe.satfat_count)),int(float(unh_2_recipe.satfat_count)),int(float(unh_3_recipe.satfat_count)), int(float(unh_4_recipe.satfat_count))]
        
        


        salt_unh = [mtl_color(unh_salt),unh_0[7],unh_1[7],unh_2[7],unh_3[7],unh_4[7]] 
        sugar_unh = [ mtl_color(unh_sugar),unh_0[8],unh_1[8],unh_2[8],unh_3[8],unh_4[8]] 
        fat_unh = [mtl_color(unh_fat),unh_0[9],unh_1[9],unh_2[9],unh_3[9],unh_4[9]] 
        satfat_unh = [ mtl_color(unh_satfat),unh_0[10],unh_1[10],unh_2[10],unh_3[10],unh_4[10]] 

    # send forms
    return render(request,'Labels_Nudges/recipe_recommendations.html',context={'h_':htop_n_for_target_user, 
                                                'unh_':unhtop_n_for_target_user,
                                                'h_0':h_0,
                                                'h_1':h_1,
                                                'h_2':h_2,
                                                'h_3':h_3,
                                                'h_4':h_4,
                                                'unh_0':unh_0,
                                                'unh_1':unh_1,
                                                'unh_2':unh_2,
                                                'unh_3':unh_3,
                                                'unh_4':unh_4,
                                                'h_salt':salt_h,
                                                'h_sugar':sugar_h,
                                                'h_fat':fat_h,
                                                'h_satfat':satfat_h,
                                                'unh_salt':salt_unh,
                                                'unh_sugar':sugar_unh,
                                                'unh_fat':fat_unh,
                                                'unh_satfat':satfat_unh
   
                                                })

#size10 = len(ClimateNews.objects.all())
Sub_100Articals=[] 

Sub_100ArticalsDict= {}
#Sub_100Articals= sample(range(1, 101), 10)
#Sub_100Articals2=Sub_100Articals
print ("Globel Sub_100Articals be called:")
print (Sub_100Articals)
def choice_evaluation(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
   #size = len(ClimateNews.objects.all())
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
        
        #Sub_100ArticalsDict = {personDict: Sub_100Articals}
        print (' Back to choice_evaluation')
        print (' Sub_100ArticalsDict.update({personDict: Sub_100Articals}) be called:')
        if request.method == 'POST':
            print ("POST")
        else:
            Sub_100ArticalsDict.update({personDict: Sub_100Articals})
        print ('The Sub_100Articals now is:')
        print (Sub_100Articals)
        print ("After reset Sub_100Articals is:")
        #Sub_100ArticalsTemp = Sub_100Articals # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        #Sub_100Articals = []
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][0])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
       
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        i1 = Sub_100ArticalsDict[personDict][0]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i1)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')
    #EvaNews = EvaluateChoices()
    
    
    newsAttributes = ClimateNews.objects.get(pk=i1) # Jeng: Here to set the NEWS ID in this page
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date] # Jeng: Here to get NEWS dataset column for usage in template
    user_selected = EvaluateChoices.objects.filter(person_id = request.session['person_id'])
    #ChoiceEvaltion = EvaluateChoices()
         
    #ChoiceEvaltion.created = 'test'
    
    if user_selected:
        EvaluateChoices.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form = ChoiceEvaluationForm(request.POST)
        person = request.session['person_id']
        print (person)
        
        if evaluation_form.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation_ = evaluation_form.save(commit=False)
            evaluation_.person_id = person
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation_.session_id = request.session['prolific_id']
            evaluation_.created = i1
            evaluation_.save()
            
           
            #return redirect('Labels_Nudges:thank_u')
            return redirect('Labels_Nudges:choice_evaluation2')
    else:
         evaluation_form = ChoiceEvaluationForm()
         
    return render(request, 'Labels_Nudges/choice_evaluation.html', context={'eval_form': evaluation_form,'newsList':newsList})

def choice_evaluation2(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][1])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i2 below is:')
        i2 = Sub_100ArticalsDict[personDict][1]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i2)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')

    
   

    newsAttributes = ClimateNews.objects.get(pk=i2)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices2.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices2.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form2 = ChoiceEvaluationForm2(request.POST)
        person2 = request.session['person_id']
        print ('Person ID after post is'+ str(person2))
        ChoiceEvaltion2 = EvaluateChoices2()
        if evaluation_form2.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation2_ = evaluation_form2.save(commit=False)
            evaluation2_.person_id = person2
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation2_.session_id = request.session['prolific_id']
            evaluation2_.created = i2
            evaluation2_.save()
            return redirect('Labels_Nudges:choice_evaluation3')
    else:
         evaluation_form2 = ChoiceEvaluationForm2()
    return render(request, 'Labels_Nudges/choice_evaluation2.html', context={'eval_form': evaluation_form2,'newsList':newsList})











def choice_evaluation3(request):
    global Sub_100Articals
    global Sub_100ArticalsDict

    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The all Sub_100ArticalsDict below is:')
        print(Sub_100ArticalsDict)
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][2])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i3 below is:')
        i3 = Sub_100ArticalsDict[personDict][2]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i3)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')




    newsAttributes = ClimateNews.objects.get(pk=i3)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
 #try:   
    user_selected = EvaluateChoices3.objects.filter(person_id = request.session['person_id'])
    
    if user_selected:
        EvaluateChoices3.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form3 = ChoiceEvaluationForm3(request.POST)
        person3 = request.session['person_id']
        ChoiceEvaltion3 = EvaluateChoices3()
        if evaluation_form3.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation3_ = evaluation_form3.save(commit=False)
            evaluation3_.person_id = person3
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation3_.session_id = request.session['prolific_id']
            evaluation3_.created = i3
            evaluation3_.save()
            return redirect('Labels_Nudges:choice_evaluation4')
    else:
         evaluation_form3 = ChoiceEvaluationForm3()
    return render(request, 'Labels_Nudges/choice_evaluation3.html', context={'eval_form': evaluation_form3,'newsList':newsList})







def choice_evaluation4(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][3])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i4 below is:')
        i4 = Sub_100ArticalsDict[personDict][3]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i4)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')




    newsAttributes = ClimateNews.objects.get(pk=i4)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices4.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices4.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form4 = ChoiceEvaluationForm4(request.POST)
        person4 = request.session['person_id']
        ChoiceEvaltion4 = EvaluateChoices4()
        if evaluation_form4.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation4_ = evaluation_form4.save(commit=False)
            evaluation4_.person_id = person4
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation4_.session_id = request.session['prolific_id']
            evaluation4_.created = i4
            evaluation4_.save()
            return redirect('Labels_Nudges:choice_evaluation5')
    else:
         evaluation_form4 = ChoiceEvaluationForm4()
    return render(request, 'Labels_Nudges/choice_evaluation4.html', context={'eval_form': evaluation_form4,'newsList':newsList})












def choice_evaluation5(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][4])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i5 below is:')
        i5 = Sub_100ArticalsDict[personDict][4]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i5)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')




    newsAttributes = ClimateNews.objects.get(pk=i5)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices5.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices5.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form5 = ChoiceEvaluationForm5(request.POST)
        person5 = request.session['person_id']
        ChoiceEvaltion5 = EvaluateChoices5()
        if evaluation_form5.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation5_ = evaluation_form5.save(commit=False)
            evaluation5_.person_id = person5
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation5_.session_id = request.session['prolific_id']
            evaluation5_.created = i5
            evaluation5_.save()
            return redirect('Labels_Nudges:choice_evaluation6')
    else:
         evaluation_form5 = ChoiceEvaluationForm5()
    return render(request, 'Labels_Nudges/choice_evaluation5.html', context={'eval_form': evaluation_form5,'newsList':newsList})














def choice_evaluation6(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][5])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i6 below is:')
        i6 = Sub_100ArticalsDict[personDict][5]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i6)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')



    newsAttributes = ClimateNews.objects.get(pk=i6)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices6.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices6.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form6 = ChoiceEvaluationForm6(request.POST)
        person6 = request.session['person_id']
        ChoiceEvaltion6 = EvaluateChoices6()
        if evaluation_form6.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation6_ = evaluation_form6.save(commit=False)
            evaluation6_.person_id = person6
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation6_.session_id = request.session['prolific_id']
            evaluation6_.created = i6
            evaluation6_.save()
            return redirect('Labels_Nudges:choice_evaluation7')
    else:
         evaluation_form6 = ChoiceEvaluationForm6()
    return render(request, 'Labels_Nudges/choice_evaluation6.html', context={'eval_form': evaluation_form6,'newsList':newsList})











def choice_evaluation7(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][6])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i7 below is:')
        i7 = Sub_100ArticalsDict[personDict][6]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i7)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')



    newsAttributes = ClimateNews.objects.get(pk=i7)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices7.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices7.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form7 = ChoiceEvaluationForm7(request.POST)
        person7 = request.session['person_id']
        ChoiceEvaltion7 = EvaluateChoices7()
        if evaluation_form7.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation7_ = evaluation_form7.save(commit=False)
            evaluation7_.person_id = person7
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation7_.session_id = request.session['prolific_id']
            evaluation7_.created = i7
            evaluation7_.save()
            return redirect('Labels_Nudges:choice_evaluation8')
    else:
         evaluation_form7 = ChoiceEvaluationForm7()
    return render(request, 'Labels_Nudges/choice_evaluation7.html', context={'eval_form': evaluation_form7,'newsList':newsList})








def choice_evaluation8(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][7])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i8 below is:')
        i8 = Sub_100ArticalsDict[personDict][7]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i8)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')



    newsAttributes = ClimateNews.objects.get(pk=i8)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices8.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices8.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form8 = ChoiceEvaluationForm8(request.POST)
        person8 = request.session['person_id']
        ChoiceEvaltion8 = EvaluateChoices8()
        if evaluation_form8.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation8_ = evaluation_form8.save(commit=False)
            evaluation8_.person_id = person8
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation8_.session_id = request.session['prolific_id']
            evaluation8_.created = i8
            evaluation8_.save()
            return redirect('Labels_Nudges:choice_evaluation9')
    else:
         evaluation_form8 = ChoiceEvaluationForm8()
    return render(request, 'Labels_Nudges/choice_evaluation8.html', context={'eval_form': evaluation_form8,'newsList':newsList})











def choice_evaluation9(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
    
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][8])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i9 below is:')
        i9 = Sub_100ArticalsDict[personDict][8]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i9)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()
    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')



    newsAttributes = ClimateNews.objects.get(pk=i9)
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices9.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices9.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form9 = ChoiceEvaluationForm9(request.POST)
        person9 = request.session['person_id']
        ChoiceEvaltion9 = EvaluateChoices9()
        if evaluation_form9.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation9_ = evaluation_form9.save(commit=False)
            evaluation9_.person_id = person9
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation9_.session_id = request.session['prolific_id']
            evaluation9_.created = i9
            evaluation9_.save()
            return redirect('Labels_Nudges:choice_evaluation10')
    else:
         evaluation_form9 = ChoiceEvaluationForm9()
    return render(request, 'Labels_Nudges/choice_evaluation9.html', context={'eval_form': evaluation_form9,'newsList':newsList})














def choice_evaluation10(request):
    global Sub_100Articals
    global Sub_100ArticalsDict
    try:
        personDict = request.session['person_id'] # Jeng: Here is the person ID for the Dict and will to be the KEY in Sub_100ArticalsDict below
    
 
        #Sub_100ArticalsDict = {personDict: Sub_100Articals} # Jeng: Here I save the 10 news based on different person ID, KEY is person ID Value is 10 NEWS
        print ('The Sub_100ArticalsDict for this person ID below is:')
        print (Sub_100ArticalsDict[personDict])
        print ('The NEWS ID for this page is:')
        print (Sub_100ArticalsDict[personDict][9])
        print ('The Sub_100ArticalsDict for all is:')
        print (Sub_100ArticalsDict)
        #global size10
        print ('The Sub_100Articals below is:')
        print (Sub_100Articals)
        #Sub_100Articals= sample(range(1, 101), 10) # Set a global list involving random 10 news when this function is loaded, and preduce 10 sampling news for other functions from 100 datasets, to narrow down the scope.
        print ('The i10 below is:')
        i10 = Sub_100ArticalsDict[personDict][9]
        #i1 = Sub_100Articals[0]
        print ('The NEWS ID below is:')
        print (i10)
        print ('Person ID is'+ str(personDict))
        print ('The keys is:')
        print (Sub_100ArticalsDict.keys())
        #EvaNews = EvaluateChoices()

    except:
        print("An exception occurred")
        return redirect('Labels_Nudges:home')

    newsAttributes = ClimateNews.objects.get(pk=i10)
    
    newsList = [newsAttributes.id,newsAttributes.image_url,newsAttributes.title,newsAttributes.text,newsAttributes.author,newsAttributes.date]
    user_selected = EvaluateChoices10.objects.filter(person_id = request.session['person_id'])
    if user_selected:
        EvaluateChoices10.objects.filter(person_id=request.session['person_id']).delete()
  
    if request.method == 'POST':
        evaluation_form10 = ChoiceEvaluationForm10(request.POST)
        person10 = request.session['person_id']
        ChoiceEvaltion10 = EvaluateChoices10()
        if evaluation_form10.is_valid():
            # print("-----------here we are")
            # ChoiceEvaltion.person = request.session['person_id']
            evaluation10_ = evaluation_form10.save(commit=False)
            evaluation10_.person_id = person10
            # ChoiceEvaltion.person_id = evaluation_form.foriengkey
            evaluation10_.session_id = request.session['prolific_id']
            evaluation10_.created = i10
            evaluation10_.save()
            return redirect('Labels_Nudges:thank_u')
    else:
         evaluation_form10 = ChoiceEvaluationForm10()
    return render(request, 'Labels_Nudges/choice_evaluation10.html', context={'eval_form': evaluation_form10,'newsList':newsList})












def thank_u(request):

    global Sub_100Articals
     

    #Sub_100Articals=[] # This is used to reset the random 100 articles for next usage
    #print (Sub_100Articals)
    return render(request, 'Labels_Nudges/thanks.html', context={'session_id':request.session['session_id']})

def error_404(request,exception):
    data = {}
    return render(request, 'Labels_Nudges/404.html',data)
def error_500(request):
        data = {}
        return render(request,'Labels_Nudges/404.html', data)
