'''Multiple graphs showing population inversion'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import scipy
from scipy.integrate import odeint
# git test
plt.style.use('ggplot')

Trad = 1
t43 = 0.5

def threelevelLaser(beta, Wp, Trad):
    return ((1-beta)*n*Wp*Trad-1)/((1+2*beta)*n*Wp*Trad+1)

def fourlevelLaser(beta, Wp, Trad):
    return ((1-beta)*n*Wp*Trad)/(1+(1+beta+(2*t43/(Trad))*n*Wp*Trad))

for beta, n, label in[(0, 1,  r'$\beta$ = 0'), (0.25, 1, r'$\beta$ = 0.25'), (0.5, 1, r'$\beta$ = 0.5'), (0.75, 1, r'$\beta$ = 0.75'), (1, 1, r'$\beta$ = 1')]:
    Wp = np.arange(0, 5, .001)
    plt.figure(1)
    plt.plot(Wp, threelevelLaser(beta, Wp, Trad), label=label)
    plt.xlabel('Normalized Pump Rate')
    plt.ylabel('Normalized Population Inversion')
    plt.title("3 Level Laser Population Inversion\n$\eta$ = fluorescent quantum efficiency = 1")
    plt.legend(loc=0)
    plt.figure(2)
    plt.plot(Wp, fourlevelLaser(beta, Wp, Trad), label=label)
    plt.xlabel('Normalized Pump Rate')
    plt.ylabel('Normalized Population Inversion')
    plt.title("4 Level Laser Population Inversion\n$\eta$ = quantum fluorescent efficiency = 1")
    plt.legend(loc=0)

for beta, n in[(0, 1)]:
    plt.figure(3)
    plt.plot(Wp, threelevelLaser(beta, Wp, Trad), label='3 Level Laser')
    plt.plot(Wp, fourlevelLaser(beta, Wp, Trad), label='4 Level Laser')
    plt.axhline(.25, ls='--', color='k', label = 'Laser Threshold')
    plt.xlabel('Normalized Pump Rate')
    plt.ylabel('Normalized Population Inversion')
    plt.title("3 Level Laser Vs. 4 Level Laser Population Inversion\nNote: Y axis; an example of why 3 Level Lasers\n"
              "need more pump energy to start a population inversion")
    plt.legend(loc=0)

for beta, n, label in[(0, 1, r'$\eta$ = 1'), (0, 0.75, r'$\eta$ = 0.75'), (0, 0.5, r'$\eta$ = 0'), (0, 0.25, r'$\eta$ = 0.25'), (0, 0, r'$\eta$ = 0')]:
    Wp = np.arange(0, 5, .001)
    plt.figure(4)
    plt.plot(Wp, threelevelLaser(beta, Wp, Trad), label=label)
    plt.xlabel('Normalized Pump Rate')
    plt.ylabel('Normalized Population Inversion')
    plt.title("3 Level Laser Population Inversion""\n"r"$\beta$ = 0")
    plt.legend(loc=0)
    plt.figure(5)
    plt.plot(Wp, fourlevelLaser(beta, Wp, Trad), label=label)
    plt.xlabel('Normalized Pump Rate')
    plt.ylabel('Normalized Population Inversion')
    plt.title("4 Level Laser Population Inversion""\n"r"$\beta$ = 0")
    plt.legend(loc=0)

plt.show()
# plt.show(2)
# plt.show(3)
# plt.show(4)
# plt.show(5)

