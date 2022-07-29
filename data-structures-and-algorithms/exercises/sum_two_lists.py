# In this exercise, you are required to sum two linked lists and return the sum embedded in another linked list.

#The first number that we append to the linked list represents the unit place and will be the least significant digit of a number.
# The next numbers appended to the linked list will subsequently represent the tenth, hundredth, thousandth, and so on places.

# My solution (I know this is messy, but I tried to train the new concepts)

    def sum_two_lists(self, llist):
        num1, num2, power = 0, 0, 0
        p = self.head
        while p:
            num1 += p.data * 10 ** power
            power += 1
            p = p.next
        power = 0
        p = llist.head
        while p:
            num2 += p.data * 10 ** power
            power += 1
            p = p.next
        num1 += num2
        power = len(str(num1)) - 1
        result = LinkedList()

        def _aux_div(n, p):
            while p > 0:
                n //= 10
                p -= 1
            return n

        while power >= 0:
            result.prepend(_aux_div(num1, power))
            num1 %= (10 ** power)
            power -= 1

        return result
      
      
# Educative solution

def sum_two_lists(self, llist):
  p = self.head  
  q = llist.head

  sum_llist = LinkedList()

  carry = 0
  while p or q:
      if not p:
          i = 0
      else:
          i = p.data
      if not q:
          j = 0 
      else:
          j = q.data
      s = i + j + carry
      if s >= 10:
          carry = 1
          remainder = s % 10
          sum_llist.append(remainder)
      else:
          carry = 0
          sum_llist.append(s)
      if p:
          p = p.next
      if q:
          q = q.next
  return sum_llist
