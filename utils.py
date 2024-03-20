from matplotlib import pyplot as plt

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