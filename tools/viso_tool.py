# -*- coding: utf-8 -*
import types
import win32com.client as win32
from win32com.client import constants


appVisio = win32.gencache.EnsureDispatch("Visio.Application")

vdoc = appVisio.Documents.Open(
    r"C:\Users\montnets\Desktop\chatbot试验 - 副本 (2).vsdx")

print("\n\n************* visio 所有节点信息 ***************************")
types = ["#模板#", "#按钮#", "#图文#"]
shps = vdoc.Pages(1).Shapes
shape_list = []
for shp in shps:
    shape_list.append(shp)
    if shp.Shapes.Count > 0:
        for s in shp.Shapes:
            shape_list.append(s)


for shp in shape_list:
    title = None
    shape_id = shp.ID
    if shp.Text == "哈哈":
        print(shp.Text)
    try:
        title = shp.Title
    except:
        pass
    if title and title in types:
        print(" 类型：" + shp.Title + "           节点ID：" + str(shape_id) +
              "           文字：" + shp.Text.replace("\\<.*?\\>|\r\n", ""))
    # f = open('C:\\Users\\montnets\\Downloads\\myExportedPage6.bmp', 'wb')
    # b = shp.ForeignData.tobytes()
    # f.write(bytearray(b))
    # f.close()
    # shp.Export ("C:\\Users\\montnets\\Downloads\\myExportedPage2.bmp")


print("\n\n************* visio 所有绑定关系信息 ***************************")

connects = vdoc.Pages(1).Connects
for conn in connects:
    from_shp = conn.FromSheet
    info = ''  # from_shp.Name
    if conn.FromPart == constants.visBegin:
        info += ('起点')
    elif conn.FromPart == constants.visEnd:
        info += ('终点')  # visBegin ==9 ,visEnd == 12
    to_shp = conn.ToSheet
    info += '--> ' + (to_shp.Text) + 'id=' + str(to_shp.ID)  # 连接的矩形名称
    print(info)
