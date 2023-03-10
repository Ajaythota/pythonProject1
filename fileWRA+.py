# ``r+''  Open for reading and writing.  The stream is positioned at the beginning of the file
file1=open("files/fileR+",'r+')
file1.write("this is r+")

#``w+''  Open for reading and writing.  The file is created if it does not
   #      exist, otherwise it is truncated.  The stream is positioned at
      #   the beginning of the file

file2=open("files/fileW+",'w+')
file2.write("this is w+")

#`a+''  Open for reading and writing.The stream is positioned at the end of the file

file3=open("files/fileA+",'a+')
file3.write("thi is a+")
file3.seek(0)
print(file3.read())
