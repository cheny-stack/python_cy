# -*- coding: utf-8 -*
import html
import time

import pyperclip as pyperclip
from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore

note_name = "my_note"
auth_token = ""
# 获取电脑剪切板内容
data = pyperclip.paste()
data = html.escape(data)
# data =re.sub(r"[\r\n]", "\n", str(data))
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


def remote_search(auth_token, note_store, search_string):
    my_filter = NoteStore.NoteFilter()
    my_filter.words = search_string
    my_filter.ascending = False

    spec = NoteStore.NotesMetadataResultSpec()
    spec.includeTitle = True
    spec.includeTagGuids = True
    return note_store.findNotesMetadata(auth_token, my_filter, 0, 10, spec)


# create note_store
client = EvernoteClient(token=auth_token, sandbox=False, china=True)
user_store = client.get_user_store()
user = user_store.getUser()
print(user.username)

note_store = client.get_note_store()
# search for the note
note_list = remote_search(auth_token, note_store, "intitle:" + note_name)

# add tag to notes found
for note in note_list.notes:
    print("Before: %s" % (note.guid))
    # 获取内容
    note_data = note_store.getNote(auth_token, note.guid, True, False, False, False)
    # note_data.content = note_data.content + copy_data
    content = note_data.content
    content = content.replace("</en-note>", "")
    content = content + copy_data + "</en-note>"
    print(content)
    note_data.content = content
    res = note_store.updateNote(auth_token, note_data)
    print("updateNote ok")
