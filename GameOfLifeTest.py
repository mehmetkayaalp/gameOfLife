import unittest
from GameOfLife import *


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        # Volkan
        neighbor_array = [0, 0, 0, 0, 0, 0, 0, 0]
        is_alive = 1
        self.cell = Cell(neighbor_array, is_alive)

    def setUpSocialCell(self):
        neighbor_array = [1, 0, 0, 1, 0, 0, 1, 0]
        is_alive = 1
        self.cell = Cell(neighbor_array, is_alive)

    def setUpTwoNeigbourCell(self):
        neighbor_array = [0, 0, 0, 1, 0, 0, 1, 0]
        is_alive = 1
        self.cell = Cell(neighbor_array, is_alive)

    def setUpOverCrowdedCell(self):
        neighbor_array = [1, 1, 1, 1, 1, 1, 1, 1]
        is_alive = 1
        self.cell = Cell(neighbor_array, is_alive)

    def test_get_number_of_neighbour(self):
        self.assertEqual(8, self.cell.get_neighbor_array_length())

    def test_print_cell(self):
        self.assertEqual("Adana", self.cell.__str__())

    def test_cell_alive(self):
        self.assertEqual(True, self.cell.is_cell_alive())

    def test_killed_cell(self):
        self.assertEqual("Killed", self.cell.kill_cell())

    def test_already_killed(self):
        neighbor_array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.cell = Cell(neighbor_array, 0)
        self.assertEqual("Already killed", self.cell.kill_cell())

    def test_cell_alone(self):
        self.assertEqual("Cell was so alone so it dies", self.cell.is_cell_alone())

    def test_social_cell_alone(self):
        self.setUpSocialCell()
        self.assertEqual("Cell is so social so it is living", self.cell.is_cell_alone())

    def test_cell_overcrowded(self):
        self.setUpOverCrowdedCell()
        self.assertEqual("Cell could not find something to eat so it died", self.cell.is_cell_overcrowded())

    def test_cell_eating(self):
        self.setUpSocialCell()
        self.assertEqual("Cell is eating something now, it is happy", self.cell.is_cell_overcrowded())

    def test_cell_surviving_with_three_neigbours(self):
        self.setUpSocialCell()
        self.assertEqual("Cell is living", self.cell.is_cell_surviving())

    def test_cell_surviving_with_two_neigbours(self):
        self.setUpTwoNeigbourCell()
        self.assertEqual("Cell is living", self.cell.is_cell_surviving())

    def test_cell_reproding(self):
        self.setUpSocialCell()
        self.assertEqual("Neigbour's 1 place has now a neigbour", self.cell.reproduce_cell())

if __name__ == '__main__':
    unittest.main()
