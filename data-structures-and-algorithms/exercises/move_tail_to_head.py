

# My solution (the indentation was needed since it is a class method)

    def move_tail_to_head(self):
        o = None
        p = None
        q = self.head
        while q:
            o = p
            p = q
            q = q.next
        o.next = None
        p.next = self.head
        self.head = p

    
# My solution 2 (I knew that using three variables was a little over and tried to do it in other way.)

    def move_tail_to_head(self):
        p = None
        q = self.head
        while q.next:
            p = q
            q = q.next
        p.next = None
        q.next = self.head
        self.head = q

        
# Educative solution (basically the same, but it handles invalid cases... less than 1 node)

    def move_tail_to_head(self):
      if self.head and self.head.next:
        last = self.head 
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head 
        second_to_last.next = None 
        self.head = last
