#create a dictionary with 5 elements

Corvette_Build = {'power adder' : 'T3 Turbo',
                 'Fuel Delivery': 'FiTech Go Street EFI',
                 'Transmission': 'Tremec TKX',
                 'block': 'Forged',
                 'Camshaft': 'Pro LS Turbo Cam'}
print(Corvette_Build)
print(len(Corvette_Build))
print(Corvette_Build['Transmission'])
print()
Corvette_Build['Clutch'] = 'McLeod Super Pro'
del Corvette_Build['block']
print(len(Corvette_Build))
print(Corvette_Build)
print()
x = Corvette_Build.keys()