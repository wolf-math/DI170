async function hello() {
  return 'Hello';
}

// Don't do this

const b = hello();

b.then((result) => console.log(result));

// Do this!!!
async function sayHi() {
  const result = await hello();
  console.log(result);
}

sayHi();

// ==================

// let goodGrades = 93;

// let endSemester = new Promise((resolve, reject) => {
//   if (goodGrades > 90) {
//     resolve('Computer');
//   } else if ((goodGrades) => 80 && goodGrades <= 89) {
//     resolve('Phone');
//   } else {
//     reject("I won't get the gift");
//   }
// });

// const checkRequest = () => {
//   console.log('test 2');
//   endSemester.then((value) => console.log('I got an amazing gift : A ', value));
// };

// console.log('test 1');
// checkRequest();
// console.log('test 3');



let goodGrades = 93;

const endSemester = new Promise((resolve, reject) => {
  if (goodGrades > 90) {
    resolve('Computer');
  } else if (goodGrades >= 80 && goodGrades <= 89) {
    // fixed comparison
    resolve('Phone');
  } else {
    reject("I won't get the gift");
  }
});

async function checkRequest() {
  console.log('test 2');
  try {
    const gift = await endSemester;
    console.log('I got an amazing gift: A', gift);
  } catch (error) {
    console.log(error);
  }
}

console.log('test 1');
checkRequest();
console.log('test 3');