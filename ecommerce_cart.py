def ecart(i):
    if not i:
        return "Cart is empty."
    total = sum(i.values())
    if len(i) > 5:
        total *= 0.9
    return f"Total Price: {total}"

i = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(ecart(i))
