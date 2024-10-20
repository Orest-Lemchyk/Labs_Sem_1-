class insects:
    __name = None
    __speed = None
    __weight = None

   
    def __init__(self, name = "not definated", speed = "not definated", weight = "lees then one gram"):
        print("Object is created.")
        self.set_data(name, speed, weight)
        #self.get_data()

   
    def set_data(self, name, speed, weight):
        self.name = name
        self.speed = speed
        self.weight = weight


    def get_data(self):
        print("Name :", self.name, "Speed(m\s) :", self.speed, "Weight(grams) :", self.weight)


class fly_insects(insects):
    __color_wings = None
    __wings_num = None
    __test_del = None
    def __init__(self, name, speed, weight, wings_num = 2, color_wings = "transparent ", test_del = True):
        super(fly_insects, self).__init__(name, speed, weight)
        self.color_wings = color_wings
        self.wings_num = wings_num
        self.test_del = test_del

    def get_data(self):
        super().get_data()
        print("Color wings:", self.color_wings, "Wings num:", self.wings_num, self.test_del)
    

    def __del__(self):
        print("Object deleted")

ant = insects("Ant", 5, 10)
ant.get_data()
buterfly = fly_insects("bob", 3, 7, 2, "blue")
buterfly.get_data()
