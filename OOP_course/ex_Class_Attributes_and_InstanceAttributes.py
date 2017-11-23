'''
Write an object oriented program to create a precious stone.
Not more than 5 precious stones can be held in possession at a given point of time.
 If there are more than 5 precious stones, delete the first stone and store the new one.
'''

class Stone:
    stone_count = 0
    stone_list = []
    def __init__(self,name):
        self.name = name
        Stone.stone_count+= 1

        if Stone.stone_count <5:
            # if there's less than five stones, add one more to the stone_list
            Stone.stone_list.append(self)
        else:
            # if there more than 5 stones, del the first one
            del Stone.stone_list[0]
            Stone.stone_list.append(self)

    def print_list(self):
        for stone in Stone.stone_list:
            print(stone.name)


stone1 = Stone("Ruby")
#stone1.print_list()
stone2 = Stone("Diamond")
stone3 = Stone("Saphire")
stone4 = Stone("Emerald")
#stone4.print_list()
stone5 = Stone("Pebble")
stone6 = Stone("FakeDiamond")
stone6.print_list()
