from .system import Memory


def fifo(memory: Memory, page):
    if page not in memory.frame_list:
        memory.page_faults += 1
        if len(memory.frame_list) == memory.frames:
            memory.frame_list.pop(0)
        memory.frame_list.append(page)
    else:
        memory.page_hits += 1


def lru(memory: Memory, page):
    if page not in memory.frame_list:
        memory.page_faults += 1
        if len(memory.frame_list) == memory.frames:
            memory.frame_list.pop(0)
        memory.frame_list.append(page)
    else:
        memory.page_hits += 1
        memory.frame_list.remove(page)
        memory.frame_list.append(page)


def second_chance(memory: Memory, page):
    if page in map(lambda x: x[0], memory.frame_list):
        memory.page_hits += 1
        # Turn the chance bit true
        for i, v in enumerate(memory.frame_list):
            if v[0] == page:
                memory.frame_list[i] = (page, 1)
                return

    memory.page_faults += 1
    if not len(memory.frame_list) == memory.frames:
        memory.frame_list.append((page, 1))
    else:
        while True:
            victim, bit = memory.frame_list.pop(0)
            if bit:
                memory.frame_list.append((victim, 0))
                continue
            memory.frame_list.append((page, 1))
            break
