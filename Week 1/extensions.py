h=input("File name :").strip().lower()

if h.endswith("gif"):
    print("image/gif")
elif h.endswith("jpg")|h.endswith("jpeg"):
    print("image/jpeg")
elif h.endswith("png"):
    print("image/png")
elif h.endswith("pdf"):
    print("application/pdf")
elif h.endswith("txt"):
    print("text/plain")
elif h.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")