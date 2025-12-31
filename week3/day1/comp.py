class Computer:

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

    def do_the_thing(self):
        self.__sell()

my_comp = Computer()
my_comp.do_the_thing()