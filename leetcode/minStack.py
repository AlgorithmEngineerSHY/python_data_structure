'''
 Design a stack that supports push, pop, top, 
 and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min is None:
            self.min = x
        else:
            if self.min > x:
                self.min = x


    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.stack.pop():
            if len(self.stack) == 0:
                self.min = None
            else:
                self.min = self.stack[0]
                for i in self.stack[1:]:
                    if i < self.min:
                        self.min = i


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]



    def getMin(self):
        """
        :rtype: int
        """
        return self.min



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()