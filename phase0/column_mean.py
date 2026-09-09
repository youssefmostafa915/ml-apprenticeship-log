def column_mean(filepath, column_name):
    f = open(filepath)
    header = f.readline().strip().split(",")
    col_index = header.index(column_name)

    total = 0
    count = 0
    for line in f:
        row = line.strip().split(",")
        value = float(row[col_index])
        total = total + value
        count = count + 1

    f.close()
    return total / count


if __name__ == "__main__":
    print(column_mean("data.csv", "age"))
