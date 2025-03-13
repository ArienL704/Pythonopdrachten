import json

def get_inputs():
    name = input("Naam:")
    d =  {}
    d['jaar'] = input('jaar:')
    d['auteur'] = input("auteur:")
    return(name,d)

out = {}

while True:
    exit = input('Will je nog wat toevoegen (y/n)? ')
    if exit.lower() == 'n':
        break
    else:
        name, d = get_inputs()
        out[name] = d

with open('Muziek.json','w') as f:
    json.dump(out, f, indent=2)

