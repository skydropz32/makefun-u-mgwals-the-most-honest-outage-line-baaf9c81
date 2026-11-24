"""The Most Honest Outage Line: one honest status page line for a total outage."""

LINE = "All services are down. I can't reach any server to check what broke, so I don't know the cause yet, and I won't invent an ETA. This page is still up."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-160 characters,
    # not only white space.
    if not (1 <= len(LINE) <= 160):
        raise ValueError("entry must be 1-160 characters")
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
