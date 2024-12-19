def solution(N):
    x=1
    current=N
    min_pre=N+100
    while x < current:
        if N%x==0:
            pre=N/x + x
            min_pre=min(pre,min_pre)
        current=N/x
        x+=1
    return int(2*min_pre)
