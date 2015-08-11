'''
Created on 28-Apr-2014

@author: savs95
'''

def form_hash():# returns neighbor list
    hash1={} 
    for i in range (0,9):
        for j in range (0,9):
            hash1[(i,j)]=[]
            for t in range (0,9):
                if(t!=j):
                    hash1[(i,j)].append((i,t))
            for t in range (0,9):
                if(t!=i):
                    hash1[(i,j)].append((t,j))
            a=(i/3)*3
            b=(j/3)*3
            for t in range (a,a+3):
                for p in range (b,b+3):
                    if (t,p) not in hash1[(i,j)]:
                        if(t!=i and p!=j):
                            hash1[(i,j)].append((t,p))
    return hash1   


def bfs((i,j), hash1):
    queue, bfs_order =[],[]
    queue=hash1[(i,j)][:]
    bfs_order.append((i,j))
    while len(queue)!=0:
        elem=queue[0]
        del(queue[0])
        for f in hash1[elem]:
            if f not in queue and f not in bfs_order:
                queue.append(f)
        bfs_order.append(elem)    
    return bfs_order

def dfs((i,j), hash1):
    stack, bfs_order =[],[]
    stack=hash1[(i,j)][:]
    #print i,j
    bfs_order.append((i,j))
    while len(stack)!=0:
        elem=stack[-1]
        del(stack[-1])
        for f in hash1[elem]:
            if f not in stack and f not in bfs_order:
                stack.append(f)
        bfs_order.append(elem)    
    return bfs_order
        
           
                
def colouring (bfs_order,hash1):
    bfs_colour=[]
    elements=[]
    #print len(bfs_order)
    colour=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    for elem in bfs_order:
        #print elem
        #print len(bfs_colour)
        used_colours=[]
        if len(bfs_colour)==0:
            bfs_colour.append(1)
            #temp_colour.append(1)
            elements.append(elem)
        else:
            for t in elements:
                if elem in hash1[t]:#agar neighbour hai 
                    used_colours.append(bfs_colour[elements.index(t)])
            for t in colour:
                if t not in used_colours:
                    bfs_colour.append(t)
                    elements.append(elem)
                    break
    return bfs_colour                
                    

hash1={}      
count_arr=[] 
maxi_arr=[] 
hash1=form_hash()
#print hash1
'''for i in range (9):
    for j in range (9):
        count=0
        temp=colouring(dfs((i,j), hash1),hash1)
        maxi=max(temp)
        for c in temp:
            if (c>9):  
                count+=1
        count_arr.append(count)  
        maxi_arr.append(maxi)  
print min(maxi_arr)
a=maxi_arr.index(min(maxi_arr))
print count_arr(a)
'''
#a=colouring((dfs((0,0),hash1)),hash1)
#print max(a)
count1,count2=0,0    
lst,lst2=[],[]                
for i in range(9):
    for j in range(9):
        d=colouring((dfs((i,j),hash1)),hash1)
        b=colouring((bfs((i,j),hash1)),hash1)
        d1=max(d)
        b1=max(b)
        if d1==12:
            for t in range(81):
                if d[t]>9:
                    count1+=1
        if b1==12:
            for t in range(81):
                if b[t]>9:
                    count2+=1            
        m=max(d1,b1)
        if (count1==0 and count2!=0):
            lst2.append(count2)
        elif (count1!=0 and count2==0):
            lst2.append(count1)
        elif (count1!=0 and count2!=0):
            f=min(count1,count2)
            lst2.append(f)
        else:
            continue    
        lst.append(m)

print min(lst)
print min(lst2)



        
        
                
        
        
    
