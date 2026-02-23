let student = {
  name: 'John',
  age: 30,
  isAdmin: false,
  courses: ['html', 'css', 'js'],
  wife: null,
  myFunc: "() => console.log('hi')"
};

let jsonStudent = JSON.stringify(student, null, 2);

console.log(jsonStudent);
