import pdb




def Matrix(rows, columns,lst,word):
    countWords = 0
    for r in range(len(lst)):
        currentRow = ""
        for c in range(len(lst[r])):
            currentRow += lst[r][c]
            
            
        print(currentRow)
        if(currentRow.find(word) != -1):
            countWords+=1


    print(countWords)


    for r in range(len(lst)):
        currentRow = ""
        c = len(lst[r]) - 1

        while(c >= 0):
            currentRow += lst[r][c]
            c -= 1
        if(currentRow.find(word) != -1):
            countWords += 1 
        print(currentRow)

    print(countWords)



## from bottom to top
    for c in range(columns):
        currentRow = ""
        r = len(lst) - 1
            
        while(r >= 0):
            
            currentRow += lst[r][c]

            r = r - 1 
        if(currentRow.find(word) != -1):
                countWords+=1
        

    lstDiagWords = []
    r = 0
    c = 0
    row = 0
    while(row < rows):
        r = row
        currentDiag = ""
        c = 0
        while(r < rows and c < columns):
            currentDiag += lst[r][c]
            
            r += 1
            c += 1
        row +=1
        lstDiagWords.append(currentDiag)
    r = 0
    c = 0
    col = 0
    while(col < columns):
        c = col
        currentDiag = ""
        r = 0
        while(r < rows and c < columns):
            currentDiag += lst[r][c]
            
            r += 1
            c += 1
        col +=1
        print(currentDiag)
        lstDiagWords.append(currentDiag)


    
Matrix(5,4,[["i","v",'a','n'],['e',"v","n","h"],["i","n","a","v"],["m","v","v","n"],["q","r","i","t"]],"ivan")




