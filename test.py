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
# Uncomment unit testt and just run the file to execute the script
# The Question:
# נתונות הגדרות הבאות:
# • מספר שלם חיובי נקרא "חמוד" אם הספרה הימנית שלו היא כפולה של הספרה השמאלית שלו
# לדוגמה:
# המספרים 2378 ,737 ,16, 48 הם מספרים "חמודים" כי בכל אחד מהמספרים האלה הספרה הימנית ביותר מתחלקת בספרה השמאלית ביותר ללא שארית.
# • עמודה במערך דו -ממדי נקראת "נחמדה" אם כל הערכים הנמצאים בעמודה זו הם "חמודים".
# • מערך דו-ממדי נקרא "מותק" אם יש בו לפחות עמודה אחת שהיא "נחמדה".
# א. כתוב פעולה אשר מקבלת מערך דו-ממדי ומחזירה "אמת" אם הוא "מותק" או "שקר " אם הוא אחר.
# ------------------------------------------------------------------------------------------------


"""Function to check if the given number is "cute\""""
arr = [12, 24, 26]
wrong_arr = [23, 27, 35]
doubled_arr = [
    [36, 24, 26],
    [48, 28, 39]
]
wrong_doubled_arr = [
    [37, 25, 27],
    [45, 23, 29]
]


def CuteNumber(number):
    # Type cast the given number to a string
    number_to_string = str(number)
    # print(len(number_to_string))
    # print(int(number_to_string[-1]) % int(number_to_string[0]))
    return "The num is cute" if len(number_to_string) > 1 and int(number_to_string[-1]) % int(
        number_to_string[0]) == 0 else False


# Unit tests
# print(CuteNumber(24))
# print(CuteNumber(27))
# print(CuteNumber(2))

"""Function to check the given array if it is cute"""


def CuteArray(regular_array):
    for i in regular_array:
        if CuteNumber(i):
            continue
        else:
            print(i)


# Unit tests
# CuteArray(arr)
# CuteArray(wrong_arr)


"""Function to check the given doubled_array if it is cute"""


def CuteDoubledArray(dub_array):
    for i in dub_array:
        for j in i:
            if CuteNumber(j):
                continue
            else:
                print(j)


# Unit tests
# CuteDoubledArray(doubled_arr)
# CuteDoubledArray(wrong_doubled_arr)

"""Function to check the column in the given doubled_array if it is cute"""


# FIXME: Implement this function to check columns and then to use in CheckSweetArray
def CheckColumn(dub_array):
    for i in range(len(dub_array[0])):
        if CuteNumber(dub_array[0][i]) and CuteNumber(dub_array[1][i]):
            # print("Column is 'fine'")
            continue
        else:
            return False
            # print("Column is not 'fine'")


# Unit tests
CheckColumn(dub_array=doubled_arr)
CheckColumn(dub_array=wrong_doubled_arr)

"""Function to check the column in the given doubled_array if it is cute"""


# TODO: Implement this function
def CheckSweetArray(dub_array):
    sweet = 0
    pass
