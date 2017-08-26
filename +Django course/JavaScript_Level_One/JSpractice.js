var First = prompt("Hello and Welcome. Please enter your first name:")
var Last = prompt("Please enter your Last Name:")
var Age = prompt("How old are you?")
var Height = prompt("How tall are you in centimeters?")
var Pet = prompt("What is the name of your pet?")

alert("Thank you so much for the information.")

if (
	First[0] == Last[0] && 
	Age < 30 && Age > 20 && 
	Height >= 170 &&
	Pet[Pet.length-1] == "y"
	) {
	console.log("Welcome, Comrade!")
}else{
	console.log("Sorry, nothing to see here.")
}