import json


def load_data(filepath):
    with open(filepath) as file:
        data = json.loads(file.read())
    return data


def get_biggest_bar(bar_data):
    biggest_bar = {"Cells": {"SeatsCount": float("-inf")}}
    for bar in bar_data:
        if biggest_bar["Cells"]["SeatsCount"] < bar["Cells"]["SeatsCount"]:
            biggest_bar = bar
    return biggest_bar


def get_smallest_bar(bar_data):
    smallest_bar = {"Cells": {"SeatsCount": float("inf")}}
    for bar in bar_data:
        if smallest_bar["Cells"]["SeatsCount"] > bar["Cells"]["SeatsCount"]:
            smallest_bar = bar
    return smallest_bar


def get_closest_bar(bar_data, longitude, latitude):
    _distance = float("inf")
    longitude = float(longitude)
    latitude = float(latitude)
    closest_bar = {}
    for bar in bar_data:
        bar_geo = bar["Cells"]["geoData"]["coordinates"]
        bar_distance = distance([longitude, latitude], bar_geo)
        if _distance > bar_distance:
            _distance = bar_distance
            closest_bar = bar
    closest_bar["Cells"]["Distance"] = _distance
    return closest_bar


def distance(point_1, point_2):
    return ((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2)**0.5


if __name__ == '__main__':
    bar_data = load_data(input("Введите путь к JSON файлу: "))
    print()
    biggest_bar = get_biggest_bar(bar_data)
    print("Самый большой бар: {0}\n"
          "Количество мест: {1}\n"
          "Адрес: {2}\n".format(
                            biggest_bar["Cells"]["Name"],
                            biggest_bar["Cells"]["SeatsCount"],
                            biggest_bar["Cells"]["Address"]))
    smallest_bar = get_smallest_bar(bar_data)
    print("Самый маленький бар: {0}\n"
          "Количество мест: {1}\n"
          "Адрес: {2}\n".format(
                            smallest_bar["Cells"]["Name"],
                            smallest_bar["Cells"]["SeatsCount"],
                            smallest_bar["Cells"]["Address"]))
    lon, lat = input("Введите долготу и широту через пробел: ").split()[:2]
    closest_bar = get_closest_bar(bar_data, lon, lat)
    print("Самый близкий бар: {0}\n"
          "Количество мест: {1}\n"
          "Адрес: {2}\n"
          "Расстояние: {3}\n".format(
                                closest_bar["Cells"]["Name"],
                                closest_bar["Cells"]["SeatsCount"],
                                closest_bar["Cells"]["Address"],
                                closest_bar["Cells"]["Distance"]))

