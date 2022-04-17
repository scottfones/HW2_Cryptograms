# CISC 320: Programming Project 2 - Cryptograms

## Usage

`python cryptoback.py WORDLIST`

### Example

```bash
$ python cryptoback.py gop pgo
4
are ear
eat tea
how who
own now
```

```bash
$ python cryptoback.py nooa noka
5
feet felt
good gold
meet meat
seed send
wood word
```

```bash
$ python cryptoback.py nttaemxeq etkkuey
3
woodchuck collect
woodchuck connect
woodchuck correct
```

```bash
$ python cryptoback.py jack u cuaes
7
bird a raise
duck a cause
girl a raise
grew a early
grew a earth
much a cause
rule a laugh
```

## Formal Problem Description

### Problem

Given a cryptogram (via StdIn), print all the possible decodings (via StdOut)

### Details of Output

- Print to StdOut
- First line should be the number of decodings
- Sort the output alphabetically

### Example Input

```bash
gop pgo
```

### Example Output

```bash
4
are ear
eat tea
how who
own now
```

## Submission

- Submit either a c, c++, Java or Python file
- You cannot just hardcode the answers as you don't know our test cases
- There is a dictionary.txt file that you must use; you should NOT upload it with your submission
