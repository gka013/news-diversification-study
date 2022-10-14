from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import ChoicesMeta
from django.db.models.fields import AutoField, CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from .choices import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.


class Personal_info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='Personal_info')

    created = models.DateTimeField(auto_now_add=True)
    #created = models.DateTimeField(default=timezone.now)

    age = models.CharField(max_length=120,
                           choices=Age_choices,
                           verbose_name='age',
                           default=None,
                           blank=False
                           )

    country = CountryField(blank_label='')

    education = models.CharField(max_length=120,
                                 choices=EducationLevel,
                                 verbose_name='education',
                                 default=None,
                                 blank=False

                                 )


    gender = models.CharField(max_length=300,
                              choices=Gender_choices,
                              verbose_name='gender',
                              default=None,
                              blank=False
                              )




    # other_diet = models.CharField(("other_diet"), max_length=50, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'personal_info'
        ordering = ['id']
        db_table = 'personal_info'

    def __str__(self):
        return "{}".format(self.id)



class Ghs_fk(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50,
		editable=False,
                default='Knowledge health')


    person = models.ForeignKey(
        Personal_info,
        on_delete = models.CASCADE
    )

    FK_1 = models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_1',
                            default = None,
                            blank = False)
    FK_2 = models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_2',
                            default = None,
                            blank = False)
    FK_3 = models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_3',
                            default = None,
                            blank =False)
    FK_4 =  models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_4',
                            default=None,
                            blank = False)
    FK_5 =  models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_5',
                            default=None,
                            blank = False)
    FK_6 =  models.CharField(max_length = 300,
                            choices = FK__choices,
                            verbose_name = 'FK_6',
                            default=None,
                            blank = False)
    FK_7 =  models.CharField(max_length = 300,
                        choices = FK__choices,
                            verbose_name = 'FK_7',
                            default=None,
                            blank = False)
    FK_8 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_8',
                             default=None,
                             blank = False)
    FK_9 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_9',
                             default=None,
                             blank = False)
    FK_10 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_10',
                             default=None,
                             blank = False)
    FK_11 =  models.CharField(max_length = 300,
                             choices = FK__choices,
                             verbose_name = 'FK_11',
                             default=None,
                             blank = False)
    FK_12 = models.CharField(max_length = 300,
 			    choices = FK__choices,
			  verbose_name = 'FK_12',
			default = None,
			blank = False)
	
    session_id = models.CharField(max_length = 100, blank=False, default = None)
    class Meta:
            verbose_name = 'Ghs_fk'
            ordering = ['id']
            db_table = 'ghs_fk'
    
    def __str__(self):
    	return "{}".format(self.id)


    
    
                            


class FoodCategory(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    category = models.CharField(("Category"),
                                max_length=50,
                                choices=foodCategories,
                                blank=False,
                                default=None)
    
    recipe_popularity = models.CharField(("recipe_popularity"),
                                max_length=50,
                                # choices=likert_scale,
                                blank=False,
                                default=None)
    
    calories = models.IntegerField(
                                   validators=[MinValueValidator(200),
                                    MaxValueValidator(1000),], )
    
    
    recipe_size = models.IntegerField(
                                   validators=[MinValueValidator(1),
                                    MaxValueValidator(10),], )

    preparation_time = models.IntegerField(
                                   validators=[MinValueValidator(15),
                                    MaxValueValidator(60),], )
    
    n_ingredient = models.IntegerField(
                                   validators=[MinValueValidator(3),
                                    MaxValueValidator(10),], )


    created = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'FoodCategory'
        ordering = ['id']
        db_table = 'FoodCategory'



class HealthyRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    URL = models.CharField(max_length=300)
    Name = models.CharField( max_length=500)
    fiber_g = models.CharField( max_length=50)
    sodium_g = models.CharField( max_length=50)
    carbohydrates_g= models.CharField(max_length=50)
    fat_g = models.CharField(max_length=50)
    protein_g = models.CharField(max_length=50)
    sugar_g= models.CharField( max_length=50)
    saturate_g = models.CharField(max_length=50)
    size_g = models.CharField( max_length=50)
    Servings = models.CharField( max_length=50)
    calories_kCal =  models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    image_link = models.CharField( max_length=500)
    fat_100g = models.CharField( max_length=50)
    fiber_100g = models.CharField(max_length=50)
    sugar_100g = models.CharField( max_length=50)
    saturated_100g = models.CharField( max_length=50)
    protien_100g = models.CharField( max_length=50)
    sodium_100mg = models.CharField(max_length=50)
    carbohydrates_100g = models.CharField(max_length=50)
    kj_100g = models.CharField( max_length=50)
    Nutri_score  = models.CharField( max_length=50)
    Fsa_new = models.CharField( max_length=50)
    salt_100g = models.CharField(max_length=50)
    salt_g = models.CharField(max_length=50)
    fat_count = models.CharField(max_length=50)
    satfat_count = models.CharField(max_length=50)
    sugar_count = models.CharField(max_length=50)
    salt_count = models.CharField(max_length=50)
    NumberRatings = models.IntegerField()
    class Meta:
        verbose_name = 'HealthyRecipe'
        ordering = ['id']
        db_table = 'HealthyRecipe'
    def __str__(self):
        return self.Name

class UnhealthyRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    URL = models.CharField(max_length=300)
    Name = models.CharField( max_length=500)
    fiber_g = models.CharField( max_length=50)
    sodium_g = models.CharField( max_length=50)
    carbohydrates_g= models.CharField(max_length=50)
    fat_g = models.CharField(max_length=50)
    protein_g = models.CharField(max_length=50)
    sugar_g= models.CharField( max_length=50)
    saturate_g = models.CharField(max_length=50)
    size_g = models.CharField( max_length=50)
    Servings = models.CharField( max_length=50)
    calories_kCal =  models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    image_link = models.CharField( max_length=500)
    fat_100g = models.CharField( max_length=50)
    fiber_100g = models.CharField(max_length=50)
    sugar_100g = models.CharField( max_length=50)
    saturated_100g = models.CharField( max_length=50)
    protien_100g = models.CharField( max_length=50)
    sodium_100mg = models.CharField(max_length=50)
    carbohydrates_100g = models.CharField(max_length=50)
    kj_100g = models.CharField( max_length=50)
    Nutri_score  = models.CharField( max_length=50)
    Fsa_new = models.CharField( max_length=50)
    salt_100g = models.CharField(max_length=50)
    salt_g = models.CharField(max_length=50)
    fat_count = models.CharField(max_length=50)
    satfat_count = models.CharField(max_length=50)
    sugar_count = models.CharField(max_length=50)
    salt_count = models.CharField(max_length=50)
    NumberRatings = models.IntegerField()
    class Meta:
        verbose_name = 'UnhealthyRecipe'
        ordering = ['id']
        db_table = 'UnhealthyRecipe'
    def __str__(self):
        return self.Name
	
class ClimateNews(models.Model):
    id = models.AutoField(primary_key=True)
    article_url = models.CharField(max_length=50000,default="Some String")
    title = models.CharField( max_length=50000,default="Some String")
    author = models.CharField( max_length=10000,default="Some String")
    type = models.CharField( max_length=50000,default="Some String")
    category = models.CharField( max_length=50000,default="Some String")
    subcategory = models.CharField(max_length=10000,default="Some String")
    text = models.CharField(max_length=40000,default="Some String")
    date = models.CharField(max_length=10000,default="Some String")
    time = models.CharField(max_length=10000,default="Some String")
    image_url = models.CharField(max_length=50000,default="Some String")
    image_caption = models.CharField(max_length=10000,default="Some String")
    author_bio = models.CharField(max_length=10000,default="Some String")
    subtype = models.CharField(max_length=10000,default="Some String")

    class Meta:
        verbose_name = 'ClimateNews'
        ordering = []
        db_table = 'ClimateNews'

    def __str__(self):
        return self.title

    #def __str__(self):
		    #return "{} {}".format(self.title, self.image_url)
            

            #This used to sent the image and title to view
            #return f"News title is {self.title} image link is {self.image_url}"

    
   
class Recommendations(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE)
    recommended_recipes = models.CharField(max_length=500)
    healthiness = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)




class SelectedRecipe(models.Model):
    id = models.AutoField(primary_key = True)

    person = models.ForeignKey(
        Personal_info,
        blank=False,
        on_delete=models.CASCADE
    )  
    recipe_id = models.IntegerField()  # recipe id that will be saved only
    recipe_name = models.CharField(max_length=200)

    Nutri_score = models.CharField(max_length= 100)
    fsa_score = models.CharField(max_length=100)

    healthiness = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100, blank=False, default=None)
    def __str__(self):
        return self.healthiness
    class Meta:
        unique_together = ('person','recipe_id')
        verbose_name = 'selectedRecipe'
        db_table  ='selectedrecipe'


class EvaluateChoices(models.Model):
    id = models.AutoField(primary_key=True)
    #news_id = models.IntegerField(default=None)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news',
        default=None,
        blank=False
    )

    

#--- choice difficulty-------
    
    many_to_choose = models.CharField(max_length=100,
        choices=FK__choices2,
        verbose_name='many_to_choose',
        default=None,
        blank=False
    )
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    #newsID = models.IntegerField(default=None)
    class Meta:
        verbose_name = 'EvaluateChoices'
        ordering = ['id']
        db_table = 'EvaluateChoices'

    def __str__(self):
        return "{}".format(self.id)






class EvaluateChoices2(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices2')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news2',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news2',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference2',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news2',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices2'
        ordering = ['id']
        db_table = 'EvaluateChoices2'

    def __str__(self):
        return "{}".format(self.id)


class EvaluateChoices3(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices3')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news3',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news3',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference3',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news3',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices3'
        ordering = ['id']
        db_table = 'EvaluateChoices3'

    def __str__(self):
        return "{}".format(self.id)




class EvaluateChoices4(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices4')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news4',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news4',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference4',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news4',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices4'
        ordering = ['id']
        db_table = 'EvaluateChoices4'

    def __str__(self):
        return "{}".format(self.id)



class EvaluateChoices5(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices5')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news5',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news5',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference5',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news5',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices5'
        ordering = ['id']
        db_table = 'EvaluateChoices5'

    def __str__(self):
        return "{}".format(self.id)





class EvaluateChoices6(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices6')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news6',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news6',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference6',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news6',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices6'
        ordering = ['id']
        db_table = 'EvaluateChoices6'

    def __str__(self):
        return "{}".format(self.id)

















class EvaluateChoices7(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices7')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news7',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news7',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference7',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news7',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices7'
        ordering = ['id']
        db_table = 'EvaluateChoices7'

    def __str__(self):
        return "{}".format(self.id)

















class EvaluateChoices8(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices8')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news8',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news8',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference8',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news8',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    many_to_choose = models.CharField(max_length=100,
        choices=FK__choices2,
        verbose_name='many_to_choose',
        default=None,
        blank=False
    )
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices8'
        ordering = ['id']
        db_table = 'EvaluateChoices8'

    def __str__(self):
        return "{}".format(self.id)











class EvaluateChoices9(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices9')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news9',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news9',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference9',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news9',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices9'
        ordering = ['id']
        db_table = 'EvaluateChoices9'

    def __str__(self):
        return "{}".format(self.id)














class EvaluateChoices10(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(
        max_length=50,
        editable=False,
        default='EvaluateChoices10')

    person = models.ForeignKey(
        Personal_info,
        on_delete=models.CASCADE
    )

    liked_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='liked_news10',
        default=None,
        blank=False
    )
    trust_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='trust_news10',
        default=None,
        blank=False
    )
    fit_preference = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='fit_preference10',
        default=None,
        blank=False
    )
    #know_many = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='know_many',
        #default=None,
        #blank=False
    #)
    recommend_news = models.CharField(max_length=100,
        choices=FK__choices,
        verbose_name='recommend_news10',
        default=None,
        blank=False
    )

#--- choice difficulty-------
    
    #many_to_choose = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='many_to_choose',
       # default=None,
        #blank=False
    #)
   #easy_choice = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='easy_choice',
        #default=None,
        #blank=False
    #)
    #choice_overwhelming = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='choice_overwhelming',
        #default=None,
        #blank=False
    #)
    
    # --- system effort
    #sys_time = models.CharField(max_length=100,
        #choices=FK__choices,
        #verbose_name='sys_time',
        #default=None,
        #blank=False
    #)
    #unders_sys = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='unders_sys',
    #default=None,
    #blank=False
    #)
    #many_actions = models.CharField(max_length=100,
    #choices=FK__choices,
    #verbose_name='many_actions',
    #default=None,
    #blank=False
    #)
    





    #created = models.DateTimeField(auto_now_add=True)
    created = models.CharField(max_length=1000, blank=False, default='0')
    session_id = models.CharField(max_length=100, blank=False, default=None)
    class Meta:
        verbose_name = 'EvaluateChoices10'
        ordering = ['id']
        db_table = 'EvaluateChoices10'

    def __str__(self):
        return "{}".format(self.id)
















# class user_rate(models.Model):
#     id = models.AutoField(primary_key=True)
#     person = models.ForeignKey(
#         Personal_info,
#         blank=False,
#         on_delete=models.CASCADE
#     )
#     recipe = models.ForeignKey(
#         Recipes,
#         # blank=False,
#         on_delete=models.CASCADE
#     )

#     recipe_rating = models.IntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(5)], blank=False, default=0)

#     created = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return self.recipe.id
#     class Meta:
#         unique_together = (('recipe','person'))
#         verbose_name = 'user_rate'
#         db_table = 'user_ratings'
