// Use the methods above to :

// Count how many keys and values are in the object below
// Display : "The x# key is : --- The x# value is : ---".

let myObj = {
  name: 'John',
  lastName: 'Doe',
  age: 25,
  friends: ['Mark', 'Lucie', 'Ana']
};

let count = Object.keys(myObj).length;
console.log(count);

for (item of Object.entries(myObj)) {
  // console.log(item);
  console.log(`The x# key is : ${item[0]}. The x# value is : ${item[1]}`);
}
