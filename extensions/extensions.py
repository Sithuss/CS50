extend = input("Filename: ").lower()

if "." in extend:
    if "jpg" in extend:
        print("image/jpeg")
    elif "jpeg" in extend:
        print("image/jpeg")
    elif "png" in extend:
        print("image/png")
    elif "gif" in extend:
        print("image/gif")
    elif "pdf" in extend:
        print("application/pdf")
    elif "txt" in extend:
        print("text/plain")
    elif "zip" in extend:
        print("application/zip")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")

