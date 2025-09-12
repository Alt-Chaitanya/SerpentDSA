#Two pointer method
arr=[4, 5, 2, 99, 22, 88]
arr.sort()
#2,4,5,22,88,99
print(arr)

t=110 #target value

L=0
R=len(arr)-1


while L<R: #if it was L>R it would've skipped the code 
    sum=arr[L]+arr[R]

    if sum==t:
        print(f"Sum found at indexes: {L} and {R}.")
        break
        
    elif sum<t:
        L=L+1
        
    elif sum>t:
        R=R-1
        
    else:
        print("Sum not found")    
                 