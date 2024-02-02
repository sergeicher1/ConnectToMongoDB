# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | https://www.zero-to-hero.dev/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                                   maintaining your code will be a violent
#                                                       psychopath who knows where you live”
# -- Language                                 | Python
# -- Version                                  | 3.12
# -- Description                              | Exercise "cute_numbers"
# Usage Example
# Just run the file to execute the script
# ------------------------------------------------------------------------------------------------


"""Function to check if the given number is "cute\""""
arr = [
    [12, 24, 26],
    [39, 48, 36]
]


def CuteNumber(number):
    # Type cast the given number to a string
    number_to_string = str(number)
    return int(number[-1]) % int(number[0]) == 0


def CheckArray(doubled_list):
    # number_of_items = len(doubled_list)
    doubled_list = arr
    number_of_items = 2
    if CuteNumber(doubled_list[0][0]):
        if CuteNumber(doubled_list[1][0]):
            if CuteNumber(doubled_list[0][1]):
                if CuteNumber(doubled_list[1][1]):
                    return "ok"
    return doubled_list

# def cute_arr(arr, column):
#     for i in arr:
#         if cute_num(i[column]) == False:
#             return False
#     return True
#
#
# def honey_arr(arr):
#     for i in range(len(arr[0])):
#         if cute_arr(arr, i) == True:
#             return True
#     return False


# arr1 = [[12, 24, 26], [23, 23, 23], [23, 23, 23]]
# arr2 = [[23, 24, 23], [23, 48, 23], [23, 17, 23]]
# arr3 = [[1, 3, 5], [6, 7, 8], [9, 3, 2]]

# print(f"{honey_arr(arr)} need to be => True.")
# print(f"{honey_arr(arr1)} need to be => False.")
# print(f"{honey_arr(arr2)} need to be => True.")
# print(f"{honey_arr(arr3)} need to be => True.")
