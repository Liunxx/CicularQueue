# coding=utf-8

class CircularQueue(object):
    def __init__(self, capacity=2):
        """
        Initialize the queue to be empty with a fixed capacity
        :param capacity: Initial size of the queue
        """
        self._capacity = capacity
        self._size = 0
        self._list = [0] * self._capacity
        self._sum = 0
        self._read = 0
        self._write = 0

    def __str__(self):
        """
        Return a string representation of RunningQueue
        :return: string
        """
        if self._size==0:
            return "Queue is Empty"

        else:
            str1 = " ".join(str(list) for list in self._list if list != 0)
            return str1 + " Sum:" + str(self._sum) + " Capacity:" + str(self._capacity)

    def parse_command(self, command):
        """
        Parse command given from the input stream
        :param command: command from input stream
        :return: None
        """
        content=command.split(" ")
        if content[0]=='a':
           self.enqueue(int(content[1]))
        elif content[0]=='r':
            self.dequeue()
        self.get_sum()

    def enqueue(self, number):
        """
        Add a number to the end of the queue
        :param number: number to add
        :return: None
        """
        self._size += 1
        if (self._size > self._capacity):
            self.resize()
        self._list[self._write] = number
        self._write=(self._write+1)%self._capacity
        if (self._size==self._capacity):
            list=self._list
            index=self._read
            self._list=[0]*self._capacity
            for i in range(self._capacity):
                self._list[i]=list[index]
                index=(index+1)%self._capacity
            self._read=0
            self._write=0

    def dequeue(self):
        """
        Remove an element from the front of the queue
        Do nothing if the queue is empty
        :return: None
        """
        if self._size==0:
            return
        num=self._list[self._read]
        self._list[self._read] = 0
        self._read=(self._read+1)%self._capacity
        self._size -= 1


    def resize(self):
        """
        Resize the queue to be two times its previous size
        :return: None
        """
        list=self._list
        index=self._read
        capacity=self._capacity
        self._capacity *= 2
        self._list = [0] * self._capacity
        for i in range(capacity):
            self._list[i]=list[index]
            index=(index+1)%capacity
        self._read=0
        self._write=capacity


    def get_sum(self):
        """
        Get the sum of the numbers currently in the queue
        :return: sum of the queue
        """
        self._sum=0
        for i in range(self._capacity):
            self._sum+=self._list[i]

