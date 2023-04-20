import re

lst = ['Toyota Corolla Altis 1.6A Elegance', 'Toyota Previa 2.4A (COE till 05/2029)',
       'Porsche Cayman R 3.4A PDK (COE till 04/2031)', 'Porsche Macan 2.0A PDK',
       'Toyota Alphard 2.4A (COE till 01/2029)', 'Toyota Vios 1.5A E (COE till 02/2024)', 'Mitsubishi Lancer EX 1.6A',
       'Mercedes-Benz A-Class Saloon A200 AMG Line', 'Audi Q2 1.4A TFSI CoD S-tronic', 'Nissan Cabstar',
       'Mitsubishi Fuso Canter FEB21', 'Kia Cerato 1.6A EX', 'Porsche Cayman 2.7A Tip (COE till 06/2028)',
       'Honda Civic Type R 2.0M (COE till 06/2027)', 'Mazda Biante 2.0A', 'Volkswagen Golf 1.4A TSI Comfortline',
       'Mercedes-Benz SLK-Class SLK200ML (COE till 04/2029)', 'Honda Odyssey 2.4A EXV-S Sunroof', 'Honda Vezel 1.5A X',
       'MINI Cooper S 1.6A Sunroof (COE till 08/2030)', 'Mercedes-Benz CLA-Class CLA200 AMG Line Premium Plus',
       'Volkswagen Scirocco GP 1.4A TSI', 'Volkswagen Golf 1.4A TSI R-Line Highline Sunroof']

brands = []
models = []
others = []

for item in lst:
    # Find the brand name
    brand = re.findall('^[A-Za-z]+', item)[0]
    brands.append(brand)

    # Remove brand name and split the string to get model and others
    item = item.replace(brand, '').strip()
    split_item = item.split(' ')

    # Find the model name
    model = ''
    for i in split_item:
        if bool(re.search('\d', i)):
            break
        else:
            model += i + ' '
    models.append(model.strip())

    # Find the other details
    other = ' '.join(split_item[len(model.split()):])
    others.append(other)

print('Brands:', brands)
print('Models:', models)
print('Others:', others)
