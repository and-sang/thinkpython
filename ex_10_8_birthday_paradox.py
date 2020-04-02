import random
from ex_10_7_has_duplicates import has_duplicates

def birthdays(n):
    '''generates n random birthdays over 366 days
    '''
    li = []
    for i in range(n):
        li.append(random.randint(1, 365))
    return li

if __name__ == "__main__":
    classroom = 23
    samples = [10, 100, 1000, 10000, 100000]
    
    for sample in samples:
        print(f'sample: {sample}')
        counter = 0
        for i in range(sample):
            li = birthdays(classroom)
            if has_duplicates(li):
                counter += 1
        print(f'{(counter/sample)*100}%  --  {counter} out of {sample} classrooms have duplicate birthdays')
