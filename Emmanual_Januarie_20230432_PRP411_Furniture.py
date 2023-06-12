strEntry = int(input("Enter wood types( 1 - pine, 2 - oak, 3- mohogany):  "))
default = 0

dictWoodType = {
    "pine" : 100,
    "oak":250,
    "mohogany":350
}
def enter1(strSize):
    if strSize == "large":
        dictWoodType["pine"] = 100 + 40
        print(dictWoodType["pine"])
        
    elif strSize == "small":
        print("no extra price")

def enter2(strSize):
    if strSize == "large":
        dictWoodType["oak"] = 250 + 40
        print(dictWoodType["oak"])
        
    elif strSize == "small":
        print("no extra price")

def enter3(strSize):
    if strSize == "large":
        dictWoodType["mohogany"] = 350 + 40
        print(dictWoodType["mohogany"])
        
    elif strSize == "small":
        print("no extra price")

#if-statement to display price of chosen woodtype
if strEntry == 1:
    print("pine")
    print(dictWoodType["pine"])
elif strEntry == 2:
    print("oak")
    print(dictWoodType["oak"])
elif strEntry == 3:
    print("mohogany")
    print(dictWoodType["mohogany"])


#if statement to display 0 if invalid entry is inputted
if strEntry == 0 or strEntry > 3:
    print(default)

#if statement to declare if the entry is valid
if strEntry == 1:
    strSize = input('Enter " small or large')
    enter1(strSize)

if strEntry == 2:
    strSize = input('Enter " small or large')
    enter2(strSize)
    
if strEntry == 3:
    strSize = input('Enter " small or large')
    enter3(strSize)
   
#if size value is invalid
if strSize != "small" and strSize != "large":
    print("Please enter a valid input, (small or large)")


