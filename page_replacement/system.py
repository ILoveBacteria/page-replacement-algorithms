class Memory:
    def __init__(self, frames):
        self.frames = frames
        self.frame_list = []
        self.page_faults = 0
        self.page_hits = 0
