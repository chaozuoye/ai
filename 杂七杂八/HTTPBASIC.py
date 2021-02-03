def read_content(filename):
    linelist=[]
    with open(filename) as f:
        linelist = f.readlines()
    return linelist

def concat_user_pass(user_file,pass_file):
    result_list = []
    user_list =read_content(user_file)
    pass_list = read_content(pass_file)
    for user_line in user_list:
        for pass_line in pass_list:
            result_list.append(user_line.strip()+":"+pass_line)
    return result_list
def write_result(result_file):
    user_file="user.txt"
    pass_file ="pass.txt"
    with open(result_file,"a") as f:
        result_list =concat_user_pass(user_file,pass_file)
        for line in result_list:
            f.write(line)

def main():
    write_result("result.txt")
main()
