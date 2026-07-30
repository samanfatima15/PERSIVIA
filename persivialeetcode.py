#TWO SUM QUESTION
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return[i,j]
                
#PALINDROME NUM QUESTION
def palindrome(numgiven):
    numberstring=str(numgiven)
    reversed= numberstring[::-1] #start from back n all the way to first number 
    if numberstring==reversed:
        print("Number is palindrome")
        return True
    else:
        print("Number is NOT palindome")
        return False

#Longest Common Prefix 
def commonprefix(words):
    if len(words)== 0:
        return "" # when no word no prefix so empty string
    firstword=words[0] 
    for i in range(len(firstword)):
        for word in words[1:]:
            if (i>=len(word)) or (word[i]!=firstword[i]):
                return firstword[:i]
    print("ALL WORDS IN STRING MATCH ")
    return firstword     

#LENGHT OF LAST WORD
def lastwordlen(sentence):
    words= sentence.split()
    lastword=words[-1]
    answer= len(lastword)
    return answer


# squareroot of number without using sqrt()
def squareroot(number):
    i=0
    while i*i <=number :
        i=i+1 
    return i-1

