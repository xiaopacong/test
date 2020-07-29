text = input("请输入今天的心情:")
with open("日记.txt","a",encoding="utf-8") as f:
    f.write(text)   