# In this exercise, you are required to determine whether a given linked list is a circular linked list or not. 
# Your solution should return True or False to indicate if the linked list that was passed in to the method is circular or not.

# My solution

    def is_circular_linked_list(self, input_list):
        if input_list.head.next == input_list.head:
            return True
        else:
            cur = input_list.head
            while cur.next != input_list.head and cur.next != None:
                cur = cur.next
            if cur.next == input_list.head:
                return True
            else:
                return False 
              
# Educative solution (way better and handles the empty list case)

    def is_circular_linked_list(self, input_list):
      if input_list.head:
        cur = input_list.head
        while cur.next:
          cur = cur.next
          if cur.next == input_list.head:
            return True
        return False
      else:
        return False
