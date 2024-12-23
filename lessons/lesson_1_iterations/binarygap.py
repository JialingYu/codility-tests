#method 1, time complexity O(N)
def solution(N):
    """
    input an integer N, convert it into a binary string and return the length of the largest string of zeros between 1 and 1
    """
    # get the binary expression 
    # start from the third character to get rid of '0b'
    binary = bin(N)[2:]
    # set a variable to store the largest gap
    largest_gap =0
    # set a variable to count the gap
    zero_counter = 0
    # loop over the binary expression
    for char in binary:
        # if the char is 1
        if char == '1':
            # compare the largest gap and the current gap
            # store the larger one
            largest_gap = max(largest_gap, zero_counter)
            # reset the counter to zero
            zero_counter = 0
        # if the current character is zero 
        else:
            # start the counting
            # keep counting until the char is 1
            zero_counter += 1
    return largest_gap

#method 2
def solution(N):
    # Implement your solution here
    b=bin(N)
    zeros=b.split('1')
    if len(zeros)==2:
        return 0
    else:
        #get rid og '0b' and the last portion of zeros
        zeros=zeros[1:-1]
        m=0
        for ele in zeros:
            m=max(m,len(ele))
    return m
                            
                            
