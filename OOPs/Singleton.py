class Singleton :
    __instance = None
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("Creating Instance")
        
        else:
            print("Using Existing Instance")
        
        return cls.__instance
    
Obj1 = Singleton()
Obj2 = Singleton()

print(Obj1 is Obj2)
