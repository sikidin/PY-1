def delete(list_, index=None):
    if index is None: #проверяем существует ли индекс?
        list_.pop() #индекс не существует, значение по умолчанию -1
    else:
        list_.pop(index)
    return list_

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
