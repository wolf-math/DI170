// Don't do this

async function hello() {
  return 'Hello';
}

const b = hello();

b.then((result) => console.log(result));

// Do this!!!

async function hello() {
  return 'Hello';
}

async function sayHi() {
  const result = await hello();
  console.log(result);
}

sayHi();
