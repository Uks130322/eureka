def eureka(number: int) -> bool:
    lst = list(str(number))
    summa = sum([int(item) ** (index + 1) for index, item in enumerate(lst)])
    return summa == number


def sum_dig_pow(a, b):
    return [number for number in range(a, b + 1) if eureka(number)]


class Color:
    def __init__(self):
        self.done = False


triplets = [
  ['t', 'u', 'p'],
  ['w', 'h', 'i'],
  ['t', 's', 'u'],
  ['a', 't', 's'],
  ['h', 'a', 'p'],
  ['t', 'i', 's'],
  ['w', 'h', 's']
]

my_dict = dict()

for triplet in triplets:
    my_dict[triplet[0]] = my_dict.get(triplet[0], set()) | {triplet[1], triplet[2]}
    my_dict[triplet[1]] = my_dict.get(triplet[1], set()) | {triplet[2], }
    my_dict[triplet[2]] = my_dict.get(triplet[2], set())
    
print(my_dict)

phrase = []

while len(phrase) < len(my_dict):
    for key, value in my_dict.items():
        if value == set():
            phrase += [key]
            my_dict[key] = {"Done", }
            for letter in my_dict.keys():
                my_dict[letter] -= {key, }
            print(my_dict)

phrase.reverse()

print("".join(phrase))
