# ----------Pascal's Triangle 1
def generate( numRows):
    data = []
    count = 0
    for i in range(numRows):

        curr = []
        for j in range(i+1):
            if j == 0 or j == i:
                curr.append(1)
            else:
                curr.append(data[i-1][j-1]+data[i-1][j])


        data.append(curr)
        count+=1

    return data,count


# ---------Pascal's Trianlge 2 

def getRow(rowIndex):
        result = []
        for i in range(rowIndex+1):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(result[i-1][j-1]+result[i-1][j])
            result.append(curr)
        
        return result[-1]


res = generate(5)
print(res,"Triangle")

res2 = getRow(3)
print(res2,"Triangle 2")