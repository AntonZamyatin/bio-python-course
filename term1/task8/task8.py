"""Task 8."""


class QueueNode(object):
    """Node: Class for single node of LinkedQueue."""

    def __init__(self, elem, nextnode):
        """Method. Initializes new node."""
        self.value = elem
        self.next = nextnode


class QueueIterator(object):
    """QueueIterator: Iterator for LinkedQueue."""

    def __init__(self, node, count):
        """Method. Initializes new Iterator."""
        self.out = node
        self.count = count

    def __next__(self):
        """Method. Returns next element of queue: next(iter)."""
        if self.count == 0:
            raise StopIteration
        else:
            out = self.out.value
            self.out = self.out.next
            self.count -= 1
            return out


class LinkedQueue(object):
    """LinkedQueue."""

    def __init__(self):
        """Method. Initializes new queue."""
        self.enter = None
        self.out = None
        self.count = 0

    def push(self, elem):
        """Method. Pushes 'elem' to queue."""
        if not self.count:
            self.enter = QueueNode(elem, None)
            self.out = self.enter
            self.count = 1
        else:
            new_node = QueueNode(elem, None)
            self.enter.next = new_node
            self.enter = new_node
            self.count += 1

    def pop(self):
        """Method. Removes front of queue and returns it."""
        out = self.out.value
        self.out = self.out.next
        self.count -= 1
        return out

    def front(self):
        """Method. Returns front of queue."""
        return self.out.value

    def empty(self):
        """Method. Checks whether queue is empty."""
        return not self.count

    def __iter__(self):
        """Method. Returns Iterator for queue: iter(queue)."""
        return QueueIterator(self.out, self.count)

    def __len__(self):
        """Method. Returns size of queue: len(queue)."""
        return self.count

    def clear(self):
        """Method. Makes queue empty."""
        self.enter = None
        self.out = None
        self.count = 0
