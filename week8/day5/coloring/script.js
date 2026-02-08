const palette = document.getElementById('palette');
const convas = document.getElementById('canvas');

const colors = [
  'darkred',
  'red',
  'darkorange',
  'orange',
  'goldenrod',
  'yellow',
  'darkgreen',
  'green',
  'darkturquoise',
  'turquoise',
  'darkblue',
  'midnightblue',
  'blue',
  'indigo',
  'darkviolet',
  'violet',
  'black',
  'white'
];

let theChosenColor;
let isDown = false;

// create color palette
for (let color of colors) {
  const swatch = document.createElement('div');
  swatch.className = 'color-swatch';
  swatch.style.backgroundColor = color;

  swatch.addEventListener('click', () => {
    theChosenColor = swatch.style.backgroundColor;
  });

  palette.appendChild(swatch);
}

// calculate the size of the canvas
const rows = Math.floor(canvas.clientHeight / 10);
const columns = Math.floor(canvas.offsetWidth / 10);
// create the canvas
for (let i = 1; i <= rows * columns; i++) {
  const pixel = document.createElement('div');
  pixel.className = 'pixel';

  pixel.addEventListener('click', (e) => {
    e.preventDefault();
    pixel.style.backgroundColor = theChosenColor;
  });

  pixel.addEventListener('mousedown', (e) => {
    e.preventDefault();
    isDown = true;
  });

  pixel.addEventListener('mouseup', (e) => {
    e.preventDefault();
    isDown = false;
  });

  pixel.addEventListener('mouseenter', (e) => {
    e.preventDefault();
    if (isDown) {
      pixel.style.backgroundColor = theChosenColor;
    }
  });

  canvas.appendChild(pixel);
}

const clear = document.getElementById('clearbutton');

const pixels = document.querySelectorAll('.pixel');

clear.addEventListener('click', (e) => {
  e.preventDefault();
  for (let pix of pixels) {
    pix.style.backgroundColor = 'white';
  }
});
