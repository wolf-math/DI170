let myArr = ['one', 'two', 'three'];

// myArr -> address 1
// "one" -> address 2
// "two" -> address 3
// "three" -> address 4

// myArr contains address1, address2, address3

// console.log(myArr);

let myOtherArr = myArr;
// Slapping another label on the box

myOtherArr[0] = 'zero';

// console.log(myOtherArr);
// console.log(myArr);

// ======================== //

let a = [1, 2, 3];
let b = [1, 2, 3];
// console.log("5" === 5) // false
// console.log("5" == 5) // true
// console.log(a === b); // false
// console.log(a == b); // false

// ======================== //

let c = a;
console.log(c === a); // true

c = [...a];
console.log(a);
console.log(c);

console.log(a === c);
