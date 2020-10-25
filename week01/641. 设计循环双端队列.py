class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = 0
        self.front, self.rear = 0, 0
        self.capacity = k
        self.data = [-1] * k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.front] = value
        else:
            self.front = (self.front - 1) % self.capacity
            self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.data[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.data[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.data[self.front] = -1
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.data[self.rear] = -1
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        if self.isEmpty():
            self.front = self.rear
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self.data[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self.data[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.capacity
