#1
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
fruits = ["orange","apple","manga"]
print_list(fruits)
