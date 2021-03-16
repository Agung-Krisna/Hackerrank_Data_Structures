#!/usr/bin/env python3

#This is my interpretation of the linked list that are demonstrated in the 
#Hackerrank Data Structures: Linked List


#making a class (template) for the individual nodes.
class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data


#making a class for the linked list so that we can keep track of our linked list.
class Linked_List:
    def __init__ (self):
        #in every linked list, even though it's not yet appended or prepended with data, 
        #it must have a head node, which contains no data.
        
        self.head = Node()
    
    def append(self, data):
        #we need to start a node from where we iterate through our linked list
        #here, we're using a variable called current_node, which hold the value of the dataless Node.
        
        current_Node = self.head
        
        #if the head pointer is equal to None type, we can just initiate the data
        #to the next node of our current_node without the need of iterating through the data.

        if (self.head == None):
            current_Node.next = Node(data)
            return
        
        #keep iterating through the linked list while the next node is not equal to None type.
        while (current_Node.next != None):
            current_Node = current_Node.next
        
        #after the iteration reached a None type, we can add the data to the next node of our current_Node.
        current_Node.next = Node(data)
    
    def print(self):
        current_Node = self.head
        if (current_Node.data != None):
            print(current_Node.data)
        while (current_Node.next != None):
            current_Node = current_Node.next
            
            #in here we're immediately printing the data to the console.
            print(current_Node.data)

    def prepend(self, data):
        new_head = Node(data)
        #added this variable because the head is dataless, 
        #hence, when you try to print the data, it would contain None
        head_with_data = self.head
        new_head.next = head_with_data.next
        head_with_data.next = new_head

    def deleteWithData(self, data):
        done = False
        current_Node = self.head
        if (current_Node.next == None):
            print("sorry, linked list is empty")
            return
        
        while(current_Node.next != None):
            #what we did here is that we're checking if the data that are contained in the next node is 
            #equal to the data that we're trying to delete, 
            #we're going to skip the next node, and go to the next.next node
            if (current_Node.next.data == data):
                current_Node.next = current_Node.next.next
                done = True
                break
            current_Node = current_Node.next
        if (done == False):
            print("Value {} not found, no changes are made to the linked list".format(data))

    #new function, not present in the demonstration
    def deleteWithIndex(self, index):
        Index = 0
        current_Node = self.head
        while (current_Node.next != None):
            current_Node = current_Node.next
            Index += 1
            if (index == Index):
                current_Node.next = current_Node.next.next
                break


#if you want to do this interactively, do it yourself, I'm only interested in re-learning linked list.
new_list = Linked_List()

#the data are [12, 7, 2, 6, 5, 9, 10]
new_list.append(2)
new_list.append(6)
new_list.append(5)
new_list.append(9)
new_list.prepend(7)
new_list.prepend(12)
new_list.append(10)
new_list.deleteWithData(10)
new_list.deleteWithIndex(2)
new_list.print()
