const firstName = prompt("Hello and Welcome. Please enter your First Name: ")

const lastName = prompt("Please enter your Last Name:")

const age = prompt("How old are you?")

const height = prompt("How tall are you in centimeters?")

const petName = prompt("What is the name of your pet?")

alert("Thank you so much for the information.")

const test1 = firstName[0] === lastName[0]

const test2 = age > 20 && age < 30

const test3 = height >= 170

const test4 = petName[-1] === "y" || "Y"

if (test1 && test2 && test3 && test4) {
    console.log("Welcome Comrade! You've passed the Spy Test")
}
