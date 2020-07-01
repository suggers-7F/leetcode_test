

def compare_majiang(x):
    if len(x) == 2:
       if x[0] == x[1]:
           return True
    if len(x) == 3:
        if x[0] == x[1] == x[2]:
            return True
        if x[0]+2 == x[1]+1 == x[2]:
            return True
    return False


def data_list(list_s):
    if len(list_s) == 2:
        if compare_majiang(list_s):
            return True
        else:
            return False
    else:
        for x in range(0, len(list_s)):
            for y in range(x + 1, len(list_s)):
                for z in range(y + 1, len(list_s)):
                    if compare_majiang([list_s[x], list_s[y], list_s[z]]):
                        #print([list_s[x], list_s[y], list_s[z]])
                        temp_list_s = list_s[:]
                        temp_list_s.remove(list_s[x])
                        temp_list_s.remove(list_s[y])
                        temp_list_s.remove(list_s[z])
                        #print(temp_list_s)
                        if data_list(temp_list_s):
                            return True
                        else:
                            continue
        return False

def get_data_majiang(s):
    true_len = [2,5,8,11,14]
    if len(s) in true_len:
        list_s =[]
        for  i in s:
            list_s.append(int(i))
        #print(list_s)
        return data_list(list_s)
    else:
        return False
if __name__ == '__main__':
    s = "11223344567"

    if get_data_majiang(s):
        print("yes")
    else:
        print("no")


