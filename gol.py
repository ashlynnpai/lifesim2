
def get_generation(cells, generations):
    tracker = {}
    if generations == 0:
        return cells
    for i, row in enumerate(cells):
        for j, num in enumerate(row):
            total = 0
            #find 8 neighbors
            rows = [i-1, i, i+1]
            columns = [j-1, j, j+1]
            for r in rows:
                for c in columns:
                    #keep within the board and don't count the original
                    try:
                        if r != -1 and c != -1:
                            if r == i and c == j:
                                pass
                            elif cells[r][c] == 1:
                                total += 1
                    except IndexError:
                        pass
            k = str(i) + str(j)
            #store cell values and neighbor totals in a dict using "ij" as keys
            #{'00': [1, 1], '01': [0, 3]}
            tracker[k] = [cells[i][j], total]
    #update cell values
    for arr in tracker.values():
        if arr[1] == 3:
            arr[0] = 1
        elif arr[1] < 2 or arr[1] > 3:
            arr[0] = 0
    for item in tracker:
        cells[int(item[0])][int(item[1])]=tracker[item][0]
    return get_generation(cells, generations-1)



get_generation(cells, generations)
