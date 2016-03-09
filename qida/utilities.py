from models import *
import datetime
__author__ = 'liubq'


def get_all_each_fifteen_mins_list():
    all_each_fif_mins_api_info_list = []
    for i in range(0, 24, 1):
        hour = i
        if hour <= 9:
            hour = "0%d" % hour
        time_00 = "%s-00" % str(hour)
        data_dict_00 = {
            "time": time_00,
            "value": 0
        }
        time_15 = "%s-15" % str(hour)
        data_dict_15 = {
            "time": time_15,
            "value": 0
        }
        time_30 = "%s-30" % str(hour)
        data_dict_30 = {
            "time": time_30,
            "value": 0
        }
        time_45 = "%s-45" % str(hour)
        data_dict_45 = {
            "time": time_45,
            "value": 0
        }

        all_each_fif_mins_api_info_list.append(data_dict_00)
        all_each_fif_mins_api_info_list.append(data_dict_15)
        all_each_fif_mins_api_info_list.append(data_dict_30)
        all_each_fif_mins_api_info_list.append(data_dict_45)

    return all_each_fif_mins_api_info_list


def get_date(index='1'):

    return str(datetime.date.today() - datetime.timedelta(days=int(index)))


# get a list that contains 96 dict which consists of time and seven values(from value1 to value7)
# eg:
# [
#     {
#         "value7": 0,
#         "value6": 0,
#         "value5": 0,
#         "value4": 0,
#         "value3": 0,
#         "value2": 0,
#         "value1": 0,
#         "time": "00-00"
#     },
#     {
#         "value7": 0,
#         "value6": 0,
#         "value5": 0,
#         "value4": 0,
#         "value3": 0,
#         "value2": 0,
#         "value1": 0,
#         "time": "00-15"
#     },
#     ...
#     {
#         "value7": 0,
#         "value6": 0,
#         "value5": 0,
#         "value4": 0,
#         "value3": 0,
#         "value2": 0,
#         "value1": 0,
#         "time": "23-45"
#     }
# ]
def get_all_each_fifteen_mins_list_with_sev_values():
    all_each_fif_mins_api_info_list = []
    for i in range(0, 24, 1):
        hour = i
        if hour <= 9:
            hour = "0%d" % hour
        time_00 = "%s-00" % str(hour)
        data_dict_00 = {
            "time": time_00,
            "value1": 0,
            "value2": 0,
            "value3": 0,
            "value4": 0,
            "value5": 0,
            "value6": 0,
            "value7": 0
        }
        time_15 = "%s-15" % str(hour)
        data_dict_15 = {
            "time": time_15,
            "value1": 0,
            "value2": 0,
            "value3": 0,
            "value4": 0,
            "value5": 0,
            "value6": 0,
            "value7": 0
        }
        time_30 = "%s-30" % str(hour)
        data_dict_30 = {
            "time": time_30,
            "value1": 0,
            "value2": 0,
            "value3": 0,
            "value4": 0,
            "value5": 0,
            "value6": 0,
            "value7": 0
        }
        time_45 = "%s-45" % str(hour)
        data_dict_45 = {
            "time": time_45,
            "value1": 0,
            "value2": 0,
            "value3": 0,
            "value4": 0,
            "value5": 0,
            "value6": 0,
            "value7": 0
        }

        all_each_fif_mins_api_info_list.append(data_dict_00)
        all_each_fif_mins_api_info_list.append(data_dict_15)
        all_each_fif_mins_api_info_list.append(data_dict_30)
        all_each_fif_mins_api_info_list.append(data_dict_45)

    return all_each_fif_mins_api_info_list
