'''
Создать функцию point_in_polygon(*points)→ bool, которая принимает список координат точек.
Этот список может иметь произвольную четную длину больше или равную 8.
Первая пара точек – это координаты точек, для который мы хотим узнать информацию о том,
принадлежит ли она многоугольнику или нет. Остальные пары – это координаты вершин многоугольника.
Гарантируется, что многоугольник имеет не меньше 3 вершин, и является выпуклым.
Функция должна вернуть True, если заданная точка принадлежит многоугольнику
(находится внутри, или на границе многоугольника), False – если точка не принадлежит многоугольнику
'''


def point_in_polygon(*points) -> bool:
    try:
        secondPol = [points[2], points[3], *points[2:]]
    except:
        raise Exception(*points)
    try:
        square1 = square_polygon(*points)
    except:
        raise Exception(*points)
    try:
        square2 = square_polygon(*secondPol)
    except:
        raise Exception(*points)
    if square1 == square2:
        return True
    return False


def square_polygon(*points):
    px = points[0]
    py = points[1]
    length = len(points) - 1
    square = 0
    for x in range(2, length - 1, 2):
        point1x = points[x]
        point1y = points[x+1]
        point2x = points[x+2]
        points2y = points[x+3]
        square += square_triangle(px, py, point1x, point1y, point2x, points2y)
    square += square_triangle(px, py, points[-2], points[-1], points[2], points[3])
    return square


def square_triangle(x1, y1, x2, y2, x3, y3):
    return (1/2)*abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))


print(point_in_polygon(-1, 0, -1, 0, 0, 3, 3, 0, 1, -3))