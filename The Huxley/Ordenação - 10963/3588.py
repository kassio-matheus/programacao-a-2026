qtd_array, qtd_ord = [int(i) for i in input().split()]
array = [int(i) for i in input().split()]

def bubble_sort (qtd_array, qtd_ord, array):
    execucoes = int(1)

    for _ in range (qtd_array - 1):
        for index in range(qtd_array - 1):
            if(array[index] > array[index + 1]):
                array[index], array[index + 1] = array[index + 1], array[index]

        print(array)

        if(execucoes == qtd_ord):
            break

        execucoes += 1

bubble_sort(qtd_array, qtd_ord, array)