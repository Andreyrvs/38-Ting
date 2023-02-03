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
        return self.queue.pop()

    def search(self, index):
        """Aqui irá sua implementação"""
