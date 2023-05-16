import pyperclip

# Get the clipboard text
text = pyperclip.paste()

# Convert the clipboard text to plain text
plain_text = text.replace('\r\n', '\n').replace('\t', ' ')

# Copy the plain text back to the clipboard
pyperclip.copy(plain_text)
