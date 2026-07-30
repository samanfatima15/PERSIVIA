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


#MEDIUM QUESTIONS
#REVERSE NUMBER it shoudlnt exceed SIGNED BIT 32 number
def reversed(x):
    negative=False
    if x< 0:
        negative= True
        x=-x #making positive temporaily for ez/simpler operations ahead
    stringnumber=str(x)
    reversednum=stringnumber[::-1]
    answer=int(reversednum)
    if negative:
        answer=-answer

    if answer <-2147483648 or answer > -2147483648:
        return 0
    return answer

#SUM OF THREE NUM
def threeSumClosest(self, nums, target):

        sumofnum = (nums[0] + nums[1] + nums[2])
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                 for k in range(j + 1, len(nums)):

                    current_sum = (nums[i] + nums[j] + nums[k])

                    if abs((current_sum) - (target)) < abs((sumofnum) - target):
                        sumofnum = current_sum

        return sumofnum
