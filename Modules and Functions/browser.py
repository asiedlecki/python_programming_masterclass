import webbrowser

# webbrowser.open("https://www.python.org/", new=2)

# help(webbrowser)

# for i in range(10):
#     print(*range(i), sep=';', end=' ')

firefox = webbrowser.get(using='firefox')
firefox.open_new_tab("https://python.org/")