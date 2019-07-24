morse_dictionary = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                   '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                   '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                   '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                   '-.--': 'Y', '--..': 'Z', '': ' '}

morse_signal = input("모스부호를 올바르게 입력하세요: ").split(" ")
print("".join(list(map(lambda x: morse_dictionary[x], morse_signal))))

# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.-- (HE SLEEPS EARLY)