from sense_hat import SenseHat


# roulis en degres
# tangage en degres
# lacet en degree
# structure contenant les paramètres de vol de l'avion
class plane():
    def __init__(self, roulis, tangage, lacet):
        self.roulis = roulis
        self.tangage = tangage
        self.lacet = lacet


# initialisation du sense hat
sense = SenseHat()

# compas : desactive | gyroscope : active | accelerometre : desactive
sense.set_imu_config(False, True, False)

# recupere les donnees initiales d'orientation selon les trois axes
sens.show_message("Getting orientation data...", text_colour=[255, 0, 0])
orientation = sense.get_gyroscope()

# message console de debug, pas affiche sur le sense hat, mais sur un terminal
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# assigne les paramètres gyroscope a la structure
def get_gyroscope_info():
    orientation = sense.get_gyroscope()
    return (plane(orientation.roulis, orientation.tangage, orientation.lacet))


def axe_calculus(axe):
    if axe < 0:
        return (axe % -90) * (-1)
    else:
        return axe % 90


def get_o_max(l, r, t):
    o_max = l
    if r > o_max:
        o_max = r
    if t > o_max:
        o_max = t


# affiche la lettre R si le roulis est le plus important, T si le tangage est le plus important, ou L si le lacet est le plus important
def display_status(avion):
    l = axe_calculus(avion.lacet)
    r = axe_calculus(avion.roulis)
    t = axe_calculus(avion.tangage)
    o_max = get_o_max(l, r, t)
    if o_max == l:
        sense.show_letter("L")
    if o_max == t:
        sense.show_letter("T")
    if o_max == r:
        sense.show_letter("R")

# tant que le sense hat n'est pas incliné à 90 degre dans un des deux axes (tangage et roulis), on continue a recuperer les parametres
while (avion.roulis <= 90 and avion.roulis >= -90 and avion.tangage <= 90 and avion.tangage >= -90):
    avion = get_gyroscope_info()
    display_status(avion)
