num2Word = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
}

def num_to_word(number):
    # print(number)
    num_list = [int(x) for x in str(number)]
    if(len(num_list) > 1):
        if(number<20):
            if(num_list[-2] == 1):
                # print(num_list[-2:])
                teen = ''.join(map(str, num_list[-2:]))
                return(num2Word[int(teen)])
        elif(number<100) :
            ty = num_list[-2] * 10
            return(num2Word[int(ty)],num2Word[num_list[-1]])
        elif(number<1000) :
            if(number%100==0):
                return(num2Word[num_list[0]],num2Word[100])
            elif(num_list[-2] == 1):
                teen = ''.join(map(str, num_list[-2:]))
                return(num2Word[num_list[0]],num2Word[100] ,"and",num2Word[int(teen)])
            else:
                ty = num_list[-2] * 10
                return(num2Word[num_list[0]],num2Word[100] ,"and", num2Word[int(ty)],num2Word[num_list[-1]])
        elif(number == 1000):
            return("one thousand")
    else:
        return(num2Word[num_list[-1]])

# print(num_to_word(911))

def word_length(word):
    word = ''.join(word).replace(" ", "")
    print(word)
    return len(word)

word_length(num_to_word(1000))

print(word_length(num_to_word(342)))


total = 0
for i in range(1001):
    total += word_length(num_to_word(i))
print(total)
