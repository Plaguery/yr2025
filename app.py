import requests
import json 

baseUrl = "https://www.themealdb.com/api/json/v1/1/"
workingUrl = ""
ingredients = ["rice", "coconut"]
mealID = set()
responses = []
recipes = []


class Recipe:


    def __init__(self,name,id, imgsrc, ingredients, amounts, instructions, video):
        self.name = name
        self.id = id
        self.imgsrc = imgsrc
        self.ingredients = ingredients
        self.amounts = amounts
        self.instructions = instructions
        self.video = video



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
    global responses
    responses = []
    for x in mealID:
        workingUrl = baseUrl + "lookup.php?i=" + x
        r = requests.get(workingUrl)
        responses.append(r.text)

    print(responses[1])

def parseMealData(i):
    r = responses[i]
    rText = json.loads(r)
    rText = rText["meals"][0]
    name = rText["strMeal"]
    id = rText["idMeal"]
    instr = rText["strInstructions"]
    imgsrc = rText["strMealThumb"]
    vid = rText["strYoutube"]
    ingr = []
    ingrMeasure = []


    for i in range(20):
        num = str(i+1)

        lf = "strIngredient" + num
        currIngr = rText[lf]
        if not currIngr:
            break
        ingr.append(currIngr)

        lf = "strMeasure" + num
        currMeasure = rText[lf]
        ingrMeasure.append(currMeasure)

    rec = Recipe(name, id, imgsrc, ingr, ingrMeasure, instr,vid)
    return rec

findMeals()
getMealData()

rec = parseMealData(1)
print(rec.name)
print(rec.instructions)
