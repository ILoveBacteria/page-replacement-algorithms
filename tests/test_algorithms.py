import unittest
from page_replacement.system import Memory
from page_replacement.algorithms import fifo, lru


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

    def test_lru(self):
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

if __name__ == '__main__':
    unittest.main()
