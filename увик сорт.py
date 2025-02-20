def quick_sort(x):
    if len(x)<=1:
        return x
    else:
        pivot = x[0]
        l = [i for i in x[1:] if i < pivot]
        r = [i for i in x[1:] if i >= pivot]
        return quick_sort(l) + [pivot] + quick_sort(r)