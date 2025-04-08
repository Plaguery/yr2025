import requests
import json 

baseUrl = "https://www.themealdb.com/api/json/v1/1/"
workingUrl = ""
ingredients = ["rice", "butter"]
mealID = set()
responses = []
recipes = []



def addIngred(ingred):
    ingredients.append(ingred)

#gets meal ids from ingredients
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

#gets meal data from ids
def getMealData():
    global responses
    responses = []
    for x in mealID:
        workingUrl = baseUrl + "lookup.php?i=" + x
        r = requests.get(workingUrl)
        responses.append(r.text)

def getData():
    findMeals()
    getMealData()

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

        lf = "strMeasure" + num
        currIngr = rText[lf]
        if not currIngr:
            break
        
        currIngr += " "
        lf = "strIngredient" + num
        currIngr += rText[lf]
        ingr.append(currIngr)
        print(currIngr)
    dic = {
        "name": name,
        "id": id,
        "imgsrc": imgsrc,
        "ingr":ingr,
        "instr":instr,
        "vid":vid

    }
    return dic

def getTop(x):
    for i in range(x):
        recipes.append(parseMealData(i))

def jsonDump():
    val = json.dumps(recipes)
    f = open("recipe.json", "w")
    f.write(val)
    f.close()


getData()
getTop(5)
jsonDump()
#recipes are stored as Recipe objects in the recipes list 