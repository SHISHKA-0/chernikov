import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
with open('ЛАБАСУКАХУЕТА.txt', 'r') as f:# сначала в файл записать подогнанные данные периода
    for line in  f:
        s = line.split(' ')
        x.append(float(s[0]))
        y.append(float(s[1]))
x=np.array(x)# ВНИМАТЕЛЬНО ПРОРАБОТАТЬ ВСЕ ДЕТАЛИ КОДА НА НАХОЖДЕНИЕ МАССЫ ДИСКА И НАЧАЛЬНОГО МОМЕНТА ИНЕРЦИИ
y=np.array(y)
x = x ** 2
y = 4.013*(10**(-4))*((1.5361+0.9657)*(y**2))-7.43*10**(-3)# момент инерции платформы
def lin_ls(x, y):
    k = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
    b = np.mean(y) - k * np.mean(x)
    return (k, b)

M, I0 = lin_ls(x, y)
print("Масса диска по графику (дополнительно умножить на 10**4) : ",
     M,"\nМомент инерции относительно оси, проходящей через центр масс диска : ", I0)
x_err = 0.141
y_err = 2.907 * ( 10 ** (-4)) # отдельно посчитать погрешность получившегося момента инерции
plt.errorbar(x, y, xerr=x_err, yerr=y_err, lw =1, capsize = 4, capthick = 1.5, elinewidth=0.5, label = "График зависимости момента инерции системы от расстояния каждой из половинок до оси вращения" )
plt.plot(np.linspace(0,32, 1000), I0 + M * np.linspace(0,32, 1000))

plt.ticklabel_format(style='sci',
                     axis='both',
                     scilimits=(0, 0),
                     useMathText=True)

plt.minorticks_on()

plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=1,
         color='0.8')

plt.xlim([0, np.max(x) * 1.05])
plt.ylim([0.001, np.max(y) * 1.05])

plt.xlabel(" Расстояние от центра масс половинки диска до оси вращения h^2, см^2  ")
plt.ylabel(" Момент инерции системы двух половинок двойного диска I, кгхм^2")

plt.show()
