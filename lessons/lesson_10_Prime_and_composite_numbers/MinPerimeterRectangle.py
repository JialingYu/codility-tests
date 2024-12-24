#O(sqrt(N))
def solution(N):
    #the length of sides of the rectangle should be a divisor of N
    #the length of a smaller side should be <= sqrt(N)
    #iterate through all the possible length to find the minimal perimeter
    #initialize the minimal perimeter
    m=2*(1+N)
    i=1
    while i*i <=N:
        if N%i==0:
            peri=2*(i+N/i)
            m=min(m,peri)
        i+=1
    return int(m)

