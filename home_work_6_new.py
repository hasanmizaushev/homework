def number_1():
    probability_flu = 1 / 9000
    probability_positive = probability_flu * 1 + (1 - probability_flu) * 0.01
    return print('positive probability =', probability_positive)


def number_2():
    probability_flu = 1 / 350
    probability_positive = probability_flu * 1 + (1 - probability_flu) * 0.02
    return print('positive probability =', probability_positive)


def number_3():
    probability_rain = 0.1
    probability_cloudy_rain = 0.5
    probability_cloudy = 0.4
    probability_rain_cloudy = probability_rain * probability_cloudy_rain / probability_cloudy
    return print('probability =', probability_rain_cloudy)


number_1()
number_2()
number_3()
