def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for b in blocks:
        stripped_blocks.append(b.strip())
    while "" in stripped_blocks:
        stripped_blocks.remove("")

    return stripped_blocks