import random as rand
#create the playing field

def loadField(field, width, height):
    for i in range(0,height):
        row = []
        mineChance = .15
        for j in range(0,width):
            
            #mine decision
            r = rand.randint(0,100)
            
            if r <= mineChance * 100:
                row.append(9)
            else:
                row.append(0)
        
        #end append row
        field.append(row)
    
    #load board nums
    for i in range(0,height):
        #per row
        for j in range(0, width):
            #per col
            #if there is a mine, +1 to surrounding spots
            if field[i][j] == 9:
                mineFound(j,i, field)

def mineFound(x,y, field):
    #input coordinates of the mine
    #sniff around the mines for non-mine spots
    
    #upper left
    mineSniffer(x-1, y+1, field)
    #upper middle
    mineSniffer(x, y+1, field)
    #upper right
    mineSniffer(x+1, y+1, field)
    #left
    mineSniffer(x-1, y, field)
    #right
    mineSniffer(x+1, y, field)
    #lower left
    mineSniffer(x-1, y-1, field)
    #lower middle
    mineSniffer(x, y-1, field)
    #lower right
    mineSniffer(x+1, y-1, field)

def mineSniffer(x,y, field):
    height = len(field)
    width = len(field[0])
    
    #input coordinates that should be added
    #if not out of bounds
    if ((x >= 0 and x <= height-1) and (y >= 0 and y <= width-1)):
        #if not another mine
        if (field[y][x] != 9):
            #add one to this spot
            field[y][x] += 1

def printField(field):
    height = len(field)
    width = len(field[0])
    
    #print header
    for i in range(0, width+1):
        if i == 0:
            print("   | ", end="")
        else:
            print(f"{chr(i+64)} | ", end="")
    print("")
    
    #print board
    for i in range(0,height):
        #side bar
        print(f" {chr(i+65)} |", end="")
        #rows
        for j in range(0,width):
            print(" ", end="")
            if field[i][j] == 9:
                #mine
                print("X", end="")
                
            elif field[i][j] == 0:
                #empty
                print(" ", end="")
                
            else:
                print(f"{field[i][j]}", end="")
            print(" |", end="")
        print("")

field = []
flags = []
height = 10
width = 10

loadField(field, width, height)
printField(field)
