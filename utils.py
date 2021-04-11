def add_vectors(v1, v2):
    """Sum two tuples as if they are vectors."""
    assert len(v1) == 2
    assert len(v2) == 2
    return (v1[0] + v2[0], v1[1] + v2[1])


def subtract_vectors(v1, v2):
    """Subtract two tuples as if they are vectors."""
    assert len(v1) == 2
    assert len(v2) == 2
    return (v1[0] - v2[0], v1[1] - v2[1])


def update_tuple_element(tuple, new_val, idx):
    assert len(tuple) <= 2
    if idx == 0:
        return (new_val, tuple[1])
    if idx == 1:
        return (tuple[0], new_val)