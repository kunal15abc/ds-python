from Elements.Tree import Node


def sortList(node, value):
    if value < node.data:
        if node.left is None:
            node.left = Node(value)
        else:
            sortList(node.left, value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            sortList(node.right, value)


def inorderWithoutRecusrion(root):
    current = root
    while current is not None:
        if current.left is None:
            print (current.data)
            current = current.right
        else:
            current = current.left.right
            current = current.left


if __name__ == '__main__':
    a = [2, 4, 3, 7, 9, 8, 5, 1, 6]
    root = Node(a[0])
    print('test')
    for i in range(1, len(a)):
        sortList(root, a[i])

    root.inorderWithoutRecusrion()
