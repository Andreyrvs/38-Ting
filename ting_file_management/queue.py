from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False

    def dequeue(self):
        if len(self.queue) == 0:
            return False
        return self.queue.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
