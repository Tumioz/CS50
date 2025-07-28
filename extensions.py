file_name= input("File Name: ").lower().split(".")[-1]
file_type= {"gif":"GIF",
"jpg":"image/jpeg",
"jpeg":"image/jpeg",
"png":"image/png",
"pdf":"application/pdf",
"txt":"text/plain",
"zip":"application/zip"}

if file_name in file_type:
    print(file_type[file_name])
else:
    print("application/octet-stream")
