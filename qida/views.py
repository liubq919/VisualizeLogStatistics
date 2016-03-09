from django.shortcuts import render
from .models import *
from utilities import *
import json
import datetime

# Create your views here.


def get_qida_os_info(request):

    date = get_date('1')
    if request.method == 'POST':
        if request.POST['type']:
            date = get_date(str(request.POST['type']))

    ajax_data = {'date': date}
    qida_os_info_on_spec_day = QidaOSInfo.objects(date=date).first()
    if qida_os_info_on_spec_day and isinstance(qida_os_info_on_spec_day, QidaOSInfo):
        pie_data_list = []
        windowsxp = qida_os_info_on_spec_day.windowsxp
        api_info_dict_windowsxp = {
            'os': 'WinXP',
            'counter': windowsxp
        }
        windowsvista = qida_os_info_on_spec_day.windowsvista
        api_info_dict_windowsvista = {
            'os': 'WinVista',
            'counter': windowsvista
        }
        windows7 = qida_os_info_on_spec_day.windows7
        api_info_dict_windows7 = {
            'os': 'Win7',
            'counter': windows7
        }
        windows8 = qida_os_info_on_spec_day.windows8
        # api_info_dict_windows8 = {
        #     'os': 'Win8',
        #     'counter': windows8
        # }
        windows8_1 = qida_os_info_on_spec_day.windows8_1
        # api_info_dict_windows8_1 = {
        #     'os': 'Win8_1',
        #     'counter': windows8_1
        # }
        api_info_dict_windows8_1_or_windows8 = {
            'os': 'Win8/8.1',
            'counter': windows8 + windows8_1
        }
        windows10 = qida_os_info_on_spec_day.windows10
        api_info_dict_windows10 = {
            'os': 'Win10',
            'counter': windows10
        }
        windows_others = qida_os_info_on_spec_day.windowsOthers
        api_info_dict_windows_others = {
            'os': 'WinOthers',
            'counter': windows_others
        }
        osx = qida_os_info_on_spec_day.osx
        api_info_dict_osx = {
            'os': 'OSX',
            'counter': osx
        }
        # mobile/tablet os
        iphone = qida_os_info_on_spec_day.iPhone
        # api_info_dict_iphone = {
        #     'os': 'iPhone',
        #     'counter': iphone
        # }

        ipad = qida_os_info_on_spec_day.iPad
        # api_info_dict_ipad = {
        #     'os': 'iPad',
        #     'counter': ipad
        # }
        api_info_dict_apple_mob = {
            'os': 'iPad/iPhone',
            'counter': iphone + ipad
        }
        android = qida_os_info_on_spec_day.android
        api_info_dict_android = {
            'os': 'android',
            'counter': android
        }
        # other os
        others = qida_os_info_on_spec_day.osOthers
        api_info_others = {
            'os': 'Others',
            'counter': others
        }

        # pie_data_list.append(api_info_dict_windows)
        pie_data_list.append(api_info_dict_windowsxp)
        pie_data_list.append(api_info_dict_windowsvista)
        pie_data_list.append(api_info_dict_windows7)
        # pie_data_list.append(api_info_dict_windows8)
        # pie_data_list.append(api_info_dict_windows8_1)
        pie_data_list.append(api_info_dict_windows8_1_or_windows8)
        pie_data_list.append(api_info_dict_windows10)
        pie_data_list.append(api_info_dict_windows_others)
        pie_data_list.append(api_info_dict_osx)
        # pie_data_list.append(api_info_dict_iphone)
        # pie_data_list.append(api_info_dict_ipad)
        pie_data_list.append(api_info_dict_apple_mob)
        pie_data_list.append(api_info_dict_android)
        # pie_data_list.append(api_info_others)

        # ajax_data['info'] = sorted(pie_data_list, key=lambda k: -k['counter'])
        pie_data_list = sorted(pie_data_list, key=lambda k: -k['counter'])
        pie_data_list.append(api_info_others)
        ajax_data['info'] = pie_data_list
    return json.dumps(ajax_data)


def get_every_fif_minutes_login_count_on_specifice_day(day_index):

    date = get_date(str(day_index))

    all_every_fifteen_minutes_info_on_spec_day = QidaEveryFifMinLoginCount.objects(date=date).first()
    if all_every_fifteen_minutes_info_on_spec_day and all_every_fifteen_minutes_info_on_spec_day.info:
        ajax_data = {'date': date}
        column_data_list = []
        for item in all_every_fifteen_minutes_info_on_spec_day.info:
            if isinstance(item, EveryFifteenMinutes):
                hour = item.hour
                if hour <= 9:
                    hour = "0%d" % hour

                time_00 = "%s-00" % str(hour)
                time_15 = "%s-15" % str(hour)
                time_30 = "%s-30" % str(hour)
                time_45 = "%s-45" % str(hour)

                data_dict_00 = {
                    "time": time_00,
                    "value": item.counter1
                }
                column_data_list.append(data_dict_00)

                data_dict_15 = {
                    "time": time_15,
                    "value": item.counter2
                }
                column_data_list.append(data_dict_15)

                data_dict_30 = {
                    "time": time_30,
                    "value": item.counter3
                }
                column_data_list.append(data_dict_30)

                data_dict_45 = {
                    "time": time_45,
                    "value": item.counter4
                }
                column_data_list.append(data_dict_45)

        ajax_data['info'] = column_data_list
        return ajax_data
    else:
        return ""


def index_ery_fif_login_count_ajax_weekin_per_chart(request):
    all_each_fifteen_mins_api_info_list_with_sev_values = get_all_each_fifteen_mins_list_with_sev_values()
    sev_days_data_list = []
    for i in range(1, 8, 1):
        date_on_specific_day = get_every_fif_minutes_login_count_on_specifice_day(i)
        sev_days_data_list.append(date_on_specific_day)

    for index in range(0, 96, 1):
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value1'] += sev_days_data_list[0]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value2'] += sev_days_data_list[1]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value3'] += sev_days_data_list[2]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value4'] += sev_days_data_list[3]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value5'] += sev_days_data_list[4]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value6'] += sev_days_data_list[5]['info'][index]['value']
        all_each_fifteen_mins_api_info_list_with_sev_values[index]['value7'] += sev_days_data_list[6]['info'][index]['value']

    date_info = "%s--%s" % (str(datetime.date.today() - datetime.timedelta(days=7)),
                            str(datetime.date.today() - datetime.timedelta(days=1)))

    ajax_all_data_latest_week = {
        'date': date_info,
        'info': all_each_fifteen_mins_api_info_list_with_sev_values
    }
    return json.dumps(ajax_all_data_latest_week)


def index_login_count_day_by_day(request):
    colors = ['#FF0F00', '#FF6600', '#FF9E01', '#F8FF01', '#FCD202', '#B0DE09', '#04D215', '#0D8ECF', '#0D52D1', '#2A0CD0', '#8A0CCF', '#CD0D74']

    date_info = "%s--%s" % (str(datetime.date.today() - datetime.timedelta(days=20)),
                            str(datetime.date.today() - datetime.timedelta(days=1)))

    ajax_data = []
    for i in range(1, 21, 1):
        login_times_on_spec_day = QidaLoginCount.objects(date=get_date(str(i))).first()
        if isinstance(login_times_on_spec_day, QidaLoginCount):
            data_dict_temp = {
                'time': login_times_on_spec_day.date[-5:].replace('-', '/', 1),
                'times': login_times_on_spec_day.times,
                'color': colors[(i - 1) % 12]
            }
            ajax_data.append(data_dict_temp)

    ajax_pre_week_date = {
        'date': date_info,
        'info': ajax_data
    }
    return json.dumps(ajax_pre_week_date)


def get_qida_browser_per(request):
    date = get_date('1')
    if request.method == 'POST':
        if request.POST['type']:
            date = get_date(str(request.POST['type']))

    ajax_data = {'date': date}
    qida_browser_info_on_spec_day = QidaBrowserInfo.objects(date=date).first()
    if qida_browser_info_on_spec_day and isinstance(qida_browser_info_on_spec_day, QidaBrowserInfo):
        pie_data_list = []
        api_info_dict_ie6 = {
            'browser': 'IE6',
            'counter': qida_browser_info_on_spec_day.ie6
        }
        api_info_dict_ie7 = {
            'browser': 'IE7',
            'counter': qida_browser_info_on_spec_day.ie7
        }
        api_info_dict_ie8 = {
            'browser': 'IE8',
            'counter': qida_browser_info_on_spec_day.ie8
        }
        api_info_dict_ie9 = {
            'browser': 'IE9',
            'counter': qida_browser_info_on_spec_day.ie9
        }
        api_info_dict_ie10 = {
            'browser': 'IE10',
            'counter': qida_browser_info_on_spec_day.ie10
        }
        api_info_dict_ie11 = {
            'browser': 'IE11',
            'counter': qida_browser_info_on_spec_day.ie11
        }
        api_info_dict_edge = {
            'browser': 'Edge',
            'counter': qida_browser_info_on_spec_day.edge
        }
        api_info_dict_firefox = {
            'browser': 'Firefox',
            'counter': qida_browser_info_on_spec_day.firefox
        }
        api_info_dict_chrome = {
            'browser': 'Chrome',
            'counter': qida_browser_info_on_spec_day.chrome
        }
        api_info_dict_safari = {
            'browser': 'Safari',
            'counter': qida_browser_info_on_spec_day.safari
        }
        api_info_dict_others = {
            'browser': 'Others',
            'counter': qida_browser_info_on_spec_day.others
        }

        pie_data_list.append(api_info_dict_ie6)
        pie_data_list.append(api_info_dict_ie7)
        pie_data_list.append(api_info_dict_ie8)
        pie_data_list.append(api_info_dict_ie9)
        pie_data_list.append(api_info_dict_ie10)
        pie_data_list.append(api_info_dict_ie11)
        pie_data_list.append(api_info_dict_edge)
        pie_data_list.append(api_info_dict_firefox)
        pie_data_list.append(api_info_dict_chrome)
        pie_data_list.append(api_info_dict_safari)

        pie_data_list = sorted(pie_data_list, key=lambda k: -k['counter'])
        pie_data_list.append(api_info_dict_others)
        ajax_data['info'] = pie_data_list
    return json.dumps(ajax_data)
