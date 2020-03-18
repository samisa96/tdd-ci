import unittest
from unittest.mock import Mock, patch, MagicMock
from src.Jewishcal import Jewishcal


class MyTestCase(unittest.TestCase):

    @patch('src.Jewishcal.requests.get')
    def test_input_date(self, mockJson):
        jewishcal_data = {"location": {"geo": "none"},
                          "link": "https://www.hebcal.com",
                          "title": "Hebcal February 2000",
                          "date": "2020-03-15T15:44:11-00:00",
                          "items":
                              {"category": "holiday", "hebrew": "בדיקות", "link": "https://www.hebcal.com",
                               "date": "2000-02-02", "title": "testing holiday"}
                          }

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mockJson.return_value = Mock(ok=True)
        mockJson.return_value.json.return_value = jewishcal_data
        # assume
        stub = {"month": 2, "year": 2000}

        # expected
        expected_item = {"category": "holiday", "hebrew": "בדיקות", "link": "https://www.hebcal.com",
                         "date": "2000-02-02", "title": "testing holiday"}

        # action
        date_result = Jewishcal.specific_date_holiday(**stub)

        # assert
        self.assertDictEqual(expected_item, date_result)
	expected_item_base= {"date": "2020-03-11T15:41:38-00:00",
                         "location": {"geonameid": 295629, "geo": "geoname", "country": "Israel", "city": "Ashdod",
                                      "latitude": 31.79213, "title": "Ashdod, Southern District, Israel",
                                      "tzid": "Asia/Jerusalem", "admin1": "Southern District", "longitude": 34.64966},
                         "longitude": 34.64966,
                         "link": "https://www.hebcal.com/hebcal/?v=1&maj=on&min=on&mod=on&nx=on&year=2000&month=2&ss=on&mf=on&c=on&geo=geoname&m=50&s=on&geonameid=295629&i=on",
                         "latitude": 31.79213, "title": "Hebcal February 2000 Ashdod, Southern District, Israel",
                         "items": [{"date": "2000-02-04T16:59:00+02:00", "hebrew": "הדלקת נרות",
                                    "title": "Candle lighting: 4:59pm", "category": "candles"},
                                   {"date": "2000-02-05", "hebrew": "פרשת משפטים",
                                    "link": "https://www.hebcal.com/sedrot/mishpatim", "title": "Parashat Mishpatim",
                                    "category": "parashat"},
                                   {"date": "2000-02-05T18:08:00+02:00", "hebrew": "הבדלה - 50 דקות",
                                    "title": "Havdalah (50 min): 6:08pm", "category": "havdalah"},
                                   {"hebrew": "ראש חודש אדר א׳", "memo": "Beginning of new Hebrew month of Adar",
                                    "date": "2000-02-06", "category": "roshchodesh",
                                    "link": "https://www.hebcal.com/holidays/rosh-chodesh-adar",
                                    "title": "Rosh Chodesh Adar I"},
                                   {"hebrew": "ראש חודש אדר א׳", "memo": "Beginning of new Hebrew month of Adar",
                                    "date": "2000-02-07", "category": "roshchodesh", "title": "Rosh Chodesh Adar I",
                                    "link": "https://www.hebcal.com/holidays/rosh-chodesh-adar"},
                                   {"title": "Candle lighting: 5:06pm", "category": "candles",
                                    "date": "2000-02-11T17:06:00+02:00", "hebrew": "הדלקת נרות"},
                                   {"hebrew": "פרשת תרומה", "date": "2000-02-12", "category": "parashat",
                                    "link": "https://www.hebcal.com/sedrot/terumah", "title": "Parashat Terumah"},
                                   {"title": "Havdalah (50 min): 6:14pm", "category": "havdalah",
                                    "date": "2000-02-12T18:14:00+02:00", "hebrew": "הבדלה - 50 דקות"},
                                   {"hebrew": "הדלקת נרות", "date": "2000-02-18T17:12:00+02:00", "category": "candles",
                                    "title": "Candle lighting: 5:12pm"},
                                   {"category": "parashat", "link": "https://www.hebcal.com/sedrot/tetzaveh",
                                    "title": "Parashat Tetzaveh", "hebrew": "פרשת תצוה", "date": "2000-02-19"},
                                   {"title": "Havdalah (50 min): 6:20pm", "category": "havdalah",
                                    "date": "2000-02-19T18:20:00+02:00", "hebrew": "הבדלה - 50 דקות"},
                                   {"hebrew": "פורים קטן",
                                    "memo": "Minor Purim celebration during Adar I on leap years", "date": "2000-02-20",
                                    "category": "holiday", "subcat": "minor",
                                    "link": "https://www.hebcal.com/holidays/purim-katan", "title": "Purim Katan"},
                                   {"title": "Candle lighting: 5:17pm", "category": "candles",
                                    "date": "2000-02-25T17:17:00+02:00", "hebrew": "הדלקת נרות"},
                                   {"category": "parashat", "title": "Parashat Ki Tisa",
                                    "link": "https://www.hebcal.com/sedrot/kitisa", "hebrew": "פרשת כי תשא",
                                    "date": "2000-02-26"},
                                   {"title": "Havdalah (50 min): 6:26pm", "category": "havdalah",
                                    "date": "2000-02-26T18:26:00+02:00", "hebrew": "הבדלה - 50 דקות"}]}


    def test_specific_date_holidays_test1(self,base=expected_item_base):
        # assume
        stub = {"month": 2,"year": 2000}
        # expected
        expected_item=base["items"]
                       
        # action
        date_result = Jewishcal.specific_date_holiday(**stub)
        # assert
        self.assertEqual(expected_item[0], date_result[0])
	def test_Rest_times_date(self):
        # assume
        stub = {"month": "x", "year": 2000}
        # expected
        expected_item = "Hebcal 2000 Ashdod, Southern District, Israel"

        # action
        date_result = Jewishcal.rest_times(**stub)
        # assert
        self.assertEqual(expected_item, date_result['title'])
	
    def test_display_holidays_test1(self,base=expected_item_base):
        # assume
        stub = {"month": 2, "year": 2000}
        # expected
        expected_item = base["items"]
        expected_holidays=[]
        for item in expected_item:
            if item['category'] == "holiday":
                expected_holidays.append({k:item[k] for k in item.keys() and ['date','title']})

        # action
        date_result = Jewishcal.display_holidays(**stub)
        # assert
        self.assertEqual(expected_holidays, date_result)
	def test_display_candles_test1(self,base=expected_item_base):
        # assume
        stub = {"month": 2, "year": 2000}
        # expected
        expected_item = base["items"]
        expected_holidays=[]
        for item in expected_item:
            if item['category'] == "candles":
                expected_holidays.append({k:item[k] for k in item.keys() and ['date','title']})

        # action
        date_result = Jewishcal.display_candles(**stub)
        # assert
        self.assertEqual(expected_holidays, date_result)
	def test_display_parashat_test1(self, base=expected_item_base):
        # assume
        stub = {"month": 2, "year": 2000}
        # expected
        expected_item = base["items"]
        expected_holidays = []
        for item in expected_item:
            if item['category'] == "parashat":
                expected_holidays.append({k: item[k] for k in item.keys() and ['date', 'title']})

        # action
        date_result = Jewishcal.display_parashat(**stub)
        # assert
        self.assertEqual(expected_holidays, date_result)
	def convert_test1(self):
        # assume
        stub = {"year":2000, "month": 2, "day":20}
        #excpeted
        expected_item={"gy":2000,"gm":2,"gd":20,"hy":5760,"hm":"Adar I","hd":14,"hebrew":"\u05d9\u05f4\u05d3 \u05d1\u05bc\u05b7\u05d0\u05b2\u05d3\u05b8\u05e8 \u05d0\u05f3 \u05ea\u05e9\u05f4\u05e1","events":["Parashat Ki Tisa","Purim Katan"]}
        #action
        converion_result=Jewishcal.convert_to_hebrew(**stub)
        #assert
        self.assertEqual(expected_item,converion_result)
	def convert_test2(self):
        # assume
        stub = {"year":"x", "month": 2, "day":20}
        #excpeted
        expected_item={"error":"Gregorian year must be numeric"}
        #action
        converion_result=Jewishcal.convert_to_hebrew(**stub)
        #assert
        self.assertEqual(expected_item,converion_result)
	 def convert_test3(self):
        # assume
        stub = {"year": 2000, "month":"x", "day": 20}
        # excpeted
        expected_item = {"error":"Gregorian month must be numeric"}
        # action
        converion_result = Jewishcal.convert_to_hebrew(**stub)
        # assert
        self.assertEqual(expected_item, converion_result)
     def convert_test_len(self,mockC):
        mockC.return_value.__len__.return_value=8

        #assume
        stub = {"year": 2000, "month": "x", "day": 20}
        # excpeted
        expected_len = 8
        # action
        converion_result = Jewishcal.convert_to_hebrew(**stub)
        print(converion_result)
        # assert
        self.assertEqual(expected_len, len(converion_result))



if __name__ == '__main__':
    unittest.main()
