'''
 Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

'''

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.queue_tmp = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.move(1)
        self.queue.append(x)
        self.move(2)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        try:
            return self.queue.pop()
        except IndexError:
            return None


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0

    def move(self, n):
        if n == 1:
            for _ in range(len(self.queue)):
                self.queue_tmp.append(self.queue.pop())
        else:
            for _ in range(len(self.queue_tmp)):
                self.queue.append(self.queue_tmp.pop())


