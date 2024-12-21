def solution(S):
    #use an empty list to store the current checked parentheses
    current=[]
    #iterate through the string S to check the parentheses
    for ele in S:
    #if the current parenthesis is right bracket,append it to the list
        if ele =='(':
            current.append(ele)
    #if the current parenthesis is left bracket and the list is empty, return 0
        elif ele==')' and len(current)==0:
            return 0
    #if the current parenthesis is left bracket and the list is not empty, remove the last element of the list
        else:
            current.pop()
    #if the number of right bracket match the number of left bracket, i.e., the current list is empty, return 1
    if len(current)==0:
        return 1
    #if the left right number do not match, return 0
    else:
        return 0
