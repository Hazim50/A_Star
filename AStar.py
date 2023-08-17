class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0 #f(n)=g(n)+h(n)

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list): #açık listedeki en düşük f(x) değerine sahip olan düğümü bul
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            rev_path=path[::-1]
            for i,j in rev_path:
                # print(i,j)
                maze[i][j]=5
            return maze

        children = []
        for new_position in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]: 

            # Düğüm konumu al
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Matrisin içinde mi
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Yürülebilir yol mu
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def main():

    maze = [[0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]]
    # maze = [[0,1,1,0],
    #         [0,0,0,0],
    #         [0,1,0,0],
    #         [0,1,0,0]]

    start = (0, 0)
    end = (9,5)

    path = astar(maze, start, end)
    for i in path:
        print(i)


if __name__ == '__main__':
    main()

"""
1 Başlangıç düğümünü seç ve g(x) değerini hesapla.
2 Başlangıç düğümünü açık düğümler listesine ekle.
3 Açık düğümler listesi boş olana kadar şu adımları tekrarla:
    Açık düğümler listesindeki en düşük f(x) değerine sahip düğümü seç.
    Seçilen düğümü açık düğümler listesinden çıkar ve kapalı düğümler listesine ekle.
    Hedef düğüme ulaşıldıysa, en kısa yol bulunduğu için algoritmayı sonlandır.
    Aksi halde, mevcut düğümün komşularını keşfet.
    Her komşu düğüm için g(x) ve h(x) değerlerini hesapla ve toplam maliyeti f(x) olarak belirle.
    Eğer komşu düğüm zaten açık düğümler listesinde ise, daha iyi bir yol bulunduysa g(x) değerini güncelle.
    Eğer komşu düğüm açık veya kapalı düğümler listesinde değilse, açık düğümler listesine ekle.
4 Hedef düğüme ulaşılamazsa, en kısa yol bulunamadığı için algoritma sonlandırılır."""