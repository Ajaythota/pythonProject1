filenames=["report.txt","journal.txt","presentation.txt"]
contents=["Daily new reports are here","journals are in the library"," presentations are on my pc"]
for filename,content in zip(filenames,contents): # zip is 1:1 corresponding mapping for 2 list items
    file=open(f"files/{filename}",'w')
    file.write(content)