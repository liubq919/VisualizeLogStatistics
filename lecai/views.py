from .models import *
from .utilities import *
import json
import datetime
# Create your views here.


def get_all_api_info(request):

    date = get_date('1')
    if request.method == 'POST':
        if request.POST['type']:
            date = get_date(str(request.POST['type']))

    all_api_info_on_spec_day = AllApiInfo.objects(date=date).first()
    if all_api_info_on_spec_day:
        all_info_list = all_api_info_on_spec_day.info
        all_info_list_order_by_counter = sorted(all_info_list, key=lambda k: -k['counter'])

        ajax_data = {'date': date}
        pie_data_list = []

        if len(all_info_list_order_by_counter) > 10:
            all_api_counter = 0
            all_api_top_five_counter = 0
            for item in all_info_list_order_by_counter:
                if isinstance(item, ApiInfo):
                    all_api_counter += item.counter
                    # only add the first ten data
                    if len(pie_data_list) < 10:
                        api_info_dict = {}
                        api = item.api
                        counter = item.counter
                        api_info_dict['api'] = api
                        api_info_dict['counter'] = counter
                        pie_data_list.append(api_info_dict)
                        all_api_top_five_counter += counter
            api_info_others_dict = {
                'api': 'Others',
                'counter': all_api_counter - all_api_top_five_counter
            }
            pie_data_list.append(api_info_others_dict)
        else:
            for item in all_api_info_on_spec_day.info:
                if isinstance(item, ApiInfo):
                    api_info_dict = {}
                    api = item.api
                    counter = item.counter
                    api_info_dict['api'] = api
                    api_info_dict['counter'] = counter
                    pie_data_list.append(api_info_dict)
        ajax_data['info'] = pie_data_list
        return json.dumps(ajax_data)
    else:
        return json.dumps("")


# get api info on specific day
def get_every_fif_minutes_api_info_on_specifice_day(day_index):
    date = get_date(str(day_index))

    all_every_fifteen_minutes_info_on_spec_day = AllEveryFifteenMinutes.objects(date=date).first()
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


def index_ery_fif_min_ai_ajax_week_in_per_chart(request):
    all_each_fifteen_mins_api_info_list_with_sev_values = get_all_each_fifteen_mins_list_with_sev_values()
    sev_days_data_list = []
    for i in range(1, 8, 1):
        date_on_specific_day = get_every_fif_minutes_api_info_on_specifice_day(i)
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


def index_api_called_day_by_day(request):
    colors = ['#FF0F00', '#FF6600', '#FF9E01', '#F8FF01', '#FCD202', '#B0DE09', '#04D215', '#0D8ECF', '#0D52D1', '#2A0CD0', '#8A0CCF', '#CD0D74']

    date_info = "%s--%s" % (str(datetime.date.today() - datetime.timedelta(days=20)),
                            str(datetime.date.today() - datetime.timedelta(days=1)))

    ajax_data = []
    for i in range(1, 21, 1):
        api_called_times_on_spec_day = LecaiApiCounterInfo.objects(date=get_date(str(i))).first()
        if isinstance(api_called_times_on_spec_day, LecaiApiCounterInfo):
            data_dict_temp = {
                'time': api_called_times_on_spec_day.date[-5:].replace('-', '/', 1),
                'times': api_called_times_on_spec_day.times,
                'color': colors[(i - 1) % 12]
            }
            ajax_data.append(data_dict_temp)

    ajax_pre_week_date = {
        'date': date_info,
        'info': ajax_data
    }
    return json.dumps(ajax_pre_week_date)


def get_every_fif_minutes_login_count_on_specifice_day(day_index):

    date = get_date(str(day_index))

    all_every_fifteen_minutes_info_on_spec_day = AllEveryFifMinLoginCount.objects(date=date).first()
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


def index_ery_fif_login_count_ajax_week_in_per_chart(request):
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
        login_status_on_spec_day = LecaiLoginCountInfo.objects(date=get_date(str(i))).first()
        if isinstance(login_status_on_spec_day, LecaiLoginCountInfo):
            data_dict_temp = {
                'time': login_status_on_spec_day.date[-5:].replace('-', '/', 1),
                'times': login_status_on_spec_day.times,
                'color': colors[(i - 1) % 12]
            }
            ajax_data.append(data_dict_temp)

    ajax_pre_week_date = {
        'date': date_info,
        'info': ajax_data
    }
    return json.dumps(ajax_pre_week_date)


def index_login_distribution_provinces(request):
    date = get_date('1')
    if request.method == 'POST':
        if request.POST['type']:
            date = get_date(str(request.POST['type']))
    provinces_area_info_provinces_list = []
    provinces_area_info = EventLogProvincesAreaInfo.objects(date=date).first()
    if provinces_area_info and provinces_area_info.info:
        for item_province in provinces_area_info.info:
            if isinstance(item_province, EventLogProvincesArea):
                data_dict_temp = {
                    'name': item_province.name,
                    'value': item_province.value
                }
                provinces_area_info_provinces_list.append(data_dict_temp)

    provinces_area_info_provinces_list_by_value = sorted(provinces_area_info_provinces_list, key=lambda k: -k['value'])

    ajax_data = {
        'date': date,
        'provinces': provinces_area_info_provinces_list_by_value,
    }

    return json.dumps(ajax_data)


def index_login_distribution_cities(request):

    province = ''
    if request.method == 'POST':
        if request.POST['province']:
            province = request.POST['province']
    date = get_date('1')
    if request.method == 'POST':
        if request.POST['type']:
            date = get_date(str(request.POST['type']))

    provinces_area_info_cities_list = []
    if '' != province:
        provinces_area_info = EventLogProvincesAreaInfo.objects(date=date).first()
        for item_province in provinces_area_info.info:
            if isinstance(item_province, EventLogProvincesArea):
                if item_province.name == province:
                    for item_city in item_province.info:
                        if isinstance(item_city, EventLogCitiesArea):
                            data_dict_temp = {
                                'name': item_city.name,
                                'value': item_city.value
                            }
                            provinces_area_info_cities_list.append(data_dict_temp)

    provinces_area_info_cities_list_by_value = sorted(provinces_area_info_cities_list, key=lambda k: -k['value'])
    ajax_data = {
        'cities': provinces_area_info_cities_list_by_value,
    }
    return json.dumps(ajax_data)

