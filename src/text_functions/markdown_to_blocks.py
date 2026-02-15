def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        if block is None or block == "":
            continue
        no_spaces = block.strip()
        if no_spaces == "":
            continue

        result.append(no_spaces)

    return result