def delete(list_, index=None):
    if index is not None:
        if index < 0:
            index = len(list_) + index
            first_half = list_[: index]
            second_half = list_[index + 1:]
        else:
            first_half = list_[: index]
            second_half = list_[index + 1:]
    else:
        return list_[:-1]

    return first_half + second_half


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
