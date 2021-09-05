"""Little Sister's Vocabulary exercise.

https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""


def add_prefix_un(word: str) -> str:
    """Converts a word to its 'un' equivalent

    Example: 'happy' becomes 'unhappy'

    Args:
        word (str): The word to prefix with 'un'

    Returns:
        str: The word prefixed with 'un'
    """

    return "un" + word


def make_word_groups(vocab_words: list[str]) -> str:
    """Adds a prefix of to a list of words

    The first word in the list must be the prefix to add to the other words in
    the list.

    Args:
        vocab_words (list): List of words to add the prefix to

    Returns:
        str: A string of words with the `prefix` added to each
    """

    prefix = vocab_words[0]
    return f" :: {prefix}".join(vocab_words)


def remove_suffix_ness(word: str) -> str:
    """Takes a word and returns it with 'ness' removed

    Words that end with an 'i' after having 'ness' removed should have the 'i'
    replaced with 'y'; e.g., 'happiness' -> 'happy'

    Args:
        word (str): The word to remove 'ness' from

    Returns:
        str: The word with 'ness' removed
    """

    word_with_ness_removed = word[0:-4]
    last_letter = word_with_ness_removed[-1]

    if last_letter == "i":
        word_with_ness_removed = word_with_ness_removed[:-1] + "y"

    return word_with_ness_removed


def noun_to_verb(sentence: str, index: int) -> str:
    """Verbify (convert adjective to verb) a selected word in a sentence

    Select a word from a sentence and 'verbify' it; that is, convert adjective
    to a verb. E.g. if the selected word is 'bright' then convert to 'brighten'
    by adding the 'en' suffix. All words will be regular spelling and will not
    need spelling changes to accommodate the suffix. All sentences will have a
    period on the end.

    Args:
        sentence (str): A string of words with a period on the end.
        index (int): The index of the word in list once sentence is split apart

    Returns:
        str: The selected and verbified word
    """

    # Remove the period from the end of the sentence before splitting into a
    # list of words, then selecting a word using the index argument
    words = sentence[:-1].split()
    selected_word = words[index]

    return selected_word + "en"
