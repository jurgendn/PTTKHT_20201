from itertools import combinations
from time import time

import matplotlib.pyplot as plt
import numpy as np

from search import AntColonyOptimizer


class GreedyOptimization:

    def __init__(self, forward_steps=1):
        """Khởi tạo các attr

        Args:
            forward_steps (int, optional): [description]. Defaults to 1.
        """
        self.forward_steps = forward_steps

        self.original_map = None

        self.nodes_list = np.array([])
        self.available_nodes = np.array([])
        self.visited_nodes = np.array([], dtype=np.int16)

        self.best_path = np.array([])
        self.best = None

    def __get_next_k_nodes(self, current_node) -> list:
        """Lấy ra k - nearest neighbors tiếp theo kể từ vị trí hiện tại

        Args:
            current_node (int): Vị trí hiện tại của người
            k (int, optional): Số k - lân cận gần nhất tính từ vị trí hiện tại.
                                Mặc định là 2.

        Returns:
            list: Danh sách k - nodes lân cận gần nhất tính từ vị trí hiện tại
        """
        # Các vị trí chưa được duyệt
        available_nodes = self.available_nodes

        # k node kể từ node hiện tại
        k_step = []

        # Chọn k, trong trường hợp số node còn lại nhỏ hơn
        k = list(
            filter(lambda x: x < available_nodes.shape[0] + 1,
                   list(range(1, self.forward_steps + 1))))[-1]

        # Lặp từng bước để lấy ra đường đi ngắn nhất theo
        for i in range(k):

            # Nếu không còn node nào đi được, dừng thuật toán
            if available_nodes.shape[0] == 0:
                break

            # Các node có thể đi
            available_path = self.original_map[current_node][available_nodes]

            # Lân cận gần nhất mà còn chưa được duyệt
            min_val = np.amin(available_path)
            next_neighbor = list(
                set(np.where(self.original_map[current_node] == min_val)
                    [0]).intersection(available_nodes))[0]

            # Thêm vào danh sách
            k_step.append(next_neighbor)

            # Chuyển sang node kế tiếp
            current_node = next_neighbor

            # Xóa node đó ra khỏi danh sách các node có thể đi
            available_nodes = np.delete(
                available_nodes, np.where(available_nodes == current_node))

        return k_step

    def __get_next_k_possible_paths(self, current_node):
        if self.available_nodes.shape[0] == 0:
            return []
        available_nodes = self.available_nodes
        k = list(
            filter(lambda x: x < available_nodes.shape[0] + 1,
                   list(range(1, self.forward_steps + 1))))[-1]
        return np.array(list(combinations(available_nodes, r=k)))

    def __get_all_possible_k_neighbors(self, current_node):
        possible_path = self.__get_next_k_possible_paths(current_node)
        return possible_path

    def __get_distance(self, path):
        axis_1 = path[:-1]
        axis_2 = path[1:]
        return self.original_map[axis_1, axis_2].sum()

    def __evaluate_heuristic_distance(self, possible_paths):
        distance_list = self.original_map[possible_paths[:, :-1],
                                          possible_paths[:, 1:]]
        # print(distance_list)
        return np.sum(distance_list, axis=1)

    def __get_next_move(self, current_node):
        possible_path = self.__get_all_possible_k_neighbors(current_node)
        possible_path = np.array(list(map(list, possible_path)), dtype=np.int32)
        possible_path = np.insert(possible_path, 0, current_node, axis=1)
        # print(possible_path)
        distance_list = self.__evaluate_heuristic_distance(possible_path)
        minimum_path = possible_path[np.argmin(distance_list)]
        return minimum_path[1]

    def __fit_best_path(self, distance_matrix):
        self.original_map = distance_matrix
        self.nodes_list = np.array(list(range(self.original_map.shape[0])))
        self.__best_each_start = []
        self.__best_path_each_start = []
        for start in self.nodes_list:
            self.best = 0
            self.visited_nodes = np.array([], dtype=np.int16)

            self.available_nodes = np.array(
                list(range(self.original_map.shape[0])))

            current_node = start
            self.available_nodes = np.delete(
                self.available_nodes,
                np.where(self.available_nodes == current_node))
            self.visited_nodes = np.append(self.visited_nodes, current_node)

            while self.available_nodes.shape[0] > 0:
                current_node = self.__get_next_move(current_node)
                self.visited_nodes = np.append(self.visited_nodes, current_node)
                self.available_nodes = np.delete(
                    self.available_nodes,
                    np.where(self.available_nodes == current_node))
                self.best += self.original_map[self.visited_nodes[-2],
                                               self.visited_nodes[-1]]

            self.__best_path_each_start.append(self.visited_nodes)
            self.__best_each_start.append(self.best)
        self.best = np.amin(self.__best_each_start)

        self.best_path = self.__best_path_each_start[np.argmin(
            self.__best_each_start)]

    def __fit_best_cycle(self, distance_matrix):
        self.original_map = distance_matrix
        self.nodes_list = np.array(list(range(self.original_map.shape[0])))
        self.best = 0
        self.visited_nodes = np.array([], dtype=np.int16)

        self.available_nodes = np.array(list(range(self.original_map.shape[0])))

        current_node = 0
        self.available_nodes = np.delete(
            self.available_nodes,
            np.where(self.available_nodes == current_node))
        self.visited_nodes = np.append(self.visited_nodes, current_node)

        while self.available_nodes.shape[0] > 0:
            # print(f"Iteration at: {self.visited_nodes.shape[0]}")
            current_node = self.__get_next_move(current_node)
            self.visited_nodes = np.append(self.visited_nodes, current_node)
            self.available_nodes = np.delete(
                self.available_nodes,
                np.where(self.available_nodes == current_node))
            self.best += self.original_map[self.visited_nodes[-2],
                                           self.visited_nodes[-1]]

        self.best += self.original_map[self.visited_nodes[-1],
                                       self.visited_nodes[0]]
        self.best_path = np.append(self.visited_nodes, 0)

    def fit(self, problem, mode='cycle'):
        if mode == 'cycle':
            self.__fit_best_cycle(problem)
        elif mode == 'path':
            self.__fit_best_path(problem)
        else:
            print("Invalid mode. Only 'cycle' or 'path'!")


problem = np.random.uniform(1, 1.5, (100, 100))
problem = problem.dot(problem.T)

best = {}

aco = AntColonyOptimizer(10, 0.2, 3, 0.5, 0.5)
aco_time = time()
aco.fit(problem, 1000, early_stopping_count=20)
aco_time = time() - aco_time

step_range = [1, 2, 3]
for r in step_range:
    opt = GreedyOptimization(forward_steps=r)
    exec_time = time()
    opt.fit(problem)
    exec_time = time() - exec_time
    best[f'Forward Steps {opt.forward_steps}'] = [
        opt.best, opt.best_path, exec_time
    ]

best['Ant Colony Opt'] = [aco.best, aco.best_path, aco_time]

for step, val in best.items():
    plt.bar(x=step, height=val[2])

plt.xlabel("Methods")
plt.ylabel("Time")
plt.show()

print(best)
