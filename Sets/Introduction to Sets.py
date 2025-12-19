def average(array):
    distinct = set(array)
    average = sum(distinct) / len(distinct) 
    return round(average, 3)
