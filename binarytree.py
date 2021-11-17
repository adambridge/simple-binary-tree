class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        """
        >>> n(0)
        0
        >>> n(0, n(1), n(2))
         0
        1 2
        >>> n(0, n(1, n(2)), n(3, n(4), n(5)))
           0
         1   3
        2   4 5

        Layout:
        h=4 Wn=8 Wc=15
               *        | 7 + 1 + 7
           *       *    | 3 + 1 + 7 + 1 + 3
         *   *   *   *  | 1 + 1*4 + 3*3 + 1
        * * * * * * * * | 1*8 + 1*7
        1. Full width in # of nodes, Wn = 2 ** (height-1)
        2. Left pad at depth 0, lp0 = Wn - 1
        3. Left pad at depth 1, lp1 = (lp0 - 1) / 2     =>  ... 7, 3, 1 (stop at 1)
        4. Spacing at depth 1, s1 = lp0, s2 = lp1, etc
        """
        height = self.height()
        width = 2 ** (height - 1)
        left_pad = width - 1
        spacing = ''
        printableArray = self._printableArray()
        output = []
        for d in range(height):
            output.append(' ' * left_pad + spacing.join(printableArray[d]))
            spacing = ' ' * left_pad
            left_pad = (left_pad - 1) // 2
        return '\n'.join(output)

    def height(self):
        return self._heightRecursor(node=self)

    def _heightRecursor(self, node, acc=0):
        if node is None:
            return acc
        else:
            return max(self._heightRecursor(node.left, acc + 1), self._heightRecursor(node.right, acc + 1))


    def _printableArray(self):
        '''
        >>> n(0)._printableArray()
        [['0']]
        >>> n(0, n(1), n(2))._printableArray()
        [['0'], ['1', '2']]
        >>> n(0, n(1), n(2, n(3)))._printableArray()
        [['0'], ['1', '2'], [' ', ' ', '3', ' ']]
        '''
        height = self.height()
        arr = BinaryTreeNode._emptyTreeArray(height)
        self._printArrayRecursor(node=self, height=height, arr=arr)
        return arr


    def _printArrayRecursor(self, node, height, arr, depth=0, col=0):
        arr[depth][col] = str(node.data)
        if depth < height - 1:
            if node.left:
                self._printArrayRecursor(node.left, height, arr, depth + 1, 2 * col)
            if node.right:
                self._printArrayRecursor(node.right, height, arr, depth + 1, 2 * col + 1)


    def _emptyTreeArray(height):
        '''
        >>> BinaryTreeNode._emptyTreeArray(2)
        [[' '], [' ', ' ']]
        '''
        arr = [[] for _ in range(height)]
        for d in range(height):
            for _ in range(2 ** d):
                arr[d].append(' ')
        return arr


if __name__ == '__main__':
    import doctest

    n = BinaryTreeNode
    doctest.testmod()
