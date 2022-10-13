from django.contrib import admin
from django.db.models.base import Model
from .models import *
from .models import ClimateNews
# Register your models here.

import csv
from django.http import HttpResponse

from import_export.admin import ImportExportModelAdmin
from django import forms


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


def export_as_csv_action(description="Export selected objects as CSV file", fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

        # opts = modeladmin.model._meta
        # field_names = set([field.name for field in opts.fields])

        # if fields:
        #     fieldset = set(fields)
        #     field_names = field_names & fieldset

        # elif exclude:
        #     excludeset = set(exclude)
        #     field_names = field_names - excludeset

        # response = HttpResponse(content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        # writer = csv.writer(response)

        # if header:
        #     writer.writerow(list(field_names))
        # for obj in queryset:
        #     writer.writerow([str(getattr(obj, field)).encode("utf-8","replace") for field in field_names])

        # return response

    export_as_csv.short_description = description
    return export_as_csv



# @admin.register(Personal_info)
class Personal_infoAdmin(admin.ModelAdmin):
    list_display = ('id','session_id','created','age','gender','country','education')
    actions = [export_as_csv_action("CSV Export")]



# @admin.register(FoodCategory)    
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','person','session_id','category','recipe_popularity','calories','recipe_size','preparation_time','n_ingredient','created')
    actions = [export_as_csv_action("CSV Export")]


class HealthyRecipeAdmin(ImportExportModelAdmin):
    list_display = ('id','Name','category','Nutri_score','Fsa_new','NumberRatings')
    actions = [export_as_csv_action("CSV Export")]
class UnhealthyRecipeAdmin(ImportExportModelAdmin):
    list_display = ('id','Name','category','Nutri_score','Fsa_new','NumberRatings')
    actions = [export_as_csv_action("CSV Export")]

class ClimateNewsAdmin(ImportExportModelAdmin):
    list_display = ('id','article_url','title','author','type','category','subcategory','text'
                    ,'date','time','image_url','image_caption','author_bio','subtype')
    actions = [export_as_csv_action("CSV Export")]
    
class SelectedRecipeAdmin(admin.ModelAdmin):
    list_display = ('id','person','session_id','recipe_name','recipe_id','healthiness','Nutri_score','fsa_score','created')
    actions = [export_as_csv_action("CSV Export")]

class EvaluateChoicesAdmin(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','many_to_choose','created')
    actions = [export_as_csv_action("CSV Export")]

class EvaluateChoicesAdmin2(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]
#'sys_time','unders_sys','many_actions',,'many_to_choose','easy_choice','choice_overwhelming','know_many','prepare_recipes'

class EvaluateChoicesAdmin3(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]

class EvaluateChoicesAdmin4(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]

class EvaluateChoicesAdmin5(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]


class EvaluateChoicesAdmin6(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]


class EvaluateChoicesAdmin7(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]



class EvaluateChoicesAdmin8(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','many_to_choose','created')
    actions = [export_as_csv_action("CSV Export")]



class EvaluateChoicesAdmin9(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]


class EvaluateChoicesAdmin10(admin.ModelAdmin):
    list_display = ('id','person','session_id','liked_news','trust_news','fit_preference',
    'recommend_news','created')
    actions = [export_as_csv_action("CSV Export")]




class RecommedationsAdmin(admin.ModelAdmin):
    list_display = ('id','person','recommended_recipes','healthiness', 'created')
    actions = [export_as_csv_action("CSV Export")]



class Ghs_fkAdmin(admin.ModelAdmin):
    list_display = ('id','person','FK_1','FK_2','FK_3','FK_4','FK_5','FK_6','FK_7','FK_8','FK_9','FK_10','FK_11','FK_12')
    actions = [export_as_csv_action("CSV Export")]

admin.site.register(Ghs_fk,Ghs_fkAdmin)
admin.site.register(EvaluateChoices, EvaluateChoicesAdmin)
admin.site.register(EvaluateChoices2, EvaluateChoicesAdmin2)
admin.site.register(EvaluateChoices3, EvaluateChoicesAdmin3)
admin.site.register(EvaluateChoices4, EvaluateChoicesAdmin4)
admin.site.register(EvaluateChoices5, EvaluateChoicesAdmin5)
admin.site.register(EvaluateChoices6, EvaluateChoicesAdmin6)
admin.site.register(EvaluateChoices7, EvaluateChoicesAdmin7)
admin.site.register(EvaluateChoices8, EvaluateChoicesAdmin8)
admin.site.register(EvaluateChoices9, EvaluateChoicesAdmin9)
admin.site.register(EvaluateChoices10, EvaluateChoicesAdmin10)
admin.site.register(SelectedRecipe, SelectedRecipeAdmin)
admin.site.register(Personal_info, Personal_infoAdmin)
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(UnhealthyRecipe, UnhealthyRecipeAdmin)
admin.site.register(HealthyRecipe, HealthyRecipeAdmin)
admin.site.register(Recommendations, RecommedationsAdmin)
admin.site.register(ClimateNews, ClimateNewsAdmin)
# admin.site.register(user_rate, user_rateAdmin)
# admin.site.register(Recipes, RecipesAdmin)

# class RecipesAdmin(admin.ModelAdmin):
#     list_display = ('id','URL','Name','category','Size','Serving','Calories',
#     'image_link')
#     actions = [export_as_csv_action("CSV Export")]
# class user_ratingsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'person','Healthyrecipe','UnhealthyRecipe','recipe_rating','created')

# class user_rateAdmin(admin.ModelAdmin):
#     list_display = ('id', 'person','recipe','recipe_rating','created')



#https://personalizedrecipe2.herokuapp.com/