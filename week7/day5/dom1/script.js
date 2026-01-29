// For each of the questions, find 2 WAYS of accessing :

// 1. The div DOM node?

const divDom = document.body.firstElementChild;
const divDom2 = document.body.children[0];

console.log(divDom);
console.log(divDom2);

// 2. The ul DOM node?

const ulDom = document.body.firstElementChild.nextElementSibling;
const ulDom2 = document.body.lastElementChild.previousElementSibling;

console.log(ulDom);
console.log(ulDom2);

// 3. The second li (with Pete)?

const pete =
  document.body.firstElementChild.nextElementSibling.lastElementChild;

const pete2 = ulDom.lastElementChild;

const pete3 = document.getElementById('pete');

pete.innerText = 'Marko';

console.log(pete.innerText);
console.log(pete2.innerText);

// Aaron Notes:

const names = document.getElementsByClassName('name');
// this ^ is an array

const names2 = document.querySelectorAll('#names');

const tova = document.createElement('li');
tova.innerText = 'Tova';
ulDom.appendChild(tova);
