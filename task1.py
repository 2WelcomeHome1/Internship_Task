from itertools import groupby



class task1():
    def __init__(self) -> None:
        pass

    def sum_of_digits(self,num): #  суммирует цифры в числе (в id)
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    
    def get_customers_psevdoID(self, n_customers): #генерирует набор случайный ID в зависимости от числа клиентов.
        list_id = []
        try:
            n_customers = int (n_customers)
            for i in range(1, n_customers+1):
                get_id = int('{:07}'.format(i))
                sum_id = self.sum_of_digits(get_id)
                list_id.append(sum_id)
        except:
            list_id = 0
        return list_id 
    
    def group_checker (self, my_list): #группирует клиентов
        if type (my_list) == int:
            raise 'Sorry, smth get wrong'
        my_list.sort()
        for i,j in groupby(my_list):
            group = list(j)
            group_member_counter = len(group)
            print('In group: ', group[0],'-', group_member_counter, 'people')

""" 
На вход функциии get_customers_psevdoID подается число клиентов, условно находящихся в БД. 
Функция генерирует необходимый объем псевдоИД со сквозной нумерацией, начинающейся с 0000001. 
Затем с помощью функции group_checker, происходит подсчет числа клиентов в каждой группе.

"""

if __name__ == '__main__':
    list_id = task1().get_customers_psevdoID(50000)
    task1().group_checker (list_id)