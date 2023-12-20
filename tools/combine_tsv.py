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


# 指定目录和输出文件路径
directory = rf"\\10.30.9.254\share\Frank\FBIQCal_Deal"
output_file = rf"\\10.30.9.254\share\Frank\FBIQCal_Deal\allNTboot.tsv"

# 调用函数进行合并
#merge_tsv_files(directory, output_file)
#list_all_file(directory, output_file)
