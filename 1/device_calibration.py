import ast
import sys

def read_input():
    with open('input.txt') as fh:
        data = fh.readlines()

    return data


def main(part):

    data = read_input()

    results = set()
    resulting_frequency = 0
    results.add(resulting_frequency)
    reached_duplicate = False

    while not reached_duplicate:
        resulting_frequency, reached_duplicate = go_through_frequency(
            data, 
            resulting_frequency, 
            results,
            )
        if part == 1:
            return resulting_frequency


    return resulting_frequency

def go_through_frequency(data, resulting_frequency, results):

    for frequency in data:
        resulting_frequency = resulting_frequency + eval(frequency)

        if not resulting_frequency in results:
            results.add(resulting_frequency)
        else:
            reached_duplicate = True
            return resulting_frequency, reached_duplicate

    return resulting_frequency, False


if __name__ == '__main__':
    if len(sys.argv) == 2:
        part = sys.argv[1]
    else:
        part = 1
    print('output {}'.format(main(part)))