def solution(S):
    #create a dictionary to map strings to numbers
    #corresponding strings are the opposite number of each other
    d={'(':1,'[':2,'{':3,')':-1,']':-2,'}':-3}
    sto=[]
    #if len(S)=0, range(0) return an empty string, and thus the for loop is skipped
    for i in range(len(S)):
        #if the first on eis right bracket, return 0
        if i == 0 and d[S[i]]<0:
            return 0
        #if there exists a right bracket and sto is empty, return 0
        elif d[S[i]]<0 and len(sto)==0:
            return 0
        #if there exists a right bracket which is not the opposite of the former left bracket, return 0
        elif d[S[i]]<0 and d[S[i]]!=-sto[-1]:
            return 0
        elif d[S[i]]<0 and d[S[i]]==-sto[-1]:
            sto.pop()
        else:
            sto.append(d[S[i]])
    if len(sto)==0:
        return 1
    else:
        return 0
