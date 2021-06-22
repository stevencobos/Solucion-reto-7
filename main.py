import matplotlib.pyplot as plt
x = ['Python','Java' ,'PHP', 'JavaScript', 'C#', 'C++']
popularity = [21.3, 16.1, 8.7, 9, 7.4, 6.5]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='green')
plt.xlabel('Lenguaje')
plt.ylabel('Popularidad')
plt.title('Popularidad del lenguaje de programación\n en todo el mundo')
plt.xticks(x_pos, x)

plt.minorticks_on()

plt.show()