coefGold = 0.25
coefSilver = 0.5
coefCuprum = 1.0

coins = 0

stamina = 100
helth = 100

minedGold = 0
minedSilver = 0
minedCuprum = 0


def Mine(typeOfMetal, time, stamina):
    mined = 0
    if typeOfMetal=="Gold":
        print("Mining gold....")
        stamina=stamina-10;
        mined += float(time)*0.25;
        print("You succesfully mined a "+str(mined)+" gold")
        return mined
    elif typeOfMetal=="Silver":
        print("Mining silver....")
        stamina=stamina-10;
        mined += float(time)*0.25;
        print("You succesfully mined a "+str(mined)+" gold")
        return mined
    elif typeOfMetal=="Cuprum":
        print("Mining cuprum....")
        stamina=stamina-10;
        mined += float(time)*0.25;
        print("You succesfully mined a "+str(mined)+" gold")
        return mined



def Chill(time):
    stamina = stamina+(time*20)
    helth = helth+(time*10)
    
def Sleep():
    stamina = 100
    helth = 100

def Sell(mined):
    print("You succesfully selled all your gold in "+str(mined)+" for "+str(mined*float(100))+" coins" )
    return mined*float(100)
        
coins = 0
mined = 0
while True:

    print("Choose a move:")
    choise = input("Mine/Chill/Sleep/Sell: ")
    if choise=="Mine":
        print("Choose a metal")
        metalType = input("Gold/Silver/Cuprum: ")
        mineTime = input("Input a time for mining: ")
        mined = Mine(metalType, mineTime, stamina)

    elif choise=="Chill":
        chillTime = input("Input a time for chill: ")
        Chill(chillTime)
    elif choise=="Sleep":
        Sleep()
    elif choise=="Sell":
        print("Selling...")
        coins = Sell(mined)

