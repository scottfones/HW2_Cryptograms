# CISC 320: Programming Project 2 - Cryptograms

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage

### Cryptogram Solver

`python cryptoback.py WORDLIST`

### Solver Examples

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

### Testing Program

`python crypto_tester.py -n 5 -w 9`

The testing program creates a random cipher for each round. It then selects random words from the dictionary and encodes them. Finally, it runs the solver and looks for the decoded words in the output.

### Testing Example

```bash
Testing Rounds: 5, Words Per Round: 9

Encrypted: dv vgs rturm fir urlprmduymr pmqhizr d urlprmduymr ks
Decrypted: as sky enter lie temperature provide a temperature by
Result: Success

Encrypted: akvczs luc g nsrbsyvnoys lbsyvns v g svhs rsvhoys
Decrypted: change own i temperature operate a i ease measure
Result: Success

Encrypted: jmlsmhfjyhm jmlsmhfjyhm vmj cbnwrjrbn vrem fj hmshmumnj f ubn
Decrypted: temperature temperature let condition like at represent a son
Result: Success

Encrypted: u ceonjzz ejkjklje hjej lejmq csmug wmssjx ot pooqnhfnv
Decrypted: i process remember here bread plain valley of woodchuck
Result: Success

Encrypted: xeni yhbxc vhbzctz leazcn zcuvchozphc zcuvchozphc tovzoen hcmpehc ylbk
Decrypted: kind broke protect listen temperature temperature captain require blow
Result: Success
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
