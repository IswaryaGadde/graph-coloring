# comlete acyclic graph - tree
# tree with n nodes willhave n-1 edges
# n points; n-1 edges; no cycles; is a tree
# complete graph = n^2 edges; n points
# graphs are not euclidean 
import sys
import math
#import numpy as np



    
def dis_euc(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


if __name__ == '__main__':
    # mydict={}
    # with open('input.txt', 'r') as f:
    #     for line in f:
    #         print(line)



    lis_mat = [[1, 1],
               [2, 2],
               [2, 4]]
     
    adj_dict=[]

    for i in range(0,len(lis_mat)):
        for j in range(i+1,len(lis_mat)):
            
            adj_dict.append([i,j, dis_euc(lis_mat[i],lis_mat[j])])

    print(adj_dict)
    visted = []
    result=0
    adj_dict.sort(key = lambda adj_dict: adj_dict[2])
    print("sorted", adj_dict)
    for i in adj_dict:
        if i[0] not in visted or i[1] not in visted:
            result += i[2]
            visted.append(i[0])
            visted.append(i[1])
    print("result=",result)
        

