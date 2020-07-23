def swap_case(s):
    temp=''
    for i in range(len(s)):
        if s[i]!=s[i].upper():
            temp+=s[i].upper()
        else:
            temp+=s[i].lower()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)