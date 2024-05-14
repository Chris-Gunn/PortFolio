def find_common_elements(list1, list2):
    common_elements = []

    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(find_common_elements(a, b))
