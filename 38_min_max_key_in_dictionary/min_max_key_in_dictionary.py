def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    result = set(d.keys())

    sorted_keys = sorted(result)
    max_min = sorted_keys[0], sorted_keys[-1]

    return tuple(max_min)

    #ORRR

    keys = d.keys()

    return (min(keys), max(keys))