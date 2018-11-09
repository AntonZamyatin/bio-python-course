"""Task 7."""

def valuesunion(*dicts):
    answ = set()
    for d in dicts:
        for el in d.values():
            answ.add(el)
    return answ

if __name__ == "__main__":
    assert valuesunion({1: 2, 4: 8}) == {2, 8}
    assert valuesunion({1: 2}, {4: 8}) == {2, 8}
    assert valuesunion({1: 2, 4: 8}, {'a': 'b'}, {}, {}) == {2, 8, 'b'}
    print("valuesunion - OK")
