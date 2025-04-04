# Given the participants' score sheet for your University Sports Day,  
# you are required to find the runner-up score.  
# You are given 'n' scores. Store them in a list and find the score of the runner-up.  

# Input Format  
# The first line contains an integer 'n', the number of scores.  
# The second line contains an array of 'n' integers, each separated by a space.  

# Constraints  
# 2 <= n <= 100  
# -100 <= A[i] <= 100  

# Output Format  
# Print the runner-up score.  

# Sample Input  
# 5  
# 2 3 6 6 5  

# Sample Output  
# 5  

# Explanation  
# Given list is [2, 3, 6, 6, 5].  
# The maximum score is 6, and the second maximum (runner-up) is 5.  
# Hence, we print 5 as the runner-up score.



participants = int(input("enter the number of participents: "))
if 2 <= participants and participants  <= 10:
    scores = list(range(participants))
    for i in scores:
        scores[i]=int(input(f"enter the score of {i} participant: "))

    print(scores)
    winner = 0
    for i in scores:
        if i > winner:
            winner = i

    print(f"winner:{winner}")
    runner = 0
    for i in scores:
        if i == winner:
            continue 
        elif i > runner:
            runner =i
        
    print(f"second highest score is : {runner}")        
else:
    print("print a valid participants number in range (2 <= participants <= 100) ")
