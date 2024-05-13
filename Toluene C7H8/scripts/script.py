# import numpy as np

# # Исходные координаты молекулы
# coordinates = np.array([
#     [2.189, 2.289, 2.477],
#     [2.200, 2.338, 2.573],
#     [2.238, 2.159, 2.438],
#     [2.285, 2.100, 2.516],
#     [2.119, 2.371, 2.392],
#     [2.085, 2.467, 2.427],
#     [2.211, 2.117, 2.304],
#     [2.236, 2.016, 2.274],
#     [2.099, 2.331, 2.261],
#     [2.050, 2.392, 2.187],
#     [2.134, 2.205, 2.217],
#     [2.099, 2.158, 2.082],
#     [2.123, 2.055, 2.055],
#     [1.993, 2.162, 2.055],
#     [2.135, 2.226, 2.055],
# ])

# list_k = [" CG", " HG", "CD1", "HD1", "CD2", "HD2", "CE1", "HE1", "CE2", "HE2", " CZ", " CT", "H11", "H12", "H13"]

# # Размер сетки
# grid_size = 5

# # Создание сетки для размножения молекул
# x = np.linspace(0, grid_size-1, grid_size)
# y = np.linspace(0, grid_size-1, grid_size)
# z = np.linspace(0, grid_size-1, grid_size)

# # Размножение координат молекулы
# new_coordinates = []
# for i in x:
#     for j in y:
#         for k in z:
#             new_coordinates.extend(coordinates + [i, j, k])

# # Открываем файл для записи
# file_path = 'TOL/coordinates.txt'
# with open(file_path, 'w') as file:
#     for idx in range(len(new_coordinates) // len(coordinates)):
#         for i in range(len(coordinates)):
#             coord = new_coordinates[idx*len(coordinates) + i]
#             if (idx >= 9 and idx < 99): 
#                 if (i+1) <= 9:
#                     file.write(f'    {idx+1}TOLU  {list_k[i]}    {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
#                 else:
#                     file.write(f'    {idx+1}TOLU  {list_k[i]}   {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
#             if (idx <= 9 ): 
#                 if (i+1) <= 9:
#                     file.write(f'    {idx+1}TOLU   {list_k[i]}    {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
#                 else:
#                     file.write(f'    {idx+1}TOLU   {list_k[i]}   {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
#             if (idx >= 99):
#                 if (i+1) <= 9:
#                     file.write(f'    {idx+1}TOLU {list_k[i]}    {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
#                 else:
#                     file.write(f'    {idx+1}TOLU {list_k[i]}   {i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
                
# print("Сохранение завершено. Файл сохранен как 'molecule_coordinates.txt'.")
import numpy as np

# Исходные координаты молекулы
coordinates = np.array([
    [2.189, 2.289, 2.477],
    [2.200, 2.338, 2.573],
    [2.238, 2.159, 2.438],
    [2.285, 2.100, 2.516],
    [2.119, 2.371, 2.392],
    [2.085, 2.467, 2.427],
    [2.211, 2.117, 2.304],
    [2.236, 2.016, 2.274],
    [2.099, 2.331, 2.261],
    [2.050, 2.392, 2.187],
    [2.134, 2.205, 2.217],
    [2.099, 2.158, 2.082],
    [2.123, 2.055, 2.055],
    [1.993, 2.162, 2.055],
    [2.135, 2.226, 2.055],
])

list_k = [" CG", " HG", "CD1", "HD1", "CD2", "HD2", "CE1", "HE1", "CE2", "HE2", " CZ", " CT", "H11", "H12", "H13"]

# Размер сетки
grid_size = 6

# Создание сетки для размножения молекул
x = np.linspace(0, 4, grid_size)
y = np.linspace(0, 4, grid_size)
z = np.linspace(0, 4, grid_size)

# Размножение координат молекулы
new_coordinates = []
for i in x:
    for j in y:
        for k in z:
            new_coordinates.extend(coordinates + [i, j, k])

# Открываем файл для записи
file_path = 'TOL/coordinates.txt'
with open(file_path, 'w') as file:
    for idx in range(len(new_coordinates) // len(coordinates)):
        for i in range(len(coordinates)):
            coord = new_coordinates[idx*len(coordinates) + i]
            # Выбор пробелов в зависимости от длины индекса молекулы и атома
            molecule_spacing = '' if idx >= 99 else '  ' if idx >= 9 else '   '
            atom_spacing = '    ' if (i+1) <= 9 else '   '
            file.write(f'    {idx+1}TOLU{molecule_spacing}{list_k[i]}{atom_spacing}{i+1}   {coord[0]:.3f}   {coord[1]:.3f}   {coord[2]:.3f}\n')
                
print("Сохранение завершено. Файл сохранен как 'molecule_coordinates.txt'.")
