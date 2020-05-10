# -*- coding: utf-8 -*
import hashlib
import mimetypes
import os
import time
from PIL import Image,ImageGrab

import pyperclip as pyperclip
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.type.ttypes as Types

# 获取电脑剪切板图片
image_path = "screen.png"
image = ImageGrab.grabclipboard()
if isinstance(image, Image.Image):
    print("Image: size : %s, mode: %s" % (image.size, image.mode))
    image.save(image_path)
else:
    print("没有截图")
    exit()


dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
copy_data = '''
<div><br/></div>
<div>%s</div>
''' % (dateTime)

hashHex=""

def remote_search(auth_token, note_store, search_string):
    my_filter = NoteStore.NoteFilter()
    my_filter.words = search_string
    my_filter.ascending = False

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
    spec.includeTagGuids = True
    return note_store.findNotesMetadata(auth_token, my_filter, 0, 10, spec)

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

# create note_store
auth_token = ""
client = EvernoteClient(token=auth_token, sandbox=False ,china=True)
user_store = client.get_user_store()
user = user_store.getUser()
print (user.username)

note_store =client.get_note_store()
# search for the note
note_list = remote_search(auth_token, note_store, "intitle:my_image_note")

# add tag to notes found
for note in note_list.notes:
    print("Before: %s" % (note.guid))
    # 获取内容
    note_data = note_store.getNote(auth_token, note.guid, True, False, False, False)
    # note_data.content = note_data.content + copy_data
    content = note_data.content
    content = content.replace("</en-note>", "")
    content += copy_data
    #添加资源
    file_info=build_file(image_path)
    content += '<en-media type="' + file_info["resource"].mime + '" hash="' + file_info["hashHex"] + '"/>'
    content += "</en-note>"
    print(content)
    note_data.content = content

    note_data.resources = [file_info["resource"]]
    res = note_store.updateNote(auth_token, note_data)
    print("updateNote ok")
