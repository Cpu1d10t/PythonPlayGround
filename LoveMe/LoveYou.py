import random
import time 
while True:
    ImSoKind=open('NiceWordsToSay.txt').read().splitlines()
    NiceWords=random.choice(ImSoKind)
    print(NiceWords)
    time.sleep(3)
