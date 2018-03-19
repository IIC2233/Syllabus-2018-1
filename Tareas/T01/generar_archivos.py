import random
import datetime

GALAXIAS = ['Andrómeda', 'Enana del Can Mayor']
PLANETAS = ['Tierra', 'Tarsonis', 'Aiur', 'Mar Sara', 'Korhal IV',
            'Carbonis', 'Pandora', 'Sayshell', 'Krypton', 'Tatooine']
RAZAS = {
    'Tierra': "Aprendiz",
    'Tarsonis': "Asesino",
    'Aiur': "Mago",
    'Mar Sara': "Asesino",
    'Korhal IV': "Aprendiz",
    'Carbonis': "Asesino",
    'Sayshell': "Aprendiz",
    'Pandora': "Mago",
    'Krypton': "Mago",
    'Tatooine': "Aprendiz",
}

MAXIMA_POBLACION = {
    "Mago": 100,
    "Aprendiz": 150,
    "Asesino": 400
}

CONQUISTADO = {
    'Andrómeda': False,
    'Enana del Can Mayor': False
}

random.shuffle(GALAXIAS)
random.shuffle(PLANETAS)


galaxia_csv = [['nombre: string',
                'minerales: int',
                'deuterio: int']]

for galaxia in GALAXIAS:
    galaxia_csv.append([galaxia,
                        random.randint(100, 10000),
                        random.randint(100, 10000)])

galaxia_csv = list(zip(*galaxia_csv))
random.shuffle(galaxia_csv)
galaxia_csv = list(zip(*galaxia_csv))


def generar_datos(planeta):
    galaxia = random.choice(GALAXIAS)
    raza = RAZAS[planeta]

    if not CONQUISTADO[galaxia]:
        conquistado = True
        CONQUISTADO[galaxia] = True

    elif random.random() > 0.7:
        conquistado = True
        CONQUISTADO[galaxia] = True
    else:
        conquistado = False

    if conquistado:
        proba = 0.4
    else:
        proba = 0.7

    if random.random() < proba:
        cuartel = True
    else:
        cuartel = False

    if cuartel and raza == "Mago":
        magos = random.randint(0, MAXIMA_POBLACION["Mago"])
    else:
        magos = 0

    if cuartel:
        soldados = random.randint(0, MAXIMA_POBLACION[raza] - magos)
    else:
        soldados = 0

    tasa_minerales = random.randint(1, 10)
    tasa_deuterio = random.randint(5, 15)

    segundos = datetime.timedelta(seconds=random.randint(0, 240))
    hora_actual = datetime.datetime.now() - segundos
    ultima_recoleccion = str(hora_actual).split(".")[0]
    if random.random() < proba:
        nivel_ataque = random.randint(1, 3)
    else:
        nivel_ataque = 0

    if random.random() < proba:
        nivel_economia = random.randint(1, 3)
    else:
        nivel_economia = 0

    if random.random() < proba:
        torre = True
    else:
        torre = False



    return [planeta, galaxia, raza, magos, soldados, tasa_minerales,
            tasa_deuterio, ultima_recoleccion, nivel_ataque,
            nivel_economia, conquistado, torre, cuartel]

planetas_csv = [['nombre: string', 'galaxia: string', 'raza: string',
                 'magos: int', 'soldados: int', 'tasa_minerales: int',
                 'tasa_deuterio: int', 'ultima_recoleccion: datetime',
                 'nivel_ataque: int', 'nivel_economia: int',
                 'conquistado: bool', 'torre: bool', 'cuartel: bool']]

for planeta in PLANETAS:
    planetas_csv.append(generar_datos(planeta))


planetas_csv = list(zip(*planetas_csv))
random.shuffle(planetas_csv)
planetas_csv = list(zip(*planetas_csv))


with open('galaxias.csv', 'w', encoding="UTF-8") as file:
    for elem in galaxia_csv:
        file.write(", ".join([str(x) for x in elem]) + "\n")

with open('planetas.csv', 'w', encoding="UTF-8") as file:
    for elem in planetas_csv:
        file.write(", ".join([str(x) for x in elem]) + "\n")
