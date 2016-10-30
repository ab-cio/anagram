# anagram
Anagram finder

## Requirements
* Python ≥3.5. There are no package dependencies.
* File containing list of words, one on each line.

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

	$ /usr/bin/time -v python3.5 anagram empires
	premise
		Command being timed: "python3.5 anagram empires"
		User time (seconds): 0.03
		System time (seconds): 0.00
		Percent of CPU this job got: 94%
		Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.03
		Average shared text size (kbytes): 0
		Average unshared data size (kbytes): 0
		Average stack size (kbytes): 0
		Average total size (kbytes): 0
		Maximum resident set size (kbytes): 7704
		Average resident set size (kbytes): 0
		Major (requiring I/O) page faults: 0
		Minor (reclaiming a frame) page faults: 2129
		Voluntary context switches: 1
		Involuntary context switches: 3
		Swaps: 0
		File system inputs: 0
		File system outputs: 0
		Socket messages sent: 0
		Socket messages received: 0
		Signals delivered: 0
		Page size (bytes): 4096
		Exit status: 0
