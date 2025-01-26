def fibonacci(n):
    if n <= 0:
        raise ValueError("n должно быть положительным числом")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    while True:  # Бесконечный цикл, который будет запрашивать ввод до получения корректного числа
        try:
            n = int(input("Введите индекс числа Фибоначчи: "))
            print(f"Число Фибоначчи для {n}-го индекса: {fibonacci(n)}")
            break  # Если ввод корректен, выходим из цикла
        except ValueError:
            print("Пожалуйста, введите корректное число.")
        except Exception as ex:
            print(f"Произошла ошибка: {ex}. Попробуйте снова.")
