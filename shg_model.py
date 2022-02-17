'''

Author:  Riley Guest

'''

'''
Second harmonic generation simulation.  Showing the relationship
between the SHG and pump. Phase matching as well
'''

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import matplotlib.animation as animation

frequency = 16
amplitude = np.linspace(1, 0, 360)
amplitude_sh = np.linspace(0, 1, 360)
phase_shift_deg = 0
# phase_shift_deg = np.linspace(-180, 0, 360)  # in degrees
phase_shift = phase_shift_deg * np.pi/180
x = np.linspace(-np.pi, 0, 360)
y = np.cos(x * frequency)
y2 = np.cos(x * (2*frequency) + phase_shift)
y3 = y+y2

linewidth = 2.0
fig, ax = plt.subplots()
line1, = ax.plot(x, y, color = "red", linewidth=linewidth, label = r'$\omega_{pump}$')
line2, = ax.plot(x, y2, color = "blue", linewidth=linewidth, label= r'$\omega_{SHG}$')
line3, = ax.plot(x, y3, color = "lime", linewidth=linewidth, label='SHG Output')

def update(num, x, y, y2, y3, line1, line2, line3):
    line1.set_data(x[:num], y[:num])
    line2.set_data(x[:num], y2[:num])
    line3.set_data(x[:num], y3[:num])
    return [line1, line2, line3]

anim = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, y2, y3, line1, line2, line3], interval=20, blit=True)
# plt.xticks([-2*np.pi, 0, 2*np.pi], [r'-2$\pi$', '0', r'2$\pi$'])

ax.set_xlabel(r'$\Delta$k''\nPhase Mismatch')
ax.set_ylabel('Amplitude\nA.u.')
plt.ylim(-1, 2.5)
plt.grid(True)
plt.legend(loc='upper left')
plt.title('Phase matching process in SHG\nWhere $n_{2{\omega}} = n_{\omega}, k_{2{\omega}} = 2k_{\omega} $')
plt.tight_layout()
plt.show()

# f = r"C:\Users\riley\OneDrive\Python\Math\shgpm2.mov"
# # writervideo = animation.FFMpegWriter(fps=100)
# # anim.save(f, writer=writervideo)