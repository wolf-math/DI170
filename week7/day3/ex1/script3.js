// 1. Create a numerically indexed table (ie. an array): pets, like this

let animals = ['cat', 'dog', 'fish', 'rabbit', 'cow'];

// 2. Display dog

console.log(animals[1]);

// 3. Add to the array pets, the pet horse. Remove the pet rabbit

animals.splice(3, 1, 'horse');
console.log(animals);

// 4. Display the array length

console.log(animals.length);
