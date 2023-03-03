import os
import re

# 指定 Java 项目根目录
project_dir = 'C:/Users/47895/workspace/empPF_trunk_rms'
# 匹配双引号
match_double_quotes = re.compile(r'"(.*?)"')

# 遍历 Java 项目目录及其子目录中的所有文件
def delete_line(filepath):
    with open(filepath, 'r', encoding="UTF-8") as f:
        lines = f.readlines()
     # 查找并删除依赖行
    with open(filepath, 'w', encoding="UTF-8") as f:
        for line in lines:
            if 'ApiModel' in line or 'ApiModelProperty' in line :
                matches = match_double_quotes.findall(line)
                if(len(matches) > 0):
                    new_line ='    /**\n    * ' +  matches[0] + '\n    */\n'
                    if('ApiModelProperty' not in line ):
                        new_line ='/**\n* ' +  matches[0] + '\n*/\n'
                    f.write(new_line)
            else:
                f.write(line)
                

# delete_line("C:/Users/47895/workspace/empPF_trunk_rms/commons/src/main/java/com/montnets/emp/common/entity/ACmdque.java")



for root, dirs, files in os.walk(project_dir):
    for filename in files:
        # 只处理扩展名为 .gradle 或 .xml 的文件
        if filename.endswith('.java'):
            # 读取文件内容
            filepath = os.path.join(root, filename)
            delete_line(filepath)
