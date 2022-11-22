def lexical():
    list = []

    k1 = ["begin", "end", "var", "integer", "repeat", "until"]
    k2 = [">", "<", "=",  "+", ';', '.', ':', '*']
    k3 = ["<=", ">=", "<>", ":="]

    with open ("input.txt", "r") as file:
        for str in file:
            len_str = len(str)
            i = 0
            var = ""
            while i < len_str:
                if str[i] not in k2 and str[i] != " " and str[i] != "\n":
                    var += str[i]
                elif var != "":
                    if var in k1:
                        list.append([0, var])
                    elif not var[0].isdigit():
                        list.append([1, var])
                    elif var.isdigit():
                        list.append([2, var])
                    else:
                        print("Ошибка лексического анализа")
                        exit()
                    var = ""
                if i < len(str) - 1:
                    if str[i:i+2] in k3:
                        list.append([3, str[i:i+2]])
                        i += 1
                    elif str[i] in k2:
                        list.append([3, str[i]])
                elif str[i] in k2:
                    list.append([3, str[i]])
                i += 1


    for item in list:
        print("%s\n" % item)
    return list

lexical()
