def remove_duplicates(lst: list) -> list:
    present = set()
    result = []
    for item in lst:
        if item in present:
            continue
        present.add(item)
        result.append(item)

    return result


def add_elements(lst1: list, lst2: list) -> list:
    return lst1 + lst2


def add_element(lst: list, item) -> list:
    return add_elements(lst, [item])


def add_elements_wo_dups(lst1: list, lst2: list) -> list:
    return remove_duplicates(
        add_elements(lst1, lst2)
    )
