year=int(input())
if year<1918:
    if year%4==0:
        print(f"12.09.{year}")
    else:
        print(f"13.09.{year}")
else:
    if year%100==0 and year%400==0:
        print(f"12.09.{year}")
    elif year%100!=0 and year%4==0:
        print(f"12.09.{year}")        
    else:
        print(f"13.09.{year}")

        