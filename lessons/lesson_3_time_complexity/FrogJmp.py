#method 1
def solution(X, Y, D):
    if (Y-X)/D > (Y-X)//D:
        return int((Y-X)//D+1)
    else:
        return int((Y-X)/D)

#method 2
def solution(X, Y, D):
    if X==Y:
        return 0
    q=(Y-X)//D
    r=(Y-X)%D
    if r==0:
        return q
    else:
        return q+1
