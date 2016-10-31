"""List anagrams."""

import argparse
import collections
import sys

PROGRAM = 'anagram'


class ArgumentParser(argparse.ArgumentParser):
    """Parse command-line arguments."""

    def __init__(self):
        """Initialize parser with arguments."""
        epilog = 'Nothing is listed if no anagram is found.'
        super().__init__(prog=PROGRAM, description=__doc__, epilog=epilog)
        self._add_arguments()

    def _add_arguments(self):
        """Add arguments to parser."""
        self.add_argument('word', help='Word, e.g. "empires"')
        self.add_argument('file', nargs='?', default='words.txt',
                          type=argparse.FileType(),
                          help='Words file (default: "%(default)s")')

    def parse_args(self, args=None, namespace=None):
        """Parse and validate args.

        In case of a validation error, print the error and exit.
        """
        namespace = super().parse_args(args, namespace)
        if len(namespace.word) == 0:
            self.error('Word must not be empty.')
        return namespace


class AnagramFinder:  # pylint: disable=too-few-public-methods
    """Find anagrams.

    The anagram finder has a one-time initialization cost of finding and
    caching the anagrams of all words.  As such, it is optimized for fast
    successive lookups of anagrams of individual words.
    """

    def __init__(self, file):
        """Map anagrams for words in the given file.

        The file must contain a list of unique lowercase words, one per line.
        """
        with file:
            self._anagrams = self._map_anagrams(file)

    def __getitem__(self, word):
        """Return a list of anagrams for the given word."""
        wordgram = self._wordgram(word)
        anagrams = self._anagrams.get(wordgram, [])
        anagrams = [anagram for anagram in anagrams if word != anagram]
        return anagrams

    def _map_anagrams(self, file):
        """Return a mapping of wordgrams to a tuple of their anagrams."""
        anagrams = collections.defaultdict(list)
        for word in file:
            word = word.rstrip()
            wordgram = self._wordgram(word)
            anagrams[wordgram].append(word)
        anagrams.default_factory = None  # Prevents setitem upon getitem.
        return anagrams

    @staticmethod
    def _wordgram(word):
        """Return the given word with its letters sorted."""
        return ''.join(sorted(word))


def main():
    """Parse arguments and run program."""
    try:
        namespace = ArgumentParser().parse_args()
        anagram_finder = AnagramFinder(namespace.file)
        for anagram in anagram_finder[namespace.word]:
            print(anagram)
    except (Exception,  # pylint: disable=broad-except
            KeyboardInterrupt) as exc:
        sys.exit(exc)

if __name__ == '__main__':
    main()
