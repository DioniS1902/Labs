class Mechanical3Dpuzzle:

    countOfPuzzels=0

    def __init__(self,countOfElements=0,guaranteeInMonths=0,material="",typeOfPuzzel="",price=None,name=None,countOfBuys=None):
        self.countOfElements=countOfElements
        self.guaranteeInMonths=guaranteeInMonths
        self.material=material
        self.typeOfPuzzel=typeOfPuzzel
        self.price=price
        self.name=name
        self.countOfBuys=countOfBuys
        Mechanical3Dpuzzle.countOfPuzzels=Mechanical3Dpuzzle.countOfPuzzels+1


    @staticmethod
    def getCountOfPuzzels():
        return Mechanical3Dpuzzle.countOfPuzzels

    def __del__(self):
        print('Destructor called, object deleted')

    def __str__(self):
        return "Count of elements = {countOfElements}, guarantee = {guaranteeInMonths} Months, material = {material}, type of puzzel = {typeOfPuzzel} {price} {name} {countOfBuys}\n".format(countOfElements=self.countOfElements,
                                                                                                                                                                                             guaranteeInMonths=self.guaranteeInMonths,
                                                                                                                                                                                             material=self.material,
                                                                                                                                                                                             typeOfPuzzel=self.typeOfPuzzel,
                                                                                                                                                                                             price=f", price = {str(self.price)}" if self.price else "",
                                                                                                                                                                                             name=f", name = {str(self.name)}" if self.name else "",
                                                                                                                                                                                             countOfBuys=f", count of buys = {str(self.countOfBuys)}" if self.countOfBuys else "")
def main():
    first = Mechanical3Dpuzzle(124, 12, "Cardboard", "Cars", 499)
    second = Mechanical3Dpuzzle(256, 6, "Cardboard", "Cartoons", 9999, "Princess")
    third = Mechanical3Dpuzzle(512, 8, "Cardboard", "Dogs", 1499, "Puppies", 12)
    print(str(first), str(second), str(third))
    print(f"count of puzzels : {Mechanical3Dpuzzle.getCountOfPuzzels()}")

if __name__ == '__main__':
    main()
