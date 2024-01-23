legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
legendary_item_found = False
while True:
    element = input().split()
    for i in range(0, len(element), 2):
        key = element[i + 1].lower()
        value = int(element[i])

        if key in key_materials:
            key_materials[key] += value
            if key_materials[key] >= 250:
                print(f"{legendary_items[key]} obtained!")
                key_materials[key] -= 250
                legendary_item_found = True
                break
        else:
            if key not in junk:
                junk[key] = 0
            junk[key] += value

    if legendary_item_found:
        break

print('shards:', key_materials['shards'])
print('fragments:', key_materials['fragments'])
print('motes:', key_materials['motes'])
[print(f'{key}: {junk[key]}') for key in junk]