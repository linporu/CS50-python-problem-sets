def main():
    mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
    }

    file_name = input("File name: ").lower().strip()
    for ext in mime_types:
        if file_name.endswith(ext):
            print(mime_types[ext])
            break
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
