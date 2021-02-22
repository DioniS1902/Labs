class Mechanical3dPuzzle:

    countOfPuzzles=0

    def __init__(self, countOfElements=0, guaranteeInMonths=0, material="", typeOfPuzzle="",
                                                        price=None, name=None, countOfBuys=None):
        self.countOfElements = countOfElements
        self.guaranteeInMonths = guaranteeInMonths
        self.material = material
        self.typeOfPuzzle = typeOfPuzzle
        self.price = price
        self.name = name
        self.countOfBuys = countOfBuys
        Mechanical3dPuzzle.countOfPuzzles = Mechanical3dPuzzle.countOfPuzzles+1


    @staticmethod
    def getCountOfPuzzels():
        return Mechanical3dPuzzle.countOfPuzzles

    def __del__(self):
        print('Destructor called, object deleted')

    def __str__(self):
        returneSring="Count of elements = {countOfElements}, guarantee = {guaranteeInMonths} Months, material = {material}, type of puzzel = {typeOfPuzzel} {price} {name} {countOfBuys}\n"
        return returneSring.format(countOfElements = self.countOfElements,
                                                                guaranteeInMonths = self.guaranteeInMonths,
                                                                material = self.material,
                                                                typeOfPuzzel = self.typeOfPuzzle,
                                                                price = f", price = {self.price}" if self.price is not None else "",
                                                                name = f", name = {self.name}" if self.name else "",
                                                                countOfBuys = f", count of buys = {self.countOfBuys}" if self.countOfBuys is not None else "")
def main():
    first = Mechanical3dPuzzle(124, 12, "Cardboard", "Cars", 499)
    second = Mechanical3dPuzzle(256, 6, "Cardboard", "Cartoons", 9999, "Princess")
    third = Mechanical3dPuzzle(512, 8, "Cardboard", "Dogs", 1499, "Puppies", 12)
    print(first, second, third)
    print(f"count of puzzels : {Mechanical3dPuzzle.getCountOfPuzzels()}")

if __name__ == '__main__':
    main()
