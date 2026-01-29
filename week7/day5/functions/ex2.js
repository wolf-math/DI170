// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, return the age of my mum (my mum is twice my age)

// 4. Call the function

// 5. In the global scope, console.log the result of the function

function whatsMyAgeAgain(myAge) {
  return myAge * 2;
}

let mum = whatsMyAgeAgain(9);

console.log(mum);

// ternary operator

let age = 19;

if (age > 18) {
  console.log("Let's go to the pub");
} else {
  console.log('you are too young');
}

age > 18
  ? console.log("Let's go to the pub")
  : console.log('you are too young');
