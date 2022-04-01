import copy

list_inp = [[2,1,1],[1,1,0],[0,1,1]]
print(list_inp)

list_t = list_inp.copy()
rotten = list()
count_loop = 0
found_fresh = True

while found_fresh == True:
    # get indexes of all the rotten ones
    for i, inner_1 in enumerate(list_t):    
        for j, inner_2  in enumerate(inner_1):
            if inner_2 == 2:
                rotten.append([i,j])

    # Check if fresh have in proximity on rotten
    for i, inner_1 in enumerate(list_t):
        for j, inner_2  in enumerate(inner_1):
            # By comparing indexes
            if (inner_2 == 1) and ( ([i-1,j] in rotten) or ([i+1,j] in rotten) or ([i,j-1] in rotten) or ([i,j+1] in rotten) ):
            
                # If conditiion true, change 1 to 2
                list_t[i][j] = 2
    
    # Check of there is any fresh. If no fresh, then found fresh == False:
    found_fresh = False
    for i, inner_1 in enumerate(list_t):
        for j, inner_2  in enumerate(inner_1):
            if inner_2 == 1:
                found_fresh = True
    count_loop += 1
    print(list_t)

print(count_loop )

