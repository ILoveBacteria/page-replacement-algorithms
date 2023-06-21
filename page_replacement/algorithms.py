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
        for i, (value, bit) in enumerate(memory.frame_list):
            if value == page:
                memory.frame_list[i] = (page, 1)
                return

    memory.page_faults += 1
    if not len(memory.frame_list) == memory.frames:
        memory.frame_list.append((page, 0))
    else:
        page_replace = False
        # While there is no page replacement. If all bits are 1
        while not page_replace:
            for i, (value, bit) in enumerate(memory.frame_list):
                if bit:
                    memory.frame_list[i] = (value, 0)
                    continue
                memory.frame_list.pop(i)
                memory.frame_list.append((page, 0))
                page_replace = True
                break
