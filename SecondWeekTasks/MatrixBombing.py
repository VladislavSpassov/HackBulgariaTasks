    def matrix_bombing_plan(m):
        result = {}
        s = 0
        for index,row in enumerate(m):
            for i,col in enumerate(row):
                s += col

        for index,row in enumerate(m):
            for i,col in enumerate(row):
                su = s
                lstngb = get_neighbors(index,i,m)
                current = []
                for x in lstngb:
                    if(x >= m[index][i]):
                        x = x - m[index][i]
                        current.append(x)
                    else:
                        x = 0
                        current.append(x)
                result[(index,i)] = su - (sum(lstngb) - sum(current))
        print(result)


    def get_neighbors(a, b,matrix):
        d = {(i, c):matrix[i][c] for i in range(len(matrix)) for c in range(len(matrix[0]))}
        return list(filter(None, [d.get(i) for i in
        [(a+1, b+1), (a, b+1), (a+1, b), (a-1, b+1), (a-1, b), (a, b-1), (a+1, b-1),(a-1,b-1)]]))

       
    matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


    def f():
        print(list(filter(None,[1,21,41,412,5,5,5,None,5,5])))
    f()