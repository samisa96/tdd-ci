import requests

class Jewishcal:
    """
    @ref: https://www.hebcal.com/home/195/jewish-calendar-rest-api
    """
    @staticmethod
    def rest_times(month, year):
        api_result = requests.get("https://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year={0}&month={1}&ss=on&mf=on&c=on&&geo=city&city=IL-Ashdod&m=50&s=on".format(year,month))
        api_response = api_result.json()
        #print (api_response)
        return api_response

    @staticmethod
    def specific_date_holiday(month, year):
        return Jewishcal.rest_times(month,year)['items']

    @staticmethod
    def display_holidays(month, year):
        date_temp_info= Jewishcal.specific_date_holiday(month, year)
        holidays=[]
        for item in date_temp_info:
            if item['category'] == "holiday":
                holidays.append({k:item[k] for k in item.keys() and ['date','title']})
        return holidays

    @staticmethod
    def display_candles(month, year):
        date_temp_info = Jewishcal.specific_date_holiday(month, year)
        candles_days = []
        for item in date_temp_info:
            if item['category'] == "candles":
                candles_days.append({k:item[k] for k in item.keys() and ['date','title']})
        return candles_days

    @staticmethod
    def display_parashat(month, year):
        date_temp_info = Jewishcal.specific_date_holiday(month, year)
        parashat_list = []
        for item in date_temp_info:
            if item['category'] == "parashat":
                parashat_list.append({k:item[k] for k in item.keys() and ['date','title']})
        return parashat_list

    @staticmethod
    def convert_to_hebrew(year,month,day):
        api_result = requests.get("https://www.hebcal.com/converter/?cfg=json&gy={0}&gm={1}&gd={2}&g2h=1".format(year, month, day))
        api_response = api_result.json()
        return api_response

    @staticmethod
    def print_convert():
        year = input("enter a Gregorian  year:")
        month = input("enter a  Gregorian  month:")
        day = input("enter a Gregorian  day:")
        result= Jewishcal.convert_to_hebrew(year, month, day)
        print(result['hy'],result['hm'],result['hd'],"or in hebrew "+ result['hebrew'])

        # print("{0},{1},{2} or in hebrew {3}".format(result[0],result[1],result[2],result[3]))

    @staticmethod
    def input_date(info):
        year = input("enter a year or write now for current year:")
        month = input("enter a month or write x for all months :")

        if info == 'all':
            print_text = Jewishcal.specific_date_holiday(month,year)
            for item in print_text:
                print("{0} there is a {1} :'{2}'".format(item['date'],item['category'],item['title']))
                #print(item['date'],item['title'])

        elif info == 'h':
            print_text = Jewishcal.display_holidays(month,year)
            for item in print_text:
                print('{0} date is "{1}"'.format(item['date'], item['title']), end='\n*')
        elif info == 'c':
            print_text = Jewishcal.display_candles(month, year)
            for item in print_text:
                print('{0} date is "{1}"'.format(item['date'], item['title']), end='\n*')
        elif info == 'p':
            print_text = Jewishcal.display_parashat(month, year)
            for item in print_text:
                print('{0} date the parashut is "{1}"'.format(item['date'], item['title']), end='\n*')


if __name__ == "__main__":
    Jewishcal.input_date()
    Jewishcal.print_convert()
