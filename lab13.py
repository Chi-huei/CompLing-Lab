def process_input(text):
    return text[0], text[-1]

def main():
    text = input("Enter a sentence: ")
    print(process_input(text))


if __name__ == "__main__":
    main()
