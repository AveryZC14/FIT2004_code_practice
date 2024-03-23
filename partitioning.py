from matplotlib import pyplot as plt
import random

def plot(lst):
    lii = [46, 11, 9, 20, 3, 15, 8, 63, 11, 9, 24, 3, 5, 45, 51, 2, 23, 9, 17, 1, 1, 37, 29, 6, 3, 9, 25, 5, 43]

    # # This is a list of unique values appearing in the input list
    # lii_unique = list(set(lii))

    # This is the corresponding count for each value
    # counts = [lii.count(value) for value in lst]
    
    

    barcontainer = plt.bar(range(len(lst)),lst)

    # Some labels and formatting to look more like the example
    plt.bar_label(barcontainer,lst, label_type='edge')
    plt.axis('off')
    plt.show()

def hoare_partition(lst,p = None):
    if p == None:
        # low,mid,high = (lst[0],lst[len(lst)//2],lst[-1])
        # p = (low if low > mid and low < high else (mid if low < mid else high))
        
        # low,mid,high = (0,len(lst)//2,len(lst)-1)
        # p = (low if (lst[low] > lst[mid] and lst[low] < lst[high]) or (lst[low] > lst[high] and lst[low] < lst[mid]) else (mid if lst[low] < lst[mid] else high))
        cands = [(0,lst[0]),(len(lst)//2,lst[len(lst)//2]),(len(lst)-1,lst[len(lst)-1])]
        cands.sort(key=(lambda i:i[1]))
        p = cands[1][0]
        # print(p)
    lst[0],lst[p] = lst[p],lst[0]
    p_val = lst[0]
    # print("p",p,p_val)
    left = 1
    right = len(lst)-1
    # print(lst)
    while left <= right:
        if lst[left] <= p_val:
            left += 1
            # print("l",left)
        elif lst[right] >= p_val:
            right -= 1
            # print("rr",right)
        else:
            lst[left],lst[right] = lst[right],lst[left]
            # print(lst)
    lst[0],lst[right] = lst[right],lst[0]
    return lst

def dutch_flag_partition(lst,p = None,low = None,high = None):
    # if len(lst) <= 1:
    #     return lst,None,None
    low = low if low else 0
    high = high if high else len(lst)-1
    if p == None:
        # low,mid,high = (lst[0],lst[len(lst)//2],lst[-1])
        # p = (low if low > mid and low < high else (mid if low < mid else high))
        
        # low,mid,high = (0,len(lst)//2,len(lst)-1)
        # p = (low if (lst[low] > lst[mid] and lst[low] < lst[high]) or (lst[low] > lst[high] and lst[low] < lst[mid]) else (mid if lst[low] < lst[mid] else high))
        cands = [(low,lst[low]),((low+high+1)//2,lst[(low+high+1)//2]),(high,lst[high])]
        cands.sort(key=(lambda i:i[1]))
        p = cands[1][0]
    p_val = lst[p]
    blue = white = low
    # white = 0
    red = high
    while white <= red:
        if lst[white] < p_val:
            lst[white],lst[blue] = lst[blue],lst[white]
            blue += 1
            white += 1
        elif lst[white] > p_val:
            lst[red],lst[white] = lst[white],lst[red]
            red -= 1
        else:
            white += 1
    return (lst,blue,white)

def dutch_flag_partition_rand(lst,p = None,low = None,high = None):
    # if len(lst) <= 1:
    #     return lst,None,None
    low = low if low else 0
    high = high if high else len(lst)-1
    if p == None:
        # low,mid,high = (lst[0],lst[len(lst)//2],lst[-1])
        # p = (low if low > mid and low < high else (mid if low < mid else high))
        
        # low,mid,high = (0,len(lst)//2,len(lst)-1)
        # p = (low if (lst[low] > lst[mid] and lst[low] < lst[high]) or (lst[low] > lst[high] and lst[low] < lst[mid]) else (mid if lst[low] < lst[mid] else high))
        p = random.randint(low,high)
    p_val = lst[p]
    blue = white = low
    # white = 0
    red = high
    while white <= red:
        if lst[white] < p_val:
            lst[white],lst[blue] = lst[blue],lst[white]
            blue += 1
            white += 1
        elif lst[white] > p_val:
            lst[red],lst[white] = lst[white],lst[red]
            red -= 1
        else:
            white += 1
    return (lst,blue,white)
        
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
    
    
    
    
    


# def partition_random_pivot():
    


if __name__ == "__main__":
    lst1 = [1,8,2,6,4,8,4,12,32,14,18,43]
    lst2 = [12,9,2,8,3,7,4,6,5,5,1,7]
    lst3 = [99,12,82,28,83,48,85,68,75,38,94,27,39,4,93,27,46,53,12,22,1,44,44,44,44]
    # print(dutch_flag_partition(lst1))
    # plot(dutch_flag_partition(lst1))
    print(quick_sort(lst3))
    plot(quick_sort(lst3))