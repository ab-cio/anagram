# anagram
Anagram finder

## Contents
- [Requirements](#requirements)
- [Design](#design)
- [Clone](#clone)
- [Test](#test)
- [Shell usage](#shell-usage)
    - [Help](#help)
    - [Example](#example)
- [Module usage](#module-usage)
- [Shell performance](#shell-performance)

## Requirements
* Python ≥3.5. There are no package dependencies.
* File containing a list of unique lowercase words, one per line.

## Design
* The anagram finder is designed with a one-time initialization cost of finding
  and caching the anagrams of all words.  As such, it is optimized for fast
  successive lookups of anagrams of individual words.
* The sort order of the word list is preserved in the returned anagrams. Using
  a sorted word list will ensure that the returned anagrams are also sorted.
* Several complementary static analysis tools were used to control code
  quality. These were `pycodestyle` (formerly `pep8`), `pydocstyle`, `pylint`,
  `mccabe`, `symilar` and `vulture`.

## Clone
```
$ git clone https://github.com/impredicative/anagram.git
$ cd ./anagram/
```

## Test
```
$ python3.5 -m anagram.test -q
```

## Shell usage

### Help
```
$ python3.5 -m anagram -h
usage: anagram [-h] word [file]

List anagrams.

positional arguments:
  word        Word, e.g. "empires"
  file        Words file (default: "words.txt")

optional arguments:
  -h, --help  show this help message and exit

Nothing is listed if no anagram is found.
```
	
### Example
```
$ python3.5 -m anagram empires ./words.txt
premise
emprise
imprese
spireme
epimers
```

## Module usage
```python
>>> import anagram
>>> words_file = open('words.txt')
>>> anagram_finder = anagram.AnagramFinder(words_file)  # Slow.
>>> anagram_finder['empires']                           # Fast.
['premise', 'emprise', 'imprese', 'spireme', 'epimers']
>>> anagram_finder['code']                              # Fast.
['deco', 'coed', 'ecod']
```

## Shell performance
```
$ wc ./words.txt 
 413988  413988 4381051 ./words.txt

$ /usr/bin/time -v python3.5 -m anagram empires ./words.txt
premise
emprise
imprese
spireme
epimers
	Command being timed: "python3.5 -m anagram empires ./words.txt"
	User time (seconds): 1.79
	System time (seconds): 0.07
	Percent of CPU this job got: 99%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.88
	Average shared text size (kbytes): 0
	Average unshared data size (kbytes): 0
	Average stack size (kbytes): 0
	Average total size (kbytes): 0
	Maximum resident set size (kbytes): 129584
	Average resident set size (kbytes): 0
	Major (requiring I/O) page faults: 0
	Minor (reclaiming a frame) page faults: 38066
	Voluntary context switches: 1
	Involuntary context switches: 51
	Swaps: 0
	File system inputs: 0
	File system outputs: 0
	Socket messages sent: 0
	Socket messages received: 0
	Signals delivered: 0
	Page size (bytes): 4096
	Exit status: 0
```
