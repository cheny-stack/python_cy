import os
from bs4 import BeautifulSoup

import xml.etree.ElementTree as ET

def read_epub_content_opf(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Define the namespace
    namespace = {"ns": "http://www.idpf.org/2007/opf"}

    # Read the title
    title_element = root.find("ns:metadata/ns:title", namespace)
    title = title_element.text if title_element is not None else ""

    # Read the HTML file names
    html_files = []
    item_elements = root.findall("ns:manifest/ns:item", namespace)
    for item_element in item_elements:
        item_id = item_element.get("id")
        item_href = item_element.get("href")
        item_media_type = item_element.get("media-type")
        
        # Filter HTML files
        if item_media_type == "application/xhtml+xml":
            html_files.append(item_href)

    return title, html_files

def rename_html_files(folder_path, html_files):
    index = 0
    for file in html_files:
        if file.endswith(".html"):
            file_path = os.path.join(folder_path, file)
            new_file_path = ''
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                soup = BeautifulSoup(content, "html.parser")
                h1_tags = soup.find_all("h1")
                h2_tags = soup.find_all("h2")

                # 获取h1标签内容
                h1_content = ""
                if h1_tags:
                    h1_content = h1_tags[0].text

                # 获取h2标签内容
                h2_content = ""
                if h2_tags:
                    h2_content = h2_tags[0].text
                index += 1
                if len(h1_content) == 0 and len(h2_content) == 0:
                    new_file_name = str(index)
                else:
                    new_file_name = str(index) + '-' + h1_content+ h2_content
                # 构建新文件名
                
                new_file_name =  f"{new_file_name}.html"
                new_file_path = os.path.join(folder_path, 'text',new_file_name)
                
            
            # 重命名文件
            if len(new_file_path) > 0:
                os.rename(file_path, new_file_path)
                print(f"Renamed {file} to {new_file_name}")

# 指定文件夹路径
root_path = "C:/Users/47895/Desktop/book/1/"
opf_file_path = root_path + "content.opf"
title, html_files = read_epub_content_opf(opf_file_path)
# Print the results
print("Title:", title)
print("HTML Files:")
for html_file in html_files:
    print(html_file)
# 调用函数进行文件夹遍历和重命名
rename_html_files(root_path, html_files)
