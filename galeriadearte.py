#"La primer obra de arte es 'Number 17A', de Jackson Pollock, año 1948."
#"La segunda obra de arte es 'Les femmes d`Alger', de Pablo Picasso, año 1955."
#"La tercer obra de arte es 'Tres estudios de Lucien Freud', de Francis Bacon, año 1969."

ent1 = int(input("La primer obra de arte es 'Number 17A', de Jackson Pollock. En que año fue creada?: "))
if ent1 == 1948:
    print("Correcto! Fue en 1948 Jackson Pollock pintó esa obra de arte.")
else:
    print("Incorrecto. Continue con la siguiente pregunta.")
ent2 = int(input("La segunda obra de arte es 'Les femmes d`Alger', de Pablo Picasso. En que año fue creada?: "))
if ent2 == 1955:
    print("Correcto! Fue en 1955 que Picasso pintó esa obra de arte.")
else:
    print("Incorrecto. Continue con la siguiente pregunta.")
ent3 = int(input("La tercer obra de arte es 'Tres estudios de Lucien Freud'. En que año fue creada?: "))
if ent3 == 1969:
    print("Correcto! Fue en 1969 que Bacon pintó esa obra de arte.")
else:
    print("Incorrecto.")
print()

if ent1 and ent2 and ent3 >=1901 <= 2000:
    print("Los cuadros corresponden al siglo XX.")
else:
    print("Los cuadros NO corresponden todos al siglo XX.")

difer = ent3 - ent1
print("La diferencia de años entre el más reciente y el más antiguo es de: ", difer, "años.")