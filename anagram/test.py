"""Tests for anagram finder."""

# pylint: disable=missing-docstring

import io
import random
import unittest

import anagram


class TestAnagramFinder(unittest.TestCase):

    def setUp(self):
        words = ['test',
                 'elvis', 'lives',
                 'evil', 'veil', 'vile',
                 'spot',
                 'coed', 'deco']
        random.shuffle(words)
        text = '\n'.join(words + [''])
        file = io.StringIO(text)
        self._anagram_finder = anagram.AnagramFinder(file)

    def test_getitem(self):
        anagrams = {'test': [],  # Present word with 0 anagrams
                    'elvis': ['lives'],  # Present word with 1 anagram
                    'evil': ['veil', 'vile'],  # Present word with >1 anagrams
                    'fun': [],  # Missing word with 0 anagrams
                    'post': ['spot'],  # Missing word with 1 anagram
                    'code': ['coed', 'deco']}  # Missing word with >1 anagrams
        for word, expected_anagrams in anagrams.items():
            actual_anagrams = self._anagram_finder[word]
            self.assertEqual(set(expected_anagrams), set(actual_anagrams))

if __name__ == '__main__':
    unittest.main()
