l=[['1','2','3','4','5','6','7','8','9'],['10','11','12','13','14','15','16','17','18'],['19','20','21','22','23','24','25','26','27'],['28','29','30','31','32','33','34','35','36'],['37','38','39','40','41','42','43','44','45'],['46','47','48','49','50','51','52','53','54'],['55','56','57','58','59','60','61','62','63'],['64','65','66','67','68','69','70','71','72'],['73','74','75','76','77','78','79','80','81']]
h={}
dfs_list=[]
c_hash={}

for i in range(1,82):
    h[i]=[]
    
for i in range(0,9):
    for j in range(0,9):
        a=0
        while(a<9):
            if(a!=j):
                h[int(l[i][j])].append(int(l[i][a]))
            a+=1
        b=0
        while(b<9):
            if(b!=i):
                h[int(l[i][j])].append(int(l[b][j]))
            b+=1
        a=0
        b=0
        a=i/3
        a=a*3
        b=j/3
        b=b*3
        c=a
        d=b
        while(c>=a and c<=a+2):
            d=b
            while(d>=b and d<=b+2):
                if(c!=i and d!=j):
                    h[int(l[i][j])].append(int(l[c][d]))
                d+=1
            c+=1

def dfs(u):
    dfs_list.append(u)
    if(len(dfs_list)==81):
        return
    l1=[]
    for i in h[u]:
        l1.append(int(i))
    while(1):
        x=min(l1)
        if(x not in dfs_list):
            dfs(x)
            break
        else:
            l1.pop(l1.index(x))

def color():
    for i in dfs_list:
        temp=[]
        for j in h[i]:
            if(j in c_hash):
                temp.append(c_hash[j])
        if(len(temp)==0):
            c_hash[i]=1
        else:
            for k in range(1,100):
                if(k not in temp):
                    c_hash[i]=k
                    break
  
def check():
    check1=[]
    for i in range(1,82):
        if(c_hash[i]>9):
            check1.append(c_hash[i])
    print check1
    print "check1"

# for i in range(1,82):
#     dfs(i)
#     color()
#     print i,"i"
#     check()
#     dfs_list=[]
#     c_hash={}

dfs(17)
print dfs_list
color()
check()