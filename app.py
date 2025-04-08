import requests
import json 

baseUrl = "https://www.themealdb.com/api/json/v1/1/"
workingUrl = ""
ingredients = ["rice", "ap"]
mealID = set()
responses = []

def addIngred(ingred):
    ingredients.append(ingred)


def findMeals():
    for i in ingredients:
        workingUrl = baseUrl + "filter.php?i=" + i
        r = requests.get(workingUrl)

        if(r.text == "{\"meals\":null}"):
            print("meals not found")
        else:
            rText = json.loads(r.text)
            for meal in rText['meals']:
                mealID.add(meal['idMeal'])

def getMealData():
    responses = []
    for x in mealID:
        workingUrl = baseUrl + "lookup.php?i=" + x
        r = requests.get(workingUrl)
        responses.append(r.text)


findMeals()
getMealData()
