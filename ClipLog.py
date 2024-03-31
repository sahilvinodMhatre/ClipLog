import pyperclip

LastText = None

while True:
    if pyperclip.paste() is not None:
            
            if pyperclip.paste() == LastText:
                 pass
            elif pyperclip.paste() is not LastText:
                with open("clipboardlog.txt", 'a') as file:
                    file.write(f"=========================================================================================\n\n{pyperclip.paste()}\n\n")
                    LastText = pyperclip.paste()
            