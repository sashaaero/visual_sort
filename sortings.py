def bubble(arr, plt):
    coordinates = list(range(len(arr)))
    colors = ['b'] * len(arr)
    r = len(arr) - 1
    if r <= 0:
        return

    while r >= 1:
        i, max_val = 0, 1
        while i <= r:
            if i >= 1:
                colors[i-1] = 'b'
            colors[i] = 'r'
            colors[max_val] = 'y'
            plt.bar(coordinates, arr, color=colors)
            plt.draw()
            plt.pause(0.0000001)
            # plt.clf()
            if arr[i] > arr[max_val]:
                colors[max_val] = 'b'
                max_val = i
            i += 1
        if r != max_val:
            arr[r], arr[max_val] = arr[max_val], arr[r]
            plt.bar(coordinates, arr, color=colors)
            plt.draw()
            plt.pause(0.0001)
            plt.clf()
            arr.swaps += 1
        r -= 1


