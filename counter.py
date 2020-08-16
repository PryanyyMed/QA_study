#пузырьковая сортировка
def bubble_sort(A):
    switch = False
    counter = 0
    while not switch:
        switch = True
        for i in range(0,len(A)-1):
            if A[i] < A[i+1]:
                switch = False
                A[i], A[i+1] = A[i+1], A[i]
                counter += 1
    print('Кол-во перестановок методом пузырька: ', counter)
    return A

#метод вставки
def insertion_sort(A):
    counter_1 = 0
    for i in range (1, len(A)):
        while A[i-1] > A[i] and i > 0: 
            A[i], A[i-1] = A[i-1], A[i]
            i = i-1 
            counter_1 +=1
    print('Кол-во перестановок методом вставки: ', counter_1)
    return A
            
A=[93, 12, 67, 77, 12, 81, 88, 58, 72, 55]

bubble_sort(A)
insertion_sort(A)
print (', '.join(map(str, A)))