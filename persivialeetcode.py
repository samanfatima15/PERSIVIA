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
