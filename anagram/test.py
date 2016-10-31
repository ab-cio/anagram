"""Tests for anagram finder."""

# pylint: disable=missing-docstring

import io
import os
import unittest

import anagram


class TestArgParser(unittest.TestCase):

    def setUp(self):
        self._argparser = anagram.ArgumentParser()

    def test_parse_args(self):
        word, filename = args = ('word', os.devnull)
        namespace = self._argparser.parse_args(args)
        self.assertEqual(word, namespace.word)
        nfile = namespace.file
        self.assertEqual(filename, nfile.name)
        self.assertTrue(nfile.readable())
        self.assertFalse(nfile.closed)
        nfile.close()


class TestAnagramFinder(unittest.TestCase):

    def setUp(self):
        words = ['test',
                 'elvis', 'lives',
                 'evil', 'veil', 'vile',
                 'spot',
                 'coed', 'deco']
        text = '\n'.join(words + [''])
        file = io.StringIO(text)
        self._anagram_finder = anagram.AnagramFinder(file)

    def test_getitem(self):
        anagrams = {'test': [],  # Present word with 0 anagrams
                    'elvis': ['lives'],  # Present word with 1 anagram
                    'veil': ['evil', 'vile'],  # Present word with >1 anagrams
                    'fun': [],  # Missing word with 0 anagrams
                    'post': ['spot'],  # Missing word with 1 anagram
                    'code': ['coed', 'deco']}  # Missing word with >1 anagrams
        for word, expected_anagrams in anagrams.items():
            actual_anagrams = self._anagram_finder[word]
            self.assertEqual(expected_anagrams, actual_anagrams)

if __name__ == '__main__':
    unittest.main()
