# -*- coding: utf-8 -*
import hashlib
import mimetypes
import time

import pyperclip as pyperclip
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types
from PIL import Image, ImageGrab

note_name = "算法第四版Course课程"
auth_token = ""


def build_file(path):
    filedata = open(path, 'rb').read()
    md5 = hashlib.md5()
    md5.update(filedata)
    hashHex = md5.hexdigest()

    data = Types.Data()
    data.size = len(filedata)
    data.bodyHash = hashHex
    data.body = filedata
    resource = Types.Resource()
    resource.mime = mimetypes.guess_type(path)[0]
    resource.data = data
    res = {"resource": resource, "hashHex": hashHex}
    return res


# 获取电脑剪切板内容
def get_text_data():
    text_data = {}
    data = pyperclip.paste()
    # data =re.sub(r"[\r\n]", "\n", str(data))
    if len(data) == 0:
        return None
    data_list = data.splitlines()
    line_data = ""
    for x in data_list:
        line_data = line_data + ("<div>%s</div>" % x)
    print(line_data)
    dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    copy_data = '''
    <div>%s</div>
    %s
    <div><br/></div>
    ''' % (dateTime, line_data)
    # dateTime + "\n" + data + "\n\n"
    print(data)
    text_data['text'] = copy_data
    return text_data


# 获取电脑剪切板图片
def get_image_data():
    image_data = {}
    image_path = "screen.png"
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        print("Image: size : %s, mode: %s" % (image.size, image.mode))
        image.save(image_path)
        file_info = build_file(image_path)
        image_data['file_info'] = file_info
        image_data['text'] = '<en-media type="' + file_info["resource"].mime + '" hash="' + file_info["hashHex"] + '"/>'
        return image_data
    else:
        print("没有截图")
        return None


def makeNote(authToken, noteStore, noteTitle, parentNotebook=None):
    nBody = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
    nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
    nBody += "<en-note></en-note>"

    ## Create note object
    ourNote = Types.Note()
    ourNote.title = noteTitle
    ourNote.content = nBody

    ## parentNotebook is optional; if omitted, default notebook is used
    if parentNotebook and hasattr(parentNotebook, 'guid'):
        ourNote.notebookGuid = parentNotebook.guid
    noteStore.createNote(authToken, ourNote)


def remote_search(auth_token, note_store, search_string):
    my_filter = NoteStore.NoteFilter()
    my_filter.words = search_string
    my_filter.ascending = False

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
    spec.includeTagGuids = True
    return note_store.findNotesMetadata(auth_token, my_filter, 0, 10, spec)


copy_data = get_text_data()
if not copy_data or len(copy_data) == 0:
    copy_data = get_image_data()
if not copy_data:
    exit()
# create note_store
client = EvernoteClient(token=auth_token, sandbox=False, china=True)
user_store = client.get_user_store()
user = user_store.getUser()
print(user.username)

note_store = client.get_note_store()
# search for the note
note_list = remote_search(auth_token, note_store, "intitle:" + note_name)
# 如果没有创建一条
if note_list.totalNotes == 0:
    print("新建笔记: %s" % note_name)
    makeNote(auth_token, note_store, note_name)
    print("新建笔记 ok")
    note_list = remote_search(auth_token, note_store, "intitle:" + note_name)

# add tag to notes found
for note in note_list.notes:
    print("Before: %s" % (note.guid))
    # 获取内容
    note_data = note_store.getNote(auth_token, note.guid, True, False, False, False)
    # note_data.content = note_data.content + copy_data
    content = note_data.content
    content = content.replace("</en-note>", "")
    content = content + copy_data['text'] + "</en-note>"
    print(content)
    note_data.content = content
    if "file_info" in copy_data:
        file_info = copy_data['file_info']
        note_data.resources = [file_info["resource"]]
    res = note_store.updateNote(auth_token, note_data)
    print("updateNote ok")
