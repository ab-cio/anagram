#!/usr/bin/env python3.5
"""List anagrams."""

import argparse
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
                          type=argparse.FileType('r'),
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
    """Find anagrams."""

    def __init__(self, file):
        """Find anagrams for words read using the given file handle.

        The file must contain one word per line and have no repeated words.
        """
        self._file = file

    @staticmethod
    def _wordgram(word):
        """Return the given word with its letters sorted."""
        return ''.join(sorted(tuple(word)))

    def find(self, word):
        """Return a list of anagrams for the given word."""
        wordgram = self._wordgram(word)
        anagrams = []
        for fileword in self._file:
            fileword = fileword.rstrip()
            if (word != fileword) and (wordgram == self._wordgram(fileword)):
                anagrams.append(fileword)
        return anagrams


def main():
    """Parse arguments and run program."""
    try:
        namespace = ArgumentParser().parse_args()
        for anagram in AnagramFinder(namespace.file).find(namespace.word):
            print(anagram)
    except (Exception,  # pylint: disable=broad-except
            KeyboardInterrupt) as exc:
        sys.exit(exc)

if __name__ == '__main__':
    main()
