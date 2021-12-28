#Modules Used to in this program

from pyamaze import maze,agent,textLabel
from queue import PriorityQueue

#Heuristic Value
def h(a,b):
    x1,y1=a
    x2,y2=b

    return abs(x1-x2) + abs(y1-y2)                  #Returning the heristic value 

#Main Logic
def AStar(m):

	                                                 #Filling All cells with infinate

    start=(m.rows,m.cols)                            #Taking the starting block as the last block of the maze
    g_score={cell:float('inf') for cell in m.grid}   #Feeling all the g values as Infinity 
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}   #Feeling all H values values as Infinity 
    f_score[start]=h(start,(1,1))

    #Creating A quee

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))  #Pushing the starting Block into the Quee
    
    aPath={}   #Path From start to End

    #starte scaning the Maze
    while not open.empty():

        currCell=open.get()[2]  
        
        if currCell==(1,1):                          #Checking for the end Block
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:        #Checking possible ways for a specific block 
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                #Updating the score 
                temp_g_score=g_score[currCell]+1             
                temp_f_score=temp_g_score+h(childCell,(1,1))

                #Checking for list heristic value 
                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    #Marking the path 
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1) 

    #Reversing the travelled path for the actual path  
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath


#Creating the mage 
m=maze(6,6)
m.CreateMaze()

#Calling the main logic function
path=AStar(m)


#Creating the traveller agent 
a=agent(m,footprints=True)

#Showing the marked path 
m.tracePath({a:path})
l=textLabel(m,'A Star Path Length',len(path)+1)

#Calling the UI Function  
m.run()
