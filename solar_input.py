# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject
import json


def read_info(obj):
    type = obj['type']
    radius = obj['radius']
    color = obj['color']
    mass = obj['mass']
    X_c = obj['X_c']
    Y_c = obj['Y_c']
    X_v = obj['X_v']
    Y_v = obj['Y_v']
    return type, radius, color, mass, X_c, Y_c, X_v, Y_v


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    with open(input_filename, 'r') as f:
        loaded = json.load(f)  # загружает файл в loaded

    objects = loaded["obj"]  # загружает из loaded список объектов
    inf = []  # массив информации по объектам
    for obj in objects:  # перебегает по каждому космическому объекту
        if obj["type"] != "Star" and obj["type"] != "Planet":
            print(obj["type"] + ' - Unknown space object')
        inf.append(read_info(obj))  # передает в inf информацию по объекту

    return inf


'''
def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            # FIXME!
'''


if __name__ == "__main__":
    print("This module is not for direct call!")
