# anagram
Anagram finder

## Contents
- [Requirements](#requirements)
- [Design]
- [Usage](#usage)
    - [Clone](#clone)
    - [Help](#help)
    - [Example](#example)
- [Performance](#performance)

## Requirements
* Python ≥3.5. There are no package dependencies.
* File containing a list of unique lowercase words, one per line.

## Design
The `AnagramFinder` class has a one-time initialization cost of finding and
caching the anagrams of all words.  As such, the class is optimized for fast
lookups of anagrams of _multiple_ individual words.

## Usage

### Clone
    $ git clone https://github.com/ab-cio/anagram.git
    $ cd ./anagram/

### Help
	$ python3.5 anagram -h
	usage: anagram [-h] word [file]
	
	List anagrams.
	
	positional arguments:
	  word        Word, e.g. "empires"
	  file        Words file (default: "words.txt")
	
	optional arguments:
	  -h, --help  show this help message and exit
	
	Nothing is listed if no anagram is found.
	
### Example
	$ python3.5 anagram empires ./words.txt
	premise
	emprise
	imprese
	spireme
	epimers

## Performance

	$ wc ./words.txt 
	 413988  413988 4381051 ./words.txt
	
	$ /usr/bin/time -v python3.5 anagram empires ./words.txt
	premise
	emprise
	imprese
	spireme
	epimers
		Command being timed: "python3.5 anagram empires"
		User time (seconds): 1.73
		System time (seconds): 0.08
		Percent of CPU this job got: 99%
		Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.82
		Average shared text size (kbytes): 0
		Average unshared data size (kbytes): 0
		Average stack size (kbytes): 0
		Average total size (kbytes): 0
		Maximum resident set size (kbytes): 129552
		Average resident set size (kbytes): 0
		Major (requiring I/O) page faults: 0
		Minor (reclaiming a frame) page faults: 38031
		Voluntary context switches: 1
		Involuntary context switches: 31
		Swaps: 0
		File system inputs: 0
		File system outputs: 0
		Socket messages sent: 0
		Socket messages received: 0
		Signals delivered: 0
		Page size (bytes): 4096
		Exit status: 0
