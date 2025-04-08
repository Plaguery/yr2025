const obj = JSON.parse(recipe.JSON);

let ingredientList = [];
const input = document.getElementById('inputBox');

var fName = "Argon"
var lName = "Neon"
var email = "ArgoNeo@gmail.com"
var password = "pass34523"
var priceR = 220


var user = {
    FirstName: fName, 
    LastName: lName,
    Email: email, 
    Password: password, 
    PriceRange: priceR
}

var userstring = JSON.stringify(user);


const fs = require('fs');

const saveData = (user) => {
    const finished = (error) => {
        if (error) {
            console.error(error)
            return;
        }
    }


    const jsonData = JSON.stringify(user);
    //console.log(user)
    //console.log(jsonData)
    fs.writeFile("thing.json",jsonData,finished);
}

saveData(user);

function addIngredient(){
    if (!ingredientList.includes(input.value)){
        ingredientList.push(input.value);
        
    }
}

function searchRecipe(){

}
