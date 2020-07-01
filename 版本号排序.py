
list_version = ["1.1.1.1","2.2.2.2","2.0.0.0","3.4.5.4","3.4.4.4"]




def compare_version(x,y):
    x_list=x.split(".")
    y_list=y.split(".")
    for i,j in zip(x_list,y_list):
        if i > j:
            return True
        elif i < j :
            return False
    return True

def compares_version(list_version):
    if len(list_version)>1:
        for i in range(0,len(list_version)):
            for j in range(i+1,len(list_version)):
                if compare_version(list_version[i],list_version[j]):
                    list_version[i],list_version[j] = list_version[j],list_version[i]
    return list_version

if __name__ == '__main__':
    list = compares_version(list_version)
    print(list)