from collections import defaultdict 

# алгоритм группировки
def f(id):
    return sum(map(int,str(id)))

# Функция, которая подсчитывает число покупателей, 
# попадающих в каждую группу, 
# если нумерация ID сквозная и начинается с 0. 
# На вход функция получает целое число n_customers (количество клиентов).
def function1(n_customers):
    customer_counts = defaultdict(int)
    for i in range(n_customers):
        customer_counts[f(i)] += 1
    return customer_counts

# Функция, аналогичная первой, если ID начинается с произвольного числа. 
# На вход функция получает целые числа: n_customers (количество клиентов)
#  и n_first_id (первый ID в последовательности).
def function2(n_customers,n_first_id):
    customer_counts = defaultdict(int)
    for i in range(n_first_id,n_first_id+n_customers):
        customer_counts[f(i)] += 1
    return customer_counts
