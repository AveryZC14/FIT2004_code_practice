from data_structures.referential_array import ArrayR
from linked_list_countingsort import LinkedList

#simple implementation of just numbers
def counting_sort_simple(items,max = None):
    length = len(items)
    if max == None:
        max = 0
        for i in items:
            if i > max:
                max = i
    count_array = [0 for _ in range(max+1)]
    for i in items:
        try:
            count_array[i]+= 1
        except:
            raise KeyError("Max value provided exceeded by input data")
    final = []
    for i,j in enumerate(count_array):
        if j > 0:
            final = final + ([i]*j)
    return final

#implementation of counting sort with objects now innit
def counting_sort_linkedlist(items,key_func = (lambda x:x),max_key = None):
    length = len(items)
    if length <= 1:
        return items
    if max_key == None:
        try:
            max_key = int(key_func(items[0]))
            #   print("MK",max_key)
        except:
            raise ValueError("given key function does not return integer, if you didnt give one then your values are not integers")
        for i in items:
            if int(key_func(i)) > max_key:
                max_key = key_func(i)
    count_array = [None for _ in range(max_key+1)]
    for i in items:
        key = key_func(i)
        if count_array[key] == None:
            count_array[key] = LinkedList()
        count_array[key].append(i)
        
    final = []
    for i in count_array:
        if i != None:
            for _ in range(len(i)):
                # print("i:"+str(i))
                final.append(i.pop_head())
    return final

def counting_sort_stable(items,key_func = (lambda x:x),max_key = None):
    length = len(items)
    if length <= 1:
        return items
    if max_key == None:
        # sussy = key_func(items[0])
        # print(key_func(items[0]))
        try:
            max_key = int(key_func(items[0]))
            #   print("MK",max_key)
        except:
            # print("ITE",items[0])
            # print("VALU",key_func(items[0]))
            raise ValueError("given key function does not return integer, if you didnt give one then your values are not integers")
        for i in items:
            if int(key_func(i)) > max_key:
                max_key = key_func(i)
    count_array = [0 for _ in range(max_key+1)]
    # position = count_array.copy()
    final = [None for _ in range(len(items))]
    for i in items:
        key = key_func(i)
        count_array[key] += 1
    # position[0] = 0
    temp = count_array[0]
    temp_temp = 0
    count_array[0] = 0
    for n in range(1,len(count_array)):
        temp_temp = count_array[n]
        count_array[n] = temp + count_array[n-1]
        temp = temp_temp
        
        # position[n] = position[n-1]+count_array[n-1]
    # count_array = position
        
    for i in items:
        key = key_func(i)
        # final[position[key]] = i
        # position[key] += 1
        # print("key",key,"CA",count_array)
        final[count_array[key]] = i
        count_array[key] += 1
    return final


    
    

class apple:
    def __init__(self,value,name):
        self.value = value
        self.name = name
    def __str__(self):
        return(f"I'm {self.name}, my value is {self.value}")

def l(lst):
    lst[1] = 3234
    return lst


if __name__ == "__main__":
    print(f"counting_sort simple! {counting_sort_simple([5,3,4,2,1,6,3],6)}")
    print(f"counting_sort ll! {counting_sort_linkedlist([5,3,4,2,1,6,3],(lambda x:x))}")

    apples = [
        apple(92,"Clauds"),
        apple(58,"Av"),
        apple(5,"john"),
        apple(2,"jack"),
        apple(3,"billian"),
        apple(7,"mcfritter"),
        apple(6,"yummers"),
        apple(0,"bobsled"),
        apple(12,"Damien milacki"),
        apple(44,"fig"),
        apple(6,"robert'); DROP TABLE STUDENTS; COMMIT; --"), 
        apple(23,"heehaw")]

    # newline = "\n"

    print(f"counting_sort better! {list(map((lambda a:[print(str(a)),str(a)][-1]),counting_sort_stable(apples,(lambda a:a.value))))}")
    # print(f"counting_sort better!! {counting_sort(apples,(lambda a:a.value))}")
    
    
    # l1 = [1,2,3,4,5]
    # l2 = l(l1)
    # l1[2] = 696969
    # print(l1,l2)
    
