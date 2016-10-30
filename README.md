# anagram
Anagram finder

## Requirements
Python ≥3.5 is required. There are no package dependencies.

## Usage

### Clone
    $ git clone https://github.com/ab-cio/anagram.git
    $ cd ./anagram/

### Help
	$ python3.5 anagram -h
	usage: anagram [-h] word [file]
	
	Find anagrams.
	
	positional arguments:
	  word        Word, e.g. "empires"
	  file        Words file (default: "words.txt")
	
	optional arguments:
	  -h, --help  show this help message and exit

### Example
    $ python3.5 anagram empires ./words.txt
    premise

## Performance

	$ time python3.5 anagram empires
	premise
	
	real	0m0.129s
	user	0m0.110s
	sys	0m0.009s
