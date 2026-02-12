const formData1 = '';
const formData2 = '  ';
const formData3 = 'Hey guys!';

function isNotEmpty(data) {
  // return false if empty, else return true
  return !!data.trim();
}

isNotEmpty(formData1); // false
isNotEmpty(formData2); // false
isNotEmpty(formData3); // true
