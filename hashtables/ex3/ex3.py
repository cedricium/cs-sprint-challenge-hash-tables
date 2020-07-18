def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_arrays = len(arrays)
    number_cache = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in number_cache:
                number_cache[num] = 1
            else:
                number_cache[num] += 1
                if number_cache[num] == num_arrays:
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
