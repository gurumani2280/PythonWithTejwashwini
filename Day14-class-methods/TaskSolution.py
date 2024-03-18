class PreciousStones :
    preciousstones_list = []
    def __init__(self,name):
        self.name = name
        if len(PreciousStones.preciousstones_list) < 5 :
            PreciousStones.preciousstones_list.append(self.name)
        else:
            PreciousStones.preciousstones_list.pop(0)
            PreciousStones.preciousstones_list.append(self.name)


    @classmethod
    def PrintPreciousStonesList(cls):
        print(cls.preciousstones_list)
Stone1 = PreciousStones("Ruby")
PreciousStones.PrintPreciousStonesList()
Stone2 = PreciousStones("Emerald")
PreciousStones.PrintPreciousStonesList()
Stone3 = PreciousStones("Diamond")
PreciousStones.PrintPreciousStonesList()
Stone4 = PreciousStones("Yellow saphire")
PreciousStones.PrintPreciousStonesList()
Stone5 = PreciousStones("Blue saphire")
PreciousStones.PrintPreciousStonesList()
Stone6 = PreciousStones("Jade")
PreciousStones.PrintPreciousStonesList()
