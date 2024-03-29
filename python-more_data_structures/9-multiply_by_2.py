#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}


if __name__ == "__main__":
    def print_sorted_dictionary(a_dictionary):
        for key in sorted(a_dictionary.keys()):
            print(f"{key}: {a_dictionary[key]}")

    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
