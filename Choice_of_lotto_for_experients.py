import numpy as np
import random
set_part_int = []
h = set()
arr = []
arr_lotto = {'loto':{'Etoiles': [10, 1], 'Grille': [49, 5]}, 'euromillion':{'Etoiles':[12,2], 'Grille':[50, 5]}}

while True:
        typelot = input('What lotto you prefer? currently available -'+ ','.join(arr_lotto) + ' : ')
        typelot = typelot.strip().lower()
        
        if typelot in arr_lotto:
            for k, v in arr_lotto[typelot].items():
                while len(arr) < 5:
                        while len(h) < min(v):
                            h.add(int(np.random.randint(1, max(v) + 1, 1)))
                        arr.append(h)
                        h = set()
                np.random.shuffle(arr)
                lotto = list(np.random.choice(arr))
                print("Here is your set of lucky " + k + " numbers " + ','.join(str(x) for x in lotto))
                arr = []
            break
        else:
                print("This type of lottery is not yet available, try one more time")
