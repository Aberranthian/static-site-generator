from textnode import *

def main():
    test = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(repr(test))

if __name__ == "__main__":
    main()