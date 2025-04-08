import requests
import json 

baseUrl = "https://www.themealdb.com/api/json/v1/1/"
workingUrl = ""
ingredients = ["rice", "ap"]
responses = []
meals = set()



def addIngred(ingred):
    ingredients.append(ingred)


def findMeals():
    for i in ingredients:
        workingUrl = baseUrl + "filter.php?i=" + i
        r = requests.get(workingUrl)

        if(r.text == "{\"meals\":null}"):
            print("meals not found")
        else:
            print(r.text)
            responses.append
            rText = json.loads(r.text)
            for meal in rText['meals']:
                meals.add(meal['idMeal'])
            

findMeals()

