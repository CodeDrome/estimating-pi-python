import math

PI_STRING = "3.141592653589793238"
RED = "\x1B[31m"
GREEN = "\x1B[32m"
RESET = "\x1B[0m"


def main():

    """
    Here we simply call the functions which estimate pi using various methods
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Estimating Pi |")
    print("-----------------\n")

    fractions()

    francois_viete()

    john_wallis()

    john_machin()

    gregory_leibniz()

    nilakantha()


def print_as_text(pi):

    """
    Takes a value for pi and prints it below a definitive value,
    with matching digits in green and non-matching digits in red
    """

    pi_string = str("%1.18f" % pi)

    print("Definitive: " + PI_STRING)

    print("Estimated:  ", end="")

    for i in range(0, len(pi_string)):

        if pi_string[i] == PI_STRING[i]:

            print(GREEN +  pi_string[i] + RESET, end="")

        else:

            print(RED +  pi_string[i] + RESET, end="")

    print("\n")


def fractions():

    """
    Estimates pi using a selection of increasingly accurate fractions
    """

    pi = 22 / 7
    print("22/7\n====")
    print_as_text(pi)

    pi = 333 / 106
    print("333/106\n=======")
    print_as_text(pi)

    pi = 355 / 113
    print("355/113\n=======")
    print_as_text(pi)

    pi = 52163 / 16604
    print("52163/16604\n===========")
    print_as_text(pi)

    pi = 103993 / 33102
    print("103993/33102\n============")
    print_as_text(pi)

    pi = 245850922 / 78256779
    print("245850922/78256779\n==================")
    print_as_text(pi)


def francois_viete():

    """
    Infinite series discovered by French mathematician Francois Viete in 1593
    """

    print("Francois Viete\n==============")

    iterations = 28
    numerator = 0.0
    pi = 1.0

    for i in range(1, iterations + 1):
        numerator = math.sqrt(2.0 + numerator)
        pi*= (numerator / 2.0)

    pi = (1.0 / pi) * 2.0

    print_as_text(pi)


def john_wallis():

    """
    Infinite product created by English mathematician John Wallis in 1655
    """

    print("John Wallis\n===========")

    iterations = 1000000
    numerator = 2.0
    denominator = 1.0
    pi = 1.0

    for i in range(1, iterations + 1):
        pi*= (numerator / denominator)
        if (i%2) == 1:
            denominator+= 2.0
        else:
            numerator+= 2.0

    pi*= 2.0

    print_as_text(pi)


def john_machin():

    """
    Formula discovered by English astronomer John Machin in 1706
    """

    print("John Machin\n===========")

    pi = (4.0 * math.atan(1.0 / 5.0) - math.atan(1.0 / 239.0)) * 4.0

    print_as_text(pi)


def gregory_leibniz():

    """
    Co-discovered by James Gregory and Gottfried Wilhelm Leibniz
    """

    print("Gregory-Leibniz\n===============")

    iterations = 400000
    denominator = 1.0
    multiplier = 1.0
    pi = (4.0 / denominator)

    for i in range(2, iterations + 1):
        denominator += 2.0
        multiplier *= -1.0
        pi += ( (4.0 / denominator) * multiplier )

    print_as_text(pi)


def nilakantha():

    """
    Named after the 15th century Indian mathematician Nilakantha Somayaji
    """

    print("Nilakantha\n=========")

    iterations = 1000000
    multiplier = 1.0
    start_denominator = 2.0
    pi = 3.0

    for i in range(1, iterations + 1):
        pi += ( (4.0 / (start_denominator * (start_denominator + 1.0) * (start_denominator + 2.0)) ) * multiplier)
        start_denominator += 2.0
        multiplier *= -1.0

    print_as_text(pi)


main()
