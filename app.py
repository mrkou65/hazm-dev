from hazm import *
normalizer = Normalizer()

lines = []

with open("datasets/chats.txt",encoding='utf-8') as file:
    while (line := file.readline().rstrip()):        
        normal=normalizer.normalize(line)
        lines.append(line)
        lines.append(normal)
        lines.append("----------")      


with open("chats-output.txt", "w",encoding="utf-8") as outfile:
    outfile.write("\n".join(lines))
