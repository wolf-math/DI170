const city = 'Sascanchuan';

const address = {
  street: 'Evergreen Terrace',
  number: '742',
  city: 'Kalamazoo',
  state: 'MI',
  zip: '49007'
};

const { street, city: addressCity } = address;
console.log(street); //Evergreen Terrace
console.log(city); //Sascanchuan
console.log(addressCity); //Kalamazoo

console.log(address.city); //Kalamazoo
