import os


def merge_tsv_files(directory, output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir(directory):
            if filename.endswith(".tsv"):
                filepath = os.path.join(directory, filename)
                with open(filepath, "r") as infile:
                    lines = infile.readlines()
                    outfile.writelines(lines[1:])  # 从第二行开始写入到输出文件


def list_all_file(directory, output_file):
    with open(output_file, "w") as outfile:
        for filename in os.listdir(directory):
            outfile.writelines(filename + "\n")  # 写入到输出文件

def remove_file(directory, output_file):
    with open(output_file, "r") as outfile:
        lines = outfile.readlines()
        for line in len(lines):
            one_path = lines[line].split('\t')[len(lines)-1] #这里要注意位置
            one_path = os.path.join(directory,lines[0])



# 指定目录和输出文件路径
directory = rf"\\10.30.9.254\Share\Frank\re-convert"
output_file = rf"\\10.30.9.254\Share\Frank\re-convert\allboot.tsv"

# 调用函数进行合并
merge_tsv_files(directory, output_file)
#list_all_file(directory, output_file)
