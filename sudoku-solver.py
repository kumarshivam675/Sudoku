'''
Created on Apr 28, 2014

@author: savs95
'''
'''
Part B: Implement the following 2 rules to solve the Sudoku Puzzle.

Rule 1: If a cell can take only one number, assign that number to that cell.

Rule 2: If there is a number which can go into only one cell, then assign that number to that cell.
'''

import sudoku_a
hash1=graph-coloring.form_hash()
possible_hash={}

arr=[['e', 6, 'e', 1, 'e', 4, 'e', 5, 'e'],      
      ['e', 'e', 8, 3, 'e', 5, 6, 'e', 'e'], 
      [2, 'e', 'e', 'e', 'e', 'e', 'e', 'e', 1], 
      [8, 'e', 'e', 4, 'e', 7, 'e', 'e', 6], 
      ['e', 'e', 6, 'e', 'e', 'e', 3, 'e', 'e'], 
      [7, 'e', 'e', 9, 'e', 1, 'e', 'e', 4],
      [5, 'e', 'e', 'e', 'e', 'e', 'e', 'e', 2],
      ['e', 'e', 7, 2, 'e', 6, 9, 'e', 'e'], 
      ['e', 4, 'e', 5, 'e', 8, 'e', 7, 'e']]

def rule1(arr):
    number=[1,2,3,4,5,6,7,8,9]
    hash1=sudoku_a.form_hash()
    #print hash1
    possible_hash={}
    for i in range(9):
        for j in range(9):
            possible_hash[(i,j)]=[]
            neighbours=hash1[(i,j)][:]
            temp_list=[]
            for elem1 in neighbours:
                temp_list.append(arr[elem1[0]][elem1[1]])
            for t in number:
                if t not in temp_list and arr[i][j]=='e':
                    possible_hash[(i,j)].append(t)
                #else:
                    #possible_hash[(i,j)].append(arr[i][j])
    for i in range(9):
        for j in range(9):
            if len (possible_hash[(i,j)])==1:
                arr[i][j]=possible_hash[(i,j)][0] 
                possible_hash[(i,j)]=[]
                rule1(arr)
    return possible_hash             
    

def rule2(arr):
    rule1(arr)
    possible_hash=rule1(arr)
    #print possible_hash
    hash1=sudoku_a.form_hash()
    for i in range(9):
        for j in range(9):
            neighbours=hash1[(i,j)][:]
            temp_ref=possible_hash[(i,j)][:]
            temp_ref_elem=[]
            temp_ref_fin=[]
            for elem in neighbours:
                temp_ref_elem=temp_ref_elem+possible_hash[elem]
            for t in temp_ref:
                if t not in temp_ref_elem:
                    temp_ref_fin.append(t)   
            if (len(temp_ref_fin)==1):
                #print "hello"
                arr[i][j]=temp_ref_fin[0]
                rule2(arr)         
                    
                
                    

'''rule1(arr) 
for i in arr:
    print i      
                  
print "yo"
            
for i in arr:
    print i      
  
    
            
        
    
'''

    
rule2(arr) 
for i in arr:
    print i         

