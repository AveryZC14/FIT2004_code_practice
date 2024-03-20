from partitioning import dutch_flag_partition
from utils import plot

def quick_sort(lst,low = None, high = None,p = None):
    
    if low == None:
        low = 0
    if high == None:
        high = len(lst)-1
    if low >= high:
        return lst
    # if high <= low:
    #     return
    lst,blue,white = dutch_flag_partition(lst,None,low,high)
    quick_sort(lst,low,blue-1)
    quick_sort(lst,white,high)
    return lst

def quick_select(lst,k,low = None, high = None,p = None):
    if low == None:
        low = 0
    if high == None:
        high = len(lst)-1
    if low >= high:
        return lst[high]
    lst,blue,white = dutch_flag_partition(lst,None,low,high)
    if k < blue:
        return quick_select(lst,k,low,blue-1)
    elif k >= white:
        return quick_select(lst,k,white,high)
    else:
        return lst[blue]

    
    
    
    
    


# def partition_random_pivot():
    


if __name__ == "__main__":
    lst1 = [1,8,2,6,4,8,4,12,32,14,18,43]
    lst2 = [12,9,2,8,3,7,4,6,5,5,1,7]
    lst3 = [99,12,82,28,83,48,85,68,75,38,94,27,39,4,93,27,46,53,12,22,1,44,44,44,44]
    # print(dutch_flag_partition(lst1))
    # plot(dutch_flag_partition(lst1))
    print(quick_sort(lst3))
    # plot(quick_sort(lst3))
    
    print(quick_select(lst3,19))