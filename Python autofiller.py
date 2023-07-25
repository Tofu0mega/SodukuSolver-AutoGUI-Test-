import numpy as np
from os import system
import time 
import datetime
import keyboard
import mouse
import pyautogui as pg 

size=9
    
topleft=0
topright=0
botleft=0
botright=0







grid=[]
for i in range(size):
    a=[]
    for j in range(size):
        system("CLS")
        print("Enter The Value Of Box" ,i+1,j+1,"\n 0 if empty")
        a.append(int(input( )))
       
    grid.append(a)

time.sleep(5)
print(np.matrix(grid))

   



def possible(R,C,N):
    global grid
    for row in range(0,size):
        if grid[R][row]==N:
            return False
        
    for column in range(0,size):    
        if grid[column][C]==N:
            return False
           
    x0=(R//3)*3
    y0=(C//3)*3
    for q in range (0,3):
        for w in range(0,3):
            if grid[x0+q][y0+w]==N:
                return False
    
    return True

def solve():
    global grid
    for a in range(0,size):
        for b in range(0,size):
            if grid[a][b] == 0:
                for k in range(1,size+1):
                    if possible(a,b,k)==True:
                        grid[a][b]=k
                        
                        
                        solve()
                        grid[a][b]=0
                
                return
        filler()
        input("More Solution?")

    
    


    
       

def filler():
    global grid
    for i in range (9):
        for j in range (9):
            k=str(grid[i][j])
            pg.press(k)
            pg.press('right')
        
        pg.press('down')
        for i in range (8):
            pg.press('left')

        

  

solve()





