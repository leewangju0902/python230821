def compare_data_structures():
    # Lists
    list_example = [1, 2, 3]
    list_example.append(4)
    list_example[0] = 0
    list_example.pop()
    list_pros = "Mutable, ordered, allows duplicates"
    list_cons = "Slower lookup, linear time removal"

    # Tuples
    tuple_example = (1, 2, 3)
    tuple_pros = "Immutable, ordered, slightly faster than lists"
    tuple_cons = "Cannot be modified after creation"

    # Sets
    set_example = {1, 2, 3}
    set_example.add(4)
    set_example.remove(1)
    set_pros = "Unordered, no duplicates, fast membership testing"
    set_cons = "No indexing, elements are not ordered"

    # Dictionaries
    dict_example = {'a': 1, 'b': 2, 'c': 3}
    dict_example['d'] = 4
    dict_example.pop('a')
    dict_pros = "Key-value pairs, fast lookups, flexible keys"
    dict_cons = "Unordered (Python 3.7 and earlier), keys must be hashable"

    print("List:")
    print(f"Pros: {list_pros}")
    print(f"Cons: {list_cons}\n")

    print("Tuple:")
    print(f"Pros: {tuple_pros}")
    print(f"Cons: {tuple_cons}\n")

    print("Set:")
    print(f"Pros: {set_pros}")
    print(f"Cons: {set_cons}\n")

    print("Dictionary:")
    print(f"Pros: {dict_pros}")
    print(f"Cons: {dict_cons}\n")

compare_data_structures()
