# encoding=utf-8
__author__ = 'liubq'

from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^all_api_info/', views.get_all_api_info, name='all_api_info'),

    # api count in previous week in one chart
    url(r'^index_ery_fif_min_ai_ajax_week_in_per_chart/', views.index_ery_fif_min_ai_ajax_week_in_per_chart,
        name='index_ery_fif_min_ai_ajax_week_in_per_chart'),

    # api count status in latest several days
    url(r'^index_api_called_day_by_day/', views.index_api_called_day_by_day,
        name='index_api_called_day_by_day'),

    # login count in previous week in one chart
    url(r'^index_ery_fif_login_count_ajax_week_in_per_chart/', views.index_ery_fif_login_count_ajax_week_in_per_chart,
        name='index_ery_fif_login_count_ajax_week_in_per_chart'),

    # login status in latest several days
    url(r'^index_login_count_day_by_day/', views.index_login_count_day_by_day,
        name='index_login_count_day_by_day'),

    url(r'^index_login_distribution_provinces/', views.index_login_distribution_provinces,
        name='index_login_distribution_provinces'),

    url(r'^index_login_distribution_cities/', views.index_login_distribution_cities,
        name='index_login_distribution_cities'),
]
