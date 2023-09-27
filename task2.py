import random
from itertools import groupby
from task1 import task1

class task2(task1):
    def __init__(self) -> None:
        super  ().__init__()
        pass
    
    def get_customers_psevdoID(self, customer_nuber, first_id):
        list_id = []
        list_id.append (self.sum_of_digits(first_id))
        try:
            n_customers = int (customer_nuber)
            for i in range (n_customers):
                ID = random.randint(1,10000000)
                if ID >= first_id:
                    sum_id = self.sum_of_digits(ID)
                    list_id.append(sum_id)
        except:
            print ('Wrong customer nuber')
            pass
        return list_id
    
    def group_checker (self, my_list):
        if type (list_id) == int: raise 'Sorry, smth get wrong'
        list_id.sort()
        for i,j in groupby(list_id):
            group = list(j)
            group_member_counter = len(group)
            print('In group: ', group[0],'-', group_member_counter, 'people')


""" 

На вход функциии get_customers_psevdoID подается число клиентов и стартовый ID клиента в последовательности, условно находящегося в БД.
Затем функция условно генерирует список всех ID клиентов, состоящий из случайных чисел.
С помощью условия происходит отсев значений, находящихся условно выше по списку (в последовательности).
Затем с помощью функции group_checker, происходит подсчет числа клиентов в каждой группе.

""" 

if __name__ == '__main__':

    list_id = task2().get_customers_psevdoID(50000, random.randint(1,10000000))
    task2().group_checker (list_id)