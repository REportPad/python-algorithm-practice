def Big_Number_Rule(n,m,k,arr):
    arr.sort()
    first = arr[n-1]
    second = arr[n-2]
    
    count = (m//(k+1)) * k
    count += m % (k+1)
    
    result = 0
    result += count * first
    result += (m-count) * second
    
    return result
