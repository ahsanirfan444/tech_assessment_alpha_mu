

def words_to_number(word_string):
    
    words_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
        'thousand': 1000, 'million': 1000000, 'and': 0, 'a': 0,
        'half': 0.5, 'quarter': 0.25
    }

    words = word_string.lower().split()
    total = 0
    current_number = 0

    for word in words:
        if word in words_dict:
            if words_dict[word] == 0:
                continue
            elif words_dict[word] == 100:
                current_number *= 100
            elif words_dict[word] == 1000 or words_dict[word] == 1000000:
                total += current_number * words_dict[word]
                current_number = 0
            else:
                current_number += words_dict[word]

    total += current_number
    return total


def number_to_words(num):
    if num == 0:
        return "Zero"

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million"]

    def convert_less_than_hundred(num):
        if num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + ("-" + units[num % 10] if num % 10 != 0 else "")

    def convert_less_than_thousand(num):
        if num < 100:
            return convert_less_than_hundred(num)
        else:
            return units[num // 100] + " Hundred" + (" and " + convert_less_than_hundred(num % 100) if num % 100 != 0 else "")

    result = ""
    digit_counter = 0
    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            chunk_words = convert_less_than_thousand(chunk)
            result = chunk_words + (" " + thousands[digit_counter] if digit_counter > 0 else "") + " " + result
        num //= 1000
        digit_counter += 1

    return result.strip()
