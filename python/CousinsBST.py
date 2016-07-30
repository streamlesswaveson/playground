class CousinsBST:

    @classmethod
    def are_cousins(cls, head, a, b):
        q = QueueWithStacks()
        a_level = -1
        b_level = -1
        a_parent = None
        b_parent = None
        q.enqueue((head, 0, None))
        while not q.is_empty():
            (node, level, parent) = q.dequeue()
            if node.data == a:
                a_level = level
                a_parent = parent
            if node.data == b:
                b_level = level
                b_parent = parent
            if node.left:
                q.enqueue((node.left, level + 1, node))
            if node.right:
                q.enqueue((node.right, level + 1, node))

        print 'a_level = ' + str(a_level)
        print 'b_level = ' + str(b_level)
        print 'a_parent = ' + str(a_parent)
        print 'b_parent = ' + str(b_parent)
        if a_level < 0 or b_level < 0: return False
        if a_parent and b_parent:
            if a_level == b_level:
                if a_parent != b_parent:
                    return True
        return False