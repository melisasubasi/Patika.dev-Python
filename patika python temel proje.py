#1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 
# Örnek olarak:
#input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#output: [1,'a','cat',2,3,'dog',4,5]
def flatten(lst):
    flattened_lst = []
    for item in lst:
        if isinstance(item, list):
            flattened_lst.extend(flatten(item))
        else:
            flattened_lst.append(item)
    return flattened_lst
#Bu fonksiyonu kullanarak, örnek girdimizi tersine döndürmeyi aşağıdaki gibi test edebiliriz:
input_lst = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattened_lst = flatten(input_lst)
print(flattened_lst)  # Output: [1,'a','cat',2,3,'dog',4,5]

#2-Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
# Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
# Örnek olarak:
#input: [[1, 2], [3, 4], [5, 6, 7]]
#output: [[[7, 6, 5], [4, 3], [2, 1]]

def reverse(lst):
    if isinstance(lst, list):
        return [reverse(item) for item in lst[::-1]]
    else:
        return lst

#Bu fonksiyonu kullanarak, örnek girdimizi tersine döndürmeyi aşağıdaki gibi test edebiliriz:

input_lst = [[1, 2], [3, 4], [5, 6, 7]]
reversed_lst = reverse(input_lst)
print(reversed_lst)  # Output: [[[7, 6, 5], [4, 3], [2, 1]]
