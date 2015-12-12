global result
n=9
results =[]
result=[0]*n

def ch(k):
    for j in range(k):
        if result [k] == result [j] or result [k] == result[j] - (k-j) or result [k] == result[j] + (k-j):
            return False
    return True 
def search(k):
    if k < n:
        for i in range(n):
            
            result[k]=i 
            if ch(k):
#                 print result
                search(k+1)
    
    else:
        #print "solved", result
        results.append (result[:])

search(0)
#print results
print len (results)
