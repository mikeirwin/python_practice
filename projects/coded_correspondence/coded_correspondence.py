message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. " \
          "muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "',.?! "

hidden = "can this message be deciphered?"


def cipher(type, offset):
    translated_message = ""
    for letter in type:
        if letter not in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    print(translated_message)


cipher(hidden, 3)


def decoder(type, offset):
    translated_message = ""
    for letter in type:
        if letter not in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    print(translated_message)


decoder(message, 10)


def vigen_decode(message, keyword):
    keyword_repeated = ""
    while len(keyword_repeated) < len(message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(message)]
    translated_message = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message


new_message = "dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!"
keyword = "friends"

print(vigen_decode(new_message, keyword))


def vigen_cipher(message, keyword):
    keyword_repeated = ""
    while len(keyword_repeated) < len(message):
        keyword_repeated += keyword
    keyword_final = keyword_repeated[0:len(message)]
    translated_message = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message


message_for_V = "your ciphers put me to the test. i hope you continue to challenge me!"
keyword2 = "rivals"
coded = "pwpr uzxceck xpt ev oo lym tpkk. i zfxz jgl xoylzvpe lf xhldcmigp dm!"
print(vigen_cipher(message_for_V, keyword2))
print(vigen_decode(coded, keyword2))