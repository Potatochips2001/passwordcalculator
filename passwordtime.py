import random
import datetime
import sys


print("\n")

try:
    if len(sys.argv) > 1:
        passw = sys.argv[1]
        comb = len(set(passw))**len(passw)
        crackTime = comb / 2000
    else:
        passw = input("Password: ")
        comb = len(set(passw)) ** len(passw)
        crackTime = comb/2000
except OverflowError:
    print("\nNever\n")
except:
    pass

try:
    print(f"\nTime to crack password : {str(datetime.timedelta(seconds=crackTime))}\n")
except OverflowError:
    try:
        print(f'\nTime to crack password : {str(crackTime/86400/365)} years')
    except:
        print('\nNever')
except:
    pass
