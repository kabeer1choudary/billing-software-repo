prod = {'50g':16, '100g':32, '150g':48,'200g':64, '250g':80 }
ls = []

while True:
    val = input('enter your value:')
    res = prod.get(val)
    try:
        if res in prod.values():
            ls.append(res)
        else:
            print('total = ', sum(ls))
            break
    except (TypeError):
        print('0')
