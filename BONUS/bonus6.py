contents = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaa", "bbbbbbbbbbbbbbbbbbbbbbbbbbbb bbbbb", "cccccccccccccccccccc cccc"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
     file = open(f"../files/{filename}",'w')
     file.write(content)