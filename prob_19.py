def split_and_join(line):
    return(line.replace(" ", "-"))
    # new_s = ""
    # for i in line:
    #     if (i == " "):
    #         new_s += "-"
    #     else:
    #         new_s += i
    # return(new_s) 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
