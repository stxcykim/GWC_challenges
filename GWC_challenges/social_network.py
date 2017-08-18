class Food:

    def __init__(self,name):
        self.name=name
        self.numcarbs= 0
        self.numcas=0
        self.ishot=False
        self.ingredients=[]

    def cook(self,cooktime):
        print ("It took" + cooktime + "to cook")
        self.ishot=True
        print("The food is now hot")

    def main():
        Cookie=Food("Chocolate Chip")
        Cookie.cook("20 minutes")
    main()
