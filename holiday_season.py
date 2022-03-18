#string x of length N
string_length = int(input())
#string consists of small english letter
letters = [t for t in input()]
#print(letter)
sum_result = 0
for a in range(string_length-3):
    for c in range(a+1,string_length-1):
#this will search for a == c
        if letters[a] == letters[c]:
            for b in range(a+1,c):
                for d in range(c+1, string_length):
                    if letters[b] == letters[d]:
                        # this checked if b == d and b < c
                        sum_result = sum_result + 1
                        #print(a,b,c,d)
#print result
print(sum_result)S