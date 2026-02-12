let myCar = {
  color: 'blue',
  details: {
    plateNumber: 123,
    name: 'Ford'
  }
};

let myNewCar = { ...myCar };
myNewCar.color = 'red';

console.log(myCar.color); // blue
console.log(myNewCar.color); // red

myNewCar.details.name = 'Farari';
console.log(myNewCar.details.name); // Farari
console.log(myCar.details.name); // Farari

// why??
let obj1 = { a: 1, b: 2, c: 3 };
let obj2 = obj1;

obj2.a = 15;
console.log(obj1.a); // 15

myOtherNewCar = structuredClone(myCar);
myOtherNewCar.details.name = 'Skoda';
myOtherNewCar.details.plateNumber = 1;

console.log(myOtherNewCar);
console.log(myCar);
