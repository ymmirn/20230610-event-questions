class Logic:
    # このファイルのみ提出してください
    # この中に解答を記述してください
    def sort(self, array):
        n = len(array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    # 隣接する要素が逆順になっている場合、交換する
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
