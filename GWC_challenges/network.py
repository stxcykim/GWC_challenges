class Food:
    def __init__(self,name):
        self.name=name
        self.numcarbs= 0
        self.numcas=0
        self.isHot=False
        self.ingredients=[]

    def cook(self,cooktime):
        print ("It took" + cooktime + "to cook" +self.name +"!!!")
        self.isHot=True
        print("The food is now hot")

    def isItHot(self):
        return self.isHot

def main():
    
    Cookie=Food("Chocolate Chip")
    Cookie.cook("20 minutes")
    print(Cookie.isItHot())
    Apple=Food("Macintosh")
    Apple.cook("3 hours")
    print(Apple.isItHot())
    
main()
