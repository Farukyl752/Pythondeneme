class person:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age    
        self.department=department
def menu():
    print("1-Add Person")
    print("2-Show Persons")
    print("3-Delete Person")
    print("4-Exit") 
peoplelist=[]
def addPerson():
    name=input("Enter name:")   
    age=int(input("Enter age:"))
    department=input("Enter department:")
    p=person(name,age,department)
    peoplelist.append(p)
    print("Person added.") 
x=0
while x!=4:
    menu()
    x=int(input("Choose an option:"))
    if x==1:
        addPerson()
    elif x==2:
        if len(peoplelist)==0:
            print("No persons to show.")
        else:   
            for p in peoplelist:
                print("Name:"+p.name+"\tAge:"+str(p.age)+"\tDepartment:"+p.department)
    elif x==3:
        name=input("Enter the name of the person to delete:")
        for p in peoplelist:
            if p.name==name:
                peoplelist.remove(p)
                print("Person deleted.")
    elif x==4:
        print("Exiting the program.")
    else:
        print("Wrong option, please try again.")
        