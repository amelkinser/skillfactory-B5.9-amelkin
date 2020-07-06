##---------- B5.9 Домашнее задание на декораторы -----------------------------
##    Написать декоратор для измерения скорости работы функций
##    06.07.2020 г.
##    Группа: PWS-21.
##    Амелькин С.Б.
##----------------------------------------------------------------------------


import time

NUM_RUNS = 10
NUM_CNT = 1000000

#------------------- 1 Вариант. Декоратор-функция -------------------
def time_this1(num_runs=64): # num_runs - число запусков функции (по умолчанию-64)
    def decorator(func):     # func - функция, у которой нужно измерить скорость работы
        
        def func_wrapper(): # Здесь измеряется время работы функции "func"
                            # путём вызова её "num_runs" раз, замера времени и последующего осреднения
            full_time=0
            avg_time = 0
            for i in range(num_runs):
                t0 = time.time()        
                func()
                t1 = time.time()
                avg_time += (t1 - t0)
                full_time=avg_time
            avg_time /= num_runs # Cреднее время выполнения func()
            print("Выполнение заняло %.5f секунд" % avg_time)
            return 1
        
        return func_wrapper   
    return decorator

@time_this1(num_runs=NUM_RUNS) # Функция-обёртка - Декоратор
def f1(cnt=NUM_CNT): # Декорируемая функция
    for j in range(cnt):
        pass
#-------------------------------------------------------------------


#------------------- 2 Вариант. Декоратор-объект -------------------
class time_this2: # Класс для декоратора
   
    def __init__(self,num_runs=64): # num_runs - число запусков функции (по умолчанию-64)
        self.num_runs=num_runs
                
    def __call__(self, func): # func - функция, у которой нужно измерить скорость работы
        def wrap(*args):  # Здесь измеряется время работы функции "func"
                          # путём вызова её "num_runs" раз, замера времени и последующего осреднения
            avg_time = 0
            for i in range(self.num_runs):
                t0 = time.time()        
                func(*args)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs # Cреднее время выполнения func()
            print("Выполнение заняло %.5f секунд" % avg_time)
            return 1
        return wrap

    def __enter__(self): # Обязательный метод контекстного менеджера
        print("_enter_")
        return self

    def __exit__(self, type, value, traceback): # Обязательный метод контекстного менеджера
        print("_exit_")
   

   
@time_this2(num_runs=NUM_RUNS) # Объект-обёртка - Декоратор
def f2(cnt=NUM_CNT): # Декорируемая функция
    for j in range(cnt):
        pass


def f3(cnt=NUM_CNT): # Для демонстрации работы контекстного менеджера (см. main)
    for j in range(cnt):
        pass
#-------------------------------------------------------------------

def main(): # Вывод результатов на экран

    print("\nДекоратор-функция:")
    f1()
    
    print("\nДекоратор - объект:")
    f2()
    
    print("\nДекоратор - объект + контекстный менеджер:")
    with time_this2(num_runs=NUM_RUNS) as tm:
        tm(f3)(NUM_CNT)
       


    
if __name__ == "__main__":
    main()   
