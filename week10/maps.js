const myArr = [1, 2, 3, 4, { one: 1 }];

const myArr2 = myArr.map((val) => val);

console.log(myArr2);

console.log(myArr === myArr2);

console.log(myArr2[4]);
console.log(myArr[4] === myArr2[4]);
