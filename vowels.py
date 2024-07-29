
alp=input("enter a alphabet")
alp=alp.lower()
def switch_demo(value):
    match value:
        case 'a':
            print("vowel")
        case 'e':
            print("vowel")
        case 'i':
            print("vowel")
        case 'o':
            print("vowel")
        case 'u':
            print("vowel")
        case _:
            print("not a vowel")
print(switch_demo(alp))
