
user_message = input("Write a message to be translate to Morse Code: ").lower()
print(user_message)

morse_code = []
separate = " "

for char in range(0, len(user_message)):
    # print(user_message[char])
    if user_message[char] == 'a':
        letter_a = user_message[char].replace('a', '. _')
        morse_code.append(letter_a)

    if user_message[char] == 'b':
        letter_b = user_message[char].replace('a', '_ . . .')
        morse_code.append(letter_b)

    if user_message[char] == 'c':
        letter_c = user_message[char].replace('c', '_ . _ .')
        morse_code.append(letter_c)

    if user_message[char] == 'd':
        letter_d = user_message[char].replace('d', '_ . .')
        morse_code.append(letter_d)

    if user_message[char] == 'e':
        letter_e = user_message[char].replace('e', '.')
        morse_code.append(letter_e)

    if user_message[char] == 'f':
        letter_f = user_message[char].replace('f', '. . _ .')
        morse_code.append(letter_f)

    if user_message[char] == 'g':
        letter_g = user_message[char].replace('g', '_ _ .')
        morse_code.append(letter_g)

    if user_message[char] == 'h':
        letter_h = user_message[char].replace('h', '. . . .')
        morse_code.append(letter_h)

    if user_message[char] == 'i':
        letter_i = user_message[char].replace('i', '. .')
        morse_code.append(letter_i)

    if user_message[char] == 'j':
        letter_j = user_message[char].replace('j', '. _ _ _')
        morse_code.append(letter_j)

    if user_message[char] == 'k':
        letter_k = user_message[char].replace('k', '_ . _')
        morse_code.append(letter_k)

    if user_message[char] == 'l':
        letter_l = user_message[char].replace('l', '. _ . .')
        morse_code.append(letter_l)

    if user_message[char] == 'm':
        letter_m = user_message[char].replace('m', '_ _')
        morse_code.append(letter_m)

    if user_message[char] == 'n':
        letter_n = user_message[char].replace('n', '_ .')
        morse_code.append(letter_n)

    if user_message[char] == 'o':
        letter_o = user_message[char].replace('o', '_ _ _')
        morse_code.append(letter_o)

    if user_message[char] == 'p':
        letter_p = user_message[char].replace('p', '. _ _ .')
        morse_code.append(letter_p)

    if user_message[char] == 'q':
        letter_q = user_message[char].replace('q', '_ _ . _')
        morse_code.append(letter_q)

    if user_message[char] == 'r':
        letter_r = user_message[char].replace('r', '. _ .')
        morse_code.append(letter_r)

    if user_message[char] == 's':
        letter_s = user_message[char].replace('s', '. . .')
        morse_code.append(letter_s)

    if user_message[char] == 't':
        letter_t = user_message[char].replace('t', '_')
        morse_code.append(letter_t)

    if user_message[char] == 'u':
        letter_u = user_message[char].replace('u', '. . _')
        morse_code.append(letter_u)

    if user_message[char] == 'v':
        letter_v = user_message[char].replace('v', '. . . _')
        morse_code.append(letter_v)

    if user_message[char] == 'w':
        letter_w = user_message[char].replace('w', '. _ _')
        morse_code.append(letter_w)

    if user_message[char] == 'x':
        letter_x = user_message[char].replace('x', '_ . . _')
        morse_code.append(letter_x)

    if user_message[char] == 'y':
        letter_y = user_message[char].replace('y', '_ . _ _')
        morse_code.append(letter_y)

    if user_message[char] == 'z':
        letter_z = user_message[char].replace('z', '_ _ . .')
        morse_code.append(letter_z)

# print(morse_code)
print(separate.join(morse_code))
