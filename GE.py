#usage: python3 GE.py

M=[[0,1,1,0,1,1,0],
  [1,2,0,0,0,1,0],
  [0,1,0,1,0,0,1],
  [1,1,0,1,0,0,0]]

def print_matrix(A):
    for l in A:
        print('\t'.join(["%0.3f" % e for e in l]))
    print("")

def print_matrix_latex(A):
    n=len(A[0])
    print("\\[\\left(\\begin{array}{"+"c"*n+"}")
    for l in A:
        print('&'.join(["%0.3f" % e for e in l])+"\\\\")
    print("\\end{array}\\right)\\]")

def switch(i, j, A):
    tmp=[s for s in A[i]]
    A[i]=[s for s in A[j]]
    A[j]=tmp
    print_matrix(A)
    
def scale(i, k, A):
    A[i]=[k*s for s in A[i]]
    print_matrix(A)
    
def scale_and_add(i, j, k, A):
    A[j]=[k*x+y for x, y in zip(A[i], A[j])]
    print_matrix(A)

def non_zero_idx(i, A):
    r=0
    for c in A[i]:
        if c!=0:
            return r
        r+=1
    return len(A[i])

def Gaussian_elimination(A):
    m=len(A)
    n=len(A[0])
    pivots=[]
    #Forward
    for i in range(m):
        j=i
        pivot=non_zero_idx(j, A)
        for k in range(i+1, m):
            if non_zero_idx(k, A)<pivot:
                j=k
                pivot=non_zero_idx(j, A)
        if pivot>=n:
            break
        switch(i,j,A)
        pivots+=[pivot]
        for j in range(i+1, m):
            scale_and_add(i, j, -((A[j][pivot])/(A[i][pivot])), A)
    print(pivots)
    #Backward
    for i in range(len(pivots)):
        p=pivots[i]
        scale(i, 1.0/A[i][p], A)
        for j in range(i):
            scale_and_add(i, j, -A[j][p], A)   
            
Gaussian_elimination(M)
        
