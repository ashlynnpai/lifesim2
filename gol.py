cells = [[1,0,0],
         [0,1,1],
         [1,1,0]]

generations = 1


def get_generation(cells, generations):
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
            print "i" + str(i)
            print "j" + str(j)
            print total
            print "---"

# got total counts working

# put totals into a dict

#update the board
