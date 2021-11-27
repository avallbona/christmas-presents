import random

family = ['Thérèse', 'Anne', 'Andreu', 'Pauline', 'Michel', 'Geneviève', 'Marie-Agnès',
          'Charles', 'Benoît', 'François', 'Jean-Louis', 'Laura', 'Louis-Marie',
          'Christine', 'David', 'Caroline']


def random_presents():

    result = []
    for it in sorted(family):
        target = random.choice(family)
        while target == it:
            target = random.choice(family)
        result.append((it, target))

    print(f'Total combinations: {len(result)}')
    print("=" * 30)
    for idx, it in enumerate(result, start=1):
        print(f'0{idx}'[-2:], it[0], ' -> ', it[1])
    print("=" * 30)


if __name__ == '__main__':
    random_presents()
