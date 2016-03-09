# encoding=utf-8
__author__ = 'liubq'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^qida_os_info/', views.get_qida_os_info, name='get_qida_os_info'),

    # login count in previous week in one chart
    url(r'^index_ery_fif_login_count_ajax_weekin_per_chart/', views.index_ery_fif_login_count_ajax_weekin_per_chart,
        name='index_ery_fif_login_count_ajax_weekin_per_chart'),

    # login count in previous week in one chart
    url(r'^index_login_count_day_by_day/', views.index_login_count_day_by_day,
        name='index_login_count_day_by_day'),

    # browser percentage
    url(r'^qida_browser_per/', views.get_qida_browser_per, name='get_qida_browser_per'),
]
