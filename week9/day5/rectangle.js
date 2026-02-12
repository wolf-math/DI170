class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.height * this.width;
  }

  // Setter
  set area(factor) {
    this.width = this.width * factor ** (1 / 2);
    this.height = this.height * factor ** (1 / 2);
  }
}

let square = new Rectangle(10, 10);
console.log(square.area); // 100
square.area = 2;
console.log(square.area); // 200

console.log(square.height);
