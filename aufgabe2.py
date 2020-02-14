print("wie alt bist du: ")
name = int(input())
if name < 2:
    print("du bist ein baby")
elif name < 5:
    print("du bist ein kleinkind")
elif name < 12:
    print("du bist ein kind")
elif name < 18:
    print("du bist ein teenager")
else:print("du bist erwachsen")