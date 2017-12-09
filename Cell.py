
class Cell(object):
    def __init__(self, neighbor_array, is_alive):
        self.neighbor_array = neighbor_array
        self.is_alive = is_alive

    def __str__(self):
        return "Adana"

    def get_neighbor_array_length(self):
        """
            Returns length of the neighbor.
        :return:
        """
        return len(self.neighbor_array)

    def is_cell_alive(self):
        """

        :return:
        """
        if self.is_alive:
            return True
        else:
            return False

    def kill_cell(self):
        """

        :return:
        """
        if self.is_alive:
            self.is_alive = 0
            return "Killed"
        else:
            return "Already killed"

    def is_cell_alone(self):
        """

        :return:
        """
        if sum(self.neighbor_array) < 2:
            self.kill_cell()
            return "Cell was so alone so it dies"
        else:
            return "Cell is so social so it is living"

    def is_cell_overcrowded(self):
        """

        :return:
        """
        if sum(self.neighbor_array) > 3:
            self.kill_cell()
            return "Cell could not find something to eat so it died"
        else:
            return "Cell is eating something now, it is happy"

    def is_cell_surviving(self):
        """

        :return:
        """
        if sum(self.neighbor_array) == 3 or sum(self.neighbor_array) == 2:
            self.kill_cell()
            return "Cell is living"
        else:
            return "Cell is dead"

    def reproduce_cell(self):
        if sum(self.neighbor_array) == 3:
            zero_index = self.neighbor_array.index(0)
            self.neighbor_array[zero_index] = 1
            return "Neigbour's %s place has now a neigbour" % zero_index
