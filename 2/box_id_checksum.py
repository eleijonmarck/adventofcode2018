import sys

def read_input():
    with open('input.txt') as fh:
        data = fh.readlines()
    return data

def walkthrough_letter_box_id(box_id):

    letter_count = {}
    for letter in box_id:

        if letter in letter_count:
            letter_count[letter] = letter_count[letter] + 1
        else:
            letter_count[letter] = 1
        
    
    two_count = False
    three_count = False
    for _, count in letter_count.items():
        if count == 2:
            two_count = True
        
        if count == 3:
            three_count = True
    
    return two_count, three_count

def go_through_all_box_ids_for_common_boxes(data):

    for box_number, first_box in enumerate(data):
        first_box = first_box.strip()

        for second_box_number, second_box in enumerate(data):
            if box_number == second_box_number:
                continue

            common_letters = []
            for letter_index, first_letter in enumerate(first_box):

                if first_letter == second_box[letter_index]:
                    common_letters.append(first_letter)
                else:
                    continue
                
            if not common_letters:
                continue
            letters_that_differ = len(first_box) - len(common_letters)
            if letters_that_differ > 1:
                continue
            
            return ''.join(common_letters)
            

def main(part):


    data = read_input()

    # part 1
    if part == 1:
        number_of_two_unique, number_of_three_unique, checksum = part_one(data)
        return print('box_id: two {} * three {} = checksum {}'.format(
            number_of_two_unique, 
            number_of_three_unique, 
            checksum,
        ))

    # part 2
    common_letters = go_through_all_box_ids_for_common_boxes(data)
    return(print('common letters {}'.format(common_letters)))


def part_one(data):
    number_of_two_unique = 0
    number_of_three_unique = 0

    for box_id in data:
        two_count, three_count = walkthrough_letter_box_id(box_id)

        if two_count:
            number_of_two_unique = number_of_two_unique + 1
        
        if three_count:
            number_of_three_unique = number_of_three_unique + 1

    checksum = number_of_two_unique * number_of_three_unique

    return number_of_two_unique, number_of_three_unique, checksum

if __name__ == '__main__':
    if len(sys.argv) == 2:
        PART = sys.argv[1]
    else:
        PART = 1
    
    main(PART)