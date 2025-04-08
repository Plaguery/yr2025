const obj = JSON.parse(recipe.JSON);

let ingredientList = [];
const input = document.getElementById('inputBox');
const sidebar = document.getElementById('sidebar');
const ingredientsTable = document.getElementById('ingredientsTable');

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

input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        event.preventDefault(); 
        addIngredient();
    }
});

function addIngredient(){
    const ingredient = input.value.trim
    if (ingredient && !ingredientList.includes(ingredient)) {
        ingredientList.push(ingredient);
        cell.textContent = ingredient;

        cell.appendChild(deleteButton);
        row.appendChild(cell);
        ingredientsTable.appendChild(row);
        input.value = '';


    }
}

function removeIngredient(){
    
}

function searchRecipe(){

}
