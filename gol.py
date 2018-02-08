cells = [[1,0,0],
         [0,1,1],
         [1,1,0]]

generations = 1

# got total counts working
    #handle index error, handle -1 problem

# put totals into a dict

#update the board

#if 2 or 3 neighbors and cell is alive, keeps living
#no change in state, do nothing
#if 3 neighbors and cell is dead, comes alive

#cell dies if less than 2 or greater than 3 neighbors


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
                    except IndexError:
                        pass
            k = str(i) + str(j)
            tracker[k] = [cells[i][j], total]
    for arr in tracker.values():
        if arr[1] == 3:
            arr[0] = 1
        elif arr[1] < 2 or arr[1] > 3:
            arr[0] = 0
    for item in tracker:
        cells[int(item[0])][int(item[1])]=tracker[item][0]
    return cells



get_generation(cells, generations)
