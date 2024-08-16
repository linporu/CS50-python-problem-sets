def main():
    output = convert(input())
    print(output)


def convert(face):
        output = face.replace(":)", "🙂")
        output = output.replace(":(", "🙁")
        return output


main()
