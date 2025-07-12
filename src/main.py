from textnode import TextNode, TextType

def main():
    tn = TextNode("This is some test text", TextType.LINK, "https://www.boot.dev")
    print(tn)

main()