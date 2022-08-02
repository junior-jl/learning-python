# The size of the tree is the total number of nodes in a tree. You are required to return the size of a binary tree given the root node of the tree.

# My solution

def size_(self, node):
  if node is None:
    return 0
  return 1 + self.size_(node.left) + self.size_(node.right)
    
# Educative solution 1 (iterative)

def size(self):
  if self.root is None:
      return 0

  stack = Stack()
  stack.push(self.root)
  size = 1
  while stack:
    node = stack.pop()
    if node.left:
      size += 1
      stack.push(node.left)
    if node.right:
      size += 1
      stack.push(node.right)
  return size

# Educative solution 2 (recursive): exactly the same as mine :)
