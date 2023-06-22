import json
import unittest

data1 = json.load(open('StudentJson.json', encoding='utf-8-sig'))
data2 = json.load(open('StudentJson2.json', encoding='utf-8-sig'))
final_result = json.load(open('final-data.json', encoding='utf-8-sig'))


def convert_first_data(jsonObject):

    conversion = {
        "ID": jsonObject["ID"],
        "LastName": jsonObject["LastName"],
        "FirstName": jsonObject["FirstName"],
        "Location": {
            "Country": jsonObject["Country"],
            "State": jsonObject["State"],
            "City": jsonObject["City"],

            "SAT": jsonObject["SAT"]

        },
        "Gender": jsonObject["Gender"],
        "StudentStatus": jsonObject["StudentStatus"],
        "Major": jsonObject["Major"],
        "Age": jsonObject["Age"],
        "Grade": jsonObject["Grade "],
        "Height": jsonObject["Height"]
    }

    return conversion

    return conversion


def convert_second_data(jsonObject):
    location = jsonObject["Location"].split(',')

    conversion1 = {
        "ID": jsonObject["ID"],
        "LastName": jsonObject["Name"]["LastName"],
        "FirstName": jsonObject["Name"]["FirstName"],
        "Location": {
            "Country": location[0],
            "State": location[1],
            "City": location[2],
            "SAT": location[3]

        },
        "Gender": jsonObject["Gender"],
        "StudentStatus": jsonObject["StudentStatus"],
        "Major": jsonObject["Major"],
        "Age": jsonObject["Age"],
        "Grade": jsonObject["Grade"],
        "Height": jsonObject["Height"]
    }

    return conversion1


def join(jsonObject):
    join = {}

    if (jsonObject.get("Name") == None):
        join = convert_first_data(jsonObject)
    else:
        join = convert_second_data(jsonObject)

    return join


class Test(unittest.TestCase):

    def test_final_result(self):

        f = json.loads(json.dumps(final_result))
        self.assertEqual(
            f,
            final_result
        )

    def test_dataType1(self):

        f = join(data1)
        self.assertEqual(
            f,
            final_result,
            "Converting from Type 1 failed"
        )

    def test_dataType2(self):

        f = join(data2)
        self.assertEqual(
            f,
            final_result,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main()
