# In this exercise, you are required to find pairs from a doubly linked list which sum to a specified number.

# My solution

  def pairs_with_sum(self, sum_val):  
    i, j = self.head, self.head
    result = []
    print(result)
    while i:
      while j:
        if i.data + j.data == sum_val and '({},{})'.format(j.data, i.data) not in result:
          result.append('({},{})'.format(i.data, j.data))
        j = j.next
      i = i.next
      j = self.head
    return result
  
  # Educative solution is better because it handles the duplicate by making 'j' always after 'i'.
  # It also takes less time because of it
  
  def pairs_with_sum(self, sum_val):
  pairs = list()
  p = self.head 
  q = None 
  while p:
    q = p.next
    while q:
      if p.data + q.data == sum_val:
          pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
      q = q.next
    p = p.next
  return pairs
