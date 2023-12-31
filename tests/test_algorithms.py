import unittest
from page_replacement.system import Memory
from page_replacement.algorithms import fifo, lru, second_chance


class MyTestCase(unittest.TestCase):
    def test_fifo(self):
        reference_sequence = [10, 1, 2, 3, 10, 1, 10, 1, 2, 3, 4]
        memory = Memory(3)

        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1, 2})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 2, 3})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 2, 3})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1, 3})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 3})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 3})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 2})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 3, 2})
        fifo(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {4, 3, 2})

    def test_lru1(self):
        reference_sequence = [10, 1, 2, 3, 10, 1, 10, 1, 2, 3, 4]
        memory = Memory(3)

        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1, 2})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 2, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 2, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {10, 1, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 10, 2})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 3, 2})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {4, 3, 2})

    def test_lru2(self):
        reference_sequence = [7, 8, 1, 8, 3, 1, 4, 2, 3, 8, 3, 9]
        memory = Memory(3)

        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {7})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {7, 8})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {7, 8, 1})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {7, 8, 1})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 8, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {8, 3, 1})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {3, 1, 4})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {1, 4, 2})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {4, 2, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {2, 3, 8})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {2, 8, 3})
        lru(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {9, 8, 3})

    def test_second_chance1(self):
        reference_sequence = [10, 1, 2, 3, 10, 1, 10, 1, 2, 3, 4]
        memory = Memory(3)

        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(10, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(10, 0), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(10, 0), (1, 0), (2, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(3, 0), (1, 0), (2, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(10, 0), (2, 0), (3, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 0), (3, 0), (10, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 0), (3, 0), (10, 1)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 1), (3, 0), (10, 1)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 1), (2, 0), (10, 1)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 0), (3, 0), (10, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(1, 0), (3, 0), (4, 0)})

    def test_second_chance2(self):
        reference_sequence = [7, 8, 1, 8, 3, 1, 4, 2, 3, 8, 3, 9]
        memory = Memory(3)

        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(7, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(7, 0), (8, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(7, 0), (8, 0), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(7, 0), (8, 1), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(3, 0), (8, 1), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(3, 0), (8, 1), (1, 1)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(8, 0), (4, 0), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(2, 0), (4, 0), (1, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(2, 0), (4, 0), (3, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(2, 0), (8, 0), (3, 0)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(2, 0), (8, 0), (3, 1)})
        second_chance(memory, reference_sequence.pop(0))
        self.assertSetEqual(set(memory.frame_list), {(9, 0), (8, 0), (3, 1)})


if __name__ == '__main__':
    unittest.main()
