# In this exercise, you are required to remove the duplicates from a doubly linked list.
# In the exercise widget, the delete_node method has been given to you. 
# It is a slight modification of the delete method we covered in one of the previous lessons. 
# You have to figure out the modification yourself. 
# The hint is to recall the remove_duplicates lesson from one of the previous chapters.

# My solution

  def remove_duplicates(self):
    dups = []
    cur = self.head
    while cur:
      nxt = cur.next
      if cur.data in dups:
        self.delete_node(cur)
      else:
        dups.append(cur.data)
      cur = nxt
      
  def delete_node(self, node):
    cur = self.head
    while cur:
      if cur == node and cur == self.head:
        # Case 1:
        if not cur.next:
          cur = None 
          self.head = None
          return

        # Case 2:
        else:
          nxt = cur.next
          cur.next = None 
          nxt.prev = None
          cur = None
          self.head = nxt
          return 

      elif cur == node:
        # Case 3:
        if cur.next:
          nxt = cur.next 
          prev = cur.prev
          prev.next = nxt
          nxt.prev = prev
          cur.next = None 
          cur.prev = None
          cur = None
          return

        # Case 4:
        else:
          prev = cur.prev 
          prev.next = None 
          cur.prev = None 
          cur = None 
          return 
      cur = cur.next
      
# Educative solution

def remove_duplicates(self):
  cur = self.head 
  seen = dict()
  while cur:
    if cur.data not in seen:
      seen[cur.data] = 1
      cur = cur.next
    else:
      nxt = cur.next
      self.delete_node(cur)
      cur = nxt
