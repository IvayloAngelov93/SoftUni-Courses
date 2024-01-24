force_book = {}
while True:
    name_in = False
    text = input()
    if text == 'Lumpawaroo':
        break

    if '|' in text:
        elements = text.split(' | ')
        key = elements[0]
        value = elements[1]
        if key not in force_book:
            force_book[key] = []
        for name in force_book.values():
            if value in name:
                name_in = True
        if not name_in:
            force_book[key].extend([value])

    elif '->' in text:
        elements = text.split(' -> ')
        key = elements[1]
        value = elements[0]
        if key not in force_book:
            force_book[key] = []

        for name in force_book.values():
            if value in name:
                name.remove(value)

        force_book[key].extend([value])
        print(f"{value} joins the {key} side!")

for key, value in force_book.items():
    if value:
        print(f"Side: {key}, Members: {len(value)}")
        for name in value:
            print(f'! {name}')