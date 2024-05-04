import random


# алгоритм Евклида нахождения обратного числа a по модулю m
def mod_inverse(a, m):
    """
    :param a - это число, для которого мы хотим найти обратное по модулю:
    :param m - модуль, по которому мы хотим найти обратное значение числа:
    :return число обратное a по модулю m:
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Функция предназначена для проверки, является ли заданное число 'n' простым числом.
def is_prime(n, k=5):
    """
    :param n - Целое число, для которого проверяется простота:
    :param k - Количество итераций, используемых в тесте простоты. Данным параметром мф контролируем насколько точной будет проверка на простоту
    :return True - число простое
    :return False - число не простое:
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


#Функция для генерации простого числа
def generate_prime_number(bits):
    """
    :param bits: Количество битов, которое должно содержать сгенерированное простое число
    :return num: сгенерированное простое число
    """
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num




# Функция для генерации пары ключей
def generate_keypair(bitlength):
    """
    :param bitlength: Длина ключа в битах
    :return (e, n), (d, n):
        e: открытая экспонента.
        n: произведение двух простых чисел, которое становится модулем для обоих ключей.
        d: закрытый ключ. Число обратное 'e' по модулю phi.

    """
    half_bitlength = bitlength // 2
    p = generate_prime_number(half_bitlength)
    q = generate_prime_number(half_bitlength)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Обычно в качестве открытого экспонента выбирают число 65537
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))



# Функция для шифрования сообщения
def encrypt(public_key, plaintext):
    """
    :param public_key:  Открытый ключ RSA, представленный в виде кортежа (e, n), где e - открытая экспонента, а n - модуль
    :param plaintext: Сообщение
    :return cipher: список зашифрованных символов
    """

    """
    pow(x, y, z) - функция возводит число 'x' в степень 'y' и берет модуль 'z' 
    ord(c) - представляет символ в числовом формате
    """
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


# функция для расшифровки зашифрованного сообщения
def decrypt(private_key, cipher):
    """

    :param private_key: Закрытый ключ RSA, представленный в виде кортежа (d, n), где d - закрытая экспонента, а n - модуль.
    :param cipher: Зашифрованное сообщение, представленное в виде списка чисел
    :return: Расшифрованное сообщение
    """
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(plain)

# Пример использования:
if __name__ == '__main__':

    # Генерация ключей
    public_key, private_key = generate_keypair(128)

    # Вывод ключей
    print("public key:", public_key)
    print("private key:", private_key)

    # Шифрование
    plaintext = "Hello, World!"
    cipher = encrypt(public_key, plaintext)
    print("Encrypted:", cipher)

    # Расшифрование
    decrypted = decrypt(private_key, cipher)
    print("Decrypted:", decrypted)



