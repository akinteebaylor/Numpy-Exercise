def main():
    play = input("Do you want to play first?? Y/N ")
    if play == 'y' or play == 'Y':
        playgame()
        game = input("Do you want to play again?? Y/N ")
        if game == 'Y' or game == 'y':
            playgame()
        else:
            print("Thank you for playing")
    elif play == 'n' or play == 'N':
        playcomp()
        game = input("Do you want to play again?? Y/N ")
        if game == 'Y' or game == 'y':
           playcomp()
        else:
            print("Thank you for playing")
######################################## 

def playgame():
    import numpy as np
    bb = np.zeros((3, 3))
    cc = 0
    store = []
    while cc < 1:
        b, c = humanplay(bb, store)
        cc, bb = wincheck(b)
        if cc < 1:
            e = compplay(b, c)
            cc, bb = wincheck(e[0])
####################################
def playcomp():
    import numpy as np
    bb = np.zeros((3, 3))
    cc = 0
    store = []
    while cc < 1:
        b, c = compplay(bb, store)
        cc, bb = wincheck(b)
        if cc < 1:
            e = humanplay(b, c)
            cc, bb = wincheck(e[0])

######################################
def humanplay(tee, store):
    import numpy as np
    import copy
    pl = np.zeros((3,3))
    list = ["row", "column"]
    a=0
    while a==0:
        play=[]
        for i in range(0, 2):
            x = int(input("Enter the" + " " + list[i] + " " + "you wish to play "))
            play.append(x)
        # print(play)
        # print(store)
        if play not in store:
            store.append(play)
            pl[play[0], play[1]] = 1
            a=-1
            tee2 = tee + pl
        else:
            a=0
            print("This location was previously selected, please choose another location")
    return tee2, store
##########################################################################
##########################################
def compplay(tee, store):
    import numpy as np
    import copy
    pl = np.zeros((3, 3))
    a = 0
    while a == 0:
        play = []
        y = np.random.randint(0, 3, 2)
        play.append(y[0])
        play.append(y[1])
        if play not in store:
            store.append(play)
            pl[play[0], play[1]] = -1
            a = -1
            tee2 = tee + pl
        else:
            a = 0
    return tee2, store
########################################################################

##############################################################
def wincheck(tee2):
    import numpy as np
    import copy
    tee6 = copy.deepcopy(tee2)
    tee7 = np.fliplr(tee6)
    yyy= np.diag(tee6, k=0)
    yyz = np.diag(tee7, k=0)
    # print(yyy.sum(axis=0))
    y = tee2.sum(axis=0)
    yy = tee2.sum(axis=1)
    if y.min() <=-3 or yy.min() <= -3:
        print("Computer Wins")
        y = 1
    elif y.max() >=3 or yy.max() >= 3:
        print("You Win")
        y = 1    
    elif yyy.sum(axis=0) == 3:
        print("You Win")
        y = 1
    elif yyy.sum(axis=0) == -3:
        print("Computer Wins")
        y = 1
    elif yyz.sum(axis=0) == 3:
        print("You Win")
        y=1
    elif yyz.sum(axis=0) == -3:
        print ("Computer Wins")
        y=1
    else:
        y = 0
    print('--------')
    tee3= copy.deepcopy(tee2)
    tee3= np.where(tee3 == 1, 'X', tee3)
    tee3 = np.where(tee3 == '1.0', 'X', tee3)
    tee4 = copy.deepcopy(tee3)
    tee4 = np.where(tee4 == -1, 'O', tee4)
    tee4 = np.where(tee4 == '-1.0', 'O', tee4)
    tee5 = copy.deepcopy(tee4)
    tee5 = np.where(tee5== '0.0','', tee5)
    print (tee5)
    return y, tee2
#####################################################################

main()
