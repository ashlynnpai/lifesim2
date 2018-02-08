cells = [[1,0,0],
         [0,1,1],
         [1,1,0]]

generations = 1

#current state
#neighbor current
#final state
#tracker = {'00': [1]}


def get_generation(cells, generations):
    tracker = {}
    for i, row in enumerate(cells):
        for j, num in enumerate(row):
            total = 0
            rows = [i-1, i, i+1]
            columns = [j-1, j, j+1]
            for r in rows:
                for c in columns:
                    try:
                        if r != -1 and c != -1:
                            if r == i and c == j:
                                total += 0
                            elif cells[r][c] == 1:
                                total += 1

                    except:
                        print "oor"

            k = str(i) + str(j)
            tracker[k] = [cells[i][j], total]
    print tracker

# got total counts working
    #handle index error, handle -1 problem
#try to go for list comprehension before the logic is worked out

# put totals into a dict

#update the board
    updates = {}
    for item in tracker:
        pass
        #if 2 or 3 neighbors and cell is alive, keeps living
        #no change in state, do nothing
        #if 3 neighbors and cell is dead, comes alive

        #cell dies if less than 2 or greater than 3 neighbors
