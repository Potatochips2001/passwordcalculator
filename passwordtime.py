import random
import datetime


print("\n")
passw = input("Password: ")
comb = len(set(passw)) ** len(passw)
crackTime = comb/2000

try:
    print(f"\nTime to crack password : {str(datetime.timedelta(seconds=crackTime))}\n")
except OverflowError:
    print("\n>68 years")
except:
    pass