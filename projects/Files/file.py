file_contents=open("Files/out.log",'w')
file_contents.write("Artificial intelligence is best")
file_contents.close()


add_content=open("Files/out.log",'a')
add_content.write("\n Cloud computing")
add_content.write("\n E-commerce")
add_content.close()

add_content=open("Files/out.log")
print(add_content.read())


