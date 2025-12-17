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

import string

def oddString(words):
        letter = {letter: index for index, letter in enumerate(string.ascii_lowercase)}
        res = []
        for i in range(len(words)):
            curr = []
            n = len(words[i])
            for j in range(n-1):
                a = letter[words[i][j]]
                b = letter[words[i][j+1]]
                curr.append(b-a)
            res.append(curr)
        count = None
        for i in range(len(res)):
            count = 0
            for j in range(len(res)):
                if res[i] == res[j]:
                    count += 1
            if count == 1:
                return words[i]
        # return count
        return res,words[count]


res = generate(5)
print(res,"Triangle")

res2 = getRow(3)
print(res2,"Triangle 2")

words = ["adc","wzy","abc"]
words2 = ["jijij","yxyxy","edede","edede","bbaaa","kjkjk"]
# ["aaa","bob","ccc","ddd"]
print(len(words[0]))
val = oddString(words2)
print(val,"values")