"""
Haolin Y
Xiaoming Zhang
Tuesday , May 4th
R. Vincent , instructor
Final Project
"""

print('Hello and welcome to "Search For String"!\nEntering two empty strings is to quit the program.' ) #\nThis program can take 2 strings and return \nthe number of distinct permutations of the short\nstring that appears as sub strings in the long string.\nEntering nothing for both strings means to quit the prorgam')
while True:
    short_s = input("Please tell me what is the short string?")
    long_s = input("The long string is ... ...?")
    if not (short_s or long_s):
        print("Have a nice day! Bye Bye;)")
        break
    S_length = len(short_s)
    L_length = len(long_s)

    lis = [0]*26     # histogram for the short_s
    histogram = [0]*26
    answer_set = set()

    import string
    x = string.ascii_lowercase

    x = dict(zip(x,range(26))) #create a letter-to-number dictionary

    P = 29
    MASK = 2**128 - 1
    h_tab = [0] * (L_length + 1)

    power = (P ** (S_length)) & MASK

    for l in short_s:
        lis[x.get(l)] += 1  # histogram for the short_s

    for i, l in enumerate(long_s):
        test = True
        h_tab[i + 1] = ((h_tab[i] * P) + x.get(l)) & MASK
        histogram[x.get(l)] += 1   # the times that the new letter appears in the sub_str += 1
        if i - S_length >= 0:   # when the sub_str has the same len as the short_s
            histogram[x.get(long_s[i - S_length])] -= 1
        if histogram == lis:
            hash_value = h_tab[i+1] - (h_tab[i + 1 - S_length] * power) & MASK # compute the hash value of the sub_str
            answer_set.add(hash_value)

    f0 = "The distinct permutations of the short string appears in the long string {} times."
    print(f0.format(len(answer_set)))
