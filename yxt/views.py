from django.shortcuts import render
from django.conf import settings
from collections import OrderedDict
import os
import json
# Create your views here.


def index(request):
    try:
        menu_file = os.path.join(settings.STATIC_ROOT, 'yxt/js/yxt/menu.json')
        json_file = json.load(file(menu_file), object_pairs_hook=OrderedDict)
    except Exception as e:
        print "Error occurred when loading menu.json, %s" % e

    # this list contains all menus
    all_menus_list = []
    # generate menus
    try:
        for keys_lev1 in json_file.keys():
            menu_type = json_file[keys_lev1]["type"].encode("utf-8")
            menus_list = []
            for keys_lev2 in json_file[keys_lev1].keys():
                key_temp = keys_lev2.encode("utf-8")
                if key_temp != 'type':
                    menu_info_dict = {
                        "id": json_file[keys_lev1][keys_lev2]["id"].encode("utf-8"),
                        "name_ch": json_file[keys_lev1][keys_lev2]["name"].encode("utf-8"),
                        "name": keys_lev2.encode("utf-8")
                    }
                    menus_list.append(menu_info_dict)
            menus_dict = {
                "type": keys_lev1.encode("utf-8"),
                "name": menu_type,
                "menus": menus_list
            }
            all_menus_list.append(menus_dict)
    except Exception as e:
        print "Error occurred when parsing menu.json, %s" % e
    return render(request, 'yxt/index.html', {"all_menus_list": all_menus_list})


def dist(request):
    try:
        menu_file = os.path.join(settings.STATIC_ROOT, 'yxt/js/yxt/dist_menu.json')
        json_file = json.load(file(menu_file), object_pairs_hook=OrderedDict)
    except Exception as e:
        print "Error occurred when loading menu.json, %s" % e

    # this list contains all menus
    all_menus_list = []
    # generate menus
    try:
        for keys_lev1 in json_file.keys():
            menu_type = json_file[keys_lev1]["type"].encode("utf-8")
            menus_list = []
            for keys_lev2 in json_file[keys_lev1].keys():
                key_temp = keys_lev2.encode("utf-8")
                if key_temp != 'type':
                    menu_info_dict = {
                        "id": json_file[keys_lev1][keys_lev2]["id"].encode("utf-8"),
                        "name_ch": json_file[keys_lev1][keys_lev2]["name"].encode("utf-8"),
                        "name": keys_lev2.encode("utf-8")
                    }
                    menus_list.append(menu_info_dict)
            menus_dict = {
                "type": keys_lev1.encode("utf-8"),
                "name": menu_type,
                "menus": menus_list
            }
            all_menus_list.append(menus_dict)
    except Exception as e:
        print "Error occurred when parsing menu.json, %s" % e
    return render(request, 'yxt/dist.html', {"all_menus_list": all_menus_list})
