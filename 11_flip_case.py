def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    new = ""
    for letter in phrase:
        if letter == to_swap.upper():
            new += letter.lower()
        elif letter == to_swap.lower():
            new += letter.upper()
        else:
            new += letter
    return new