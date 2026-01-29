// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, console.log the age of my mum and my dad. My mum is twice my age, and my dad is 1.2 the age of my mum.

function myAge(age) {
  const mum = age * 2;
  const dad = mum * 1.2;

  console.log(
    `My age is ${age}. My mum is ${mum} years old, and my dad is ${dad}!`
  );
}

// 4. Call the function.

myAge(4);
