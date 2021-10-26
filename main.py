import math


def is_prime(n):
    """
Verifies if the integer is prime
    :param n: integer
    :return: returns True if number is prime and False if not
    """
    if n < 2:
        return False
    for i in range (2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    """
Looks for largest prime below
    :param n: integer
    :return: largest prime below
    """
    n = n - 1
    while is_prime(n) == False:
        n = n - 1
    return n


def test_get_largest_prime_below():
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(27) == 23
    assert get_largest_prime_below(55) == 53
    assert get_largest_prime_below(4) == 3


def get_perfect_squares(start, end):
    """
Returns all perfect squares in an interval
    :param start: integer
    :param end: integer
    :return: list
    """
    if start < 0 and end < 0:
        return []
    if start > end:
        return []
    lst = []
    for i in range(start, end+1):
        if i >= 0:
            if int(math.sqrt(i))*int(math.sqrt(i)) == i:
                lst.append(i)
    return lst


def test_get_perfect_squares():
    assert get_perfect_squares(3, 11) == [4, 9]
    assert get_perfect_squares(5, 35) == [9, 16, 25]
    assert get_perfect_squares(-1, 5) == [0, 1, 4]
    
def is_antipalindrome(n):

    clone_n = n
    inverse_n = 0
    number_of_digits = 0

    while clone_n:
        inverse_n = inverse_n * 10 + clone_n % 10
        clone_n //= 10
        number_of_digits += 1

    if number_of_digits % 2 == 1:
        ok = 0
    else:
        ok = 1

    while inverse_n:
        if inverse_n % 10 == n % 10:
            ok = ok + 1
        if ok == 2:
            return False
        inverse_n //= 10
        n //= 10
    return True


def test_is_antipalindrome():

    assert is_antipalindrome(112316) == False
    assert is_antipalindrome(123) == True
    assert is_antipalindrome(562889) == True


def main():
    finish = False
    while not finish:
        print("Exercitiul 1. Găsește ultimul număr prim mai mic decât un număr dat")
        print("Exercitiul 12. Afișează toate pătratele perfecte dintr-un interval închis dat")
        print("Exercitiul 7. Determina daca un numar este anti-palindrom")
        print("x. Iesiti din program")
        option = input("Dati optiunea: ")
        if option == '1':
            n = int(input("Introduceti un numar: "))
            print("Ultimul numar prim mai mic decat numarul dat este: ")
            print(get_largest_prime_below(n))
            test_get_largest_prime_below()
        elif option == '12':
            print("Introduceti primul numar al unui interval: ")
            start = int(input())
            print("Ultimul numar al intervalului ales: ")
            end = int(input())
            print("Patratele perfecte din interval sunt: ")
            print(get_perfect_squares(start, end))
            test_get_perfect_squares()
        elif option == '7':
            n = int(input("Introduceti un numar: "))
            print(is_antipalindrome(n))
            test_is_antipalindrome()
        elif option == 'x':
            finish = True
        else:
            print("Optiunea nu este valida")


if __name__ == "__main__":

    main()
