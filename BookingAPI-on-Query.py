#!/usr/bin/env python
# coding: utf-8

# Libraries
import re
from datetime import datetime
import sys
import requests
import logging

def getInputData():
    data = {}
    data['childrens'] = input("How many children?  ")
    data['guests'] = input("How many guests?  ")
    data['rooms'] = input("How many rooms?  ")

    if (not data['childrens'].isdigit() or int(data['childrens']) < 0) or (not data['guests'].isdigit() or int(data['guests']) <= 0) or (not data['rooms'].isdigit() or int(data['rooms']) <= 0):
        raise Exception("Input is not correct")

    data['departure_date'] = input("What is the date of your departure? Hint: yyyy-mm-dd  ") #departure date must be after arrival date.
    data['arrival_date'] = input("What is the date of your arrival? Hint: yyyy-mm-dd  ") #arrival date must be today or after today.

    try:
        departure_datetime = datetime.strptime(data['departure_date'], '%Y-%m-%d')
        arrival_datetime = datetime.strptime(data['arrival_date'], '%Y-%m-%d')
        
        if arrival_datetime >= departure_datetime:
            raise Exception("Departure date must be greater than arrival date")
    except ValueError:
        raise Exception("Date format is not correct")
        
    return data

def getResponse(data):
    headers = {
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://www.booking.com',
        'Referer': 'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEHyAEM2AEB6AEBiAIBqAIDuAK9xPmdBsACAdICJDlkYzZmNjg5LTE0ZjYtNDIzYy04NjVkLWRmOTYyNTE5M2MyMdgCBeACAQ&sid=dd84131c86d6702477f73e2ef27d68fd&aid=304142&ss=New+York%2C+New+York+State%2C+United+States&ssne=Prague&ssne_untouched=Prague&efdco=1&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=20088325&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=cd313647c72200dc&ac_meta=GhBjZDMxMzY0N2M3MjIwMGRjIAAoATICZW46BE5ldyBAAEoAUAA%3D&group_adults=2&no_rooms=2&group_children=1&age=17&sb_travel_purpose=leisure&offset=25',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'accept': '*/*',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'x-booking-context-action-name': 'searchresults_irene',
        'x-booking-context-aid': '304142',
        'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY3MzQyODk4NywiZXhwIjoxNjczNTE1Mzg3fQ.Uc8LvVe25WDaZY-bFNGdlWzJ-og28ipya3ihXmSaqdRLGvbI652mwkPLiZTNCuj3ZucmRBduJfhhvQnunPzYhA',
        'x-booking-et-serialized-state': 'EN35HDDsGyjzBDVOQxjXf5W0nd-AmSOQIPeHCql4exAFgbHr1MXAIDXeGZEdYid7W',
        'x-booking-pageview-id': '524041fdc907009d',
        'x-booking-site-type-id': '1',
        'x-booking-topic': 'capla_browser_b-search-web-searchresults',
    }


    list_by_map_url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list-by-map"


    list_by_map_querystring = {
        "search_id":"none",
        "children_age":"",
        "price_filter_currencycode":"USD",
        "languagecode":"en-us",
        "travel_purpose":"leisure",
        "categories_filter":"class%3A%3A1%2Cclass%3A%3A2%2Cclass%3A%3A3",
        "children_qty":data['childrens'],
        "order_by":"popularity",
        "guest_qty":data['guests'],
        "room_qty":data['rooms'],
        "departure_date":data['departure_date'],
        "bbox":"49.2743100%2C50.8784941%2C13.1709517%2C15.9043652",
        "arrival_date":data['arrival_date']
    }
    list_by_map_headers = {
        'x-rapidapi-host': "apidojo-booking-v1.p.rapidapi.com",
        'x-rapidapi-key': "09576d7e30msh81b0021d19bd767p117eecjsna7a43b11ea52"
    }

    list_by_map_response = requests.request("GET", list_by_map_url, headers=list_by_map_headers, params=list_by_map_querystring).json()

    return list_by_map_response
    
def printData(data):
    if "result" in data:
        for list_result in data['result']:
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print("Name: ", list_result['hotel_name'])
            print("Establishment: ", list_result['accommodation_type_name'])
            print("Price: ", list_result['price_breakdown']['gross_price'], list_result['currencycode']) 
            print("Guest Reviews: ", list_result['review_score'], "(",list_result['review_score_word'], ")")
            print("Address: ", list_result['address'])
            print("Website: ", list_result['url'])

    else:
        print("The request was entered incorrectly!", data['message'])

def main():
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
    
    try:
        data = getInputData()
        printData(getResponse(data))
    except Exception as err:
        logging.exception(err, exc_info=True)
    
main()
