from page_replacement.algorithms import fifo, lru, second_chance
from page_replacement.system import Memory


def main():
    n = int(input('Number of frames: '))
    memory_fifo = Memory(n)
    memory_lru = Memory(n)
    memory_second_chance = Memory(n)

    while True:
        page = int(input('Page: '))
        if page == -1:
            break
        fifo(memory_fifo, page)
        lru(memory_lru, page)
        second_chance(memory_second_chance, page)
        print('FIFO: ', '-'.join(map(str, memory_fifo.frame_list)))
        print('LRU: ', '-'.join(map(str, memory_lru.frame_list)))
        print('Second Chance: ', '-'.join(map(lambda x: str(x[0]), memory_second_chance.frame_list)), end='\n\n')

    print(f'FIFO: Page faults = {memory_fifo.page_faults}, Page hits = {memory_fifo.page_hits}')
    print(f'LRU: Page faults = {memory_lru.page_faults}, Page hits = {memory_lru.page_hits}')
    print(f'S-Chance: Page faults = {memory_second_chance.page_faults}, Page hits = {memory_second_chance.page_hits}')


if __name__ == '__main__':
    main()
