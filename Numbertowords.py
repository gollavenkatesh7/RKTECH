#  Task -2
#  Number to Words


def spell_out_number(number):
    words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
        80: 'eighty', 90: 'ninety'
    }

    if number < 0 or isinstance(number, float):
        return "Please enter a non-negative integer"

    if number == 0:
        return 'zero'

    def spell_out_helper(num):
        if num in words:
            return words[num]

        if num < 100:
            return words[num // 10 * 10] + '-' + words[num % 10]
        else:
            return words[num // 100] + ' hundred ' + spell_out_helper(num % 100)

    if number <= 999:
        return spell_out_helper(number)
    elif number <= 999999:
        return spell_out_helper(number // 1000) + ' thousand ' + spell_out_helper(number % 1000)
    else:
        return "Please enter a number less than or equal to 999999"


# Example usage:
number_to_spell = int(input("Enter the Number: "))
result = spell_out_number(number_to_spell)
print(f"{number_to_spell} spelled out is: {result}")
