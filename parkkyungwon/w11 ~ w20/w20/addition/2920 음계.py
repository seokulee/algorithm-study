def is_sorted(arr, ran):
    for att, num in zip(arr, ran):
        if att != num: return False
    
    return True


def sol(arr):
    match arr[0]:
        case 1: 
            if is_sorted(arr[1:], range(2, 9)): return 'ascending'
        case 8: 
            if is_sorted(arr[1:], range(7, 1, -1)): return 'descending'
    
    return 'mixed'
    
        
arr = tuple(map(int, input().split()))
print(sol(arr))
