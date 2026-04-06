# Primers • Shell Scripting

**Source:** https://aman.ai/primers/bash/
**Ingested:** 2026-04-02
**Re-scraped:** 2026-04-05
**Tags:** ml-fundamentals

---

* [Introduction](#introduction)
* [Arrays](#arrays)
  + [Loop over an array’s elements](#loop-over-an-arrays-elements)
  + [Loop over an array’s indices](#loop-over-an-arrays-indices)
* [How to get the list of files in a directory in a shell script?](#how-to-get-the-list-of-files-in-a-directory-in-a-shell-script)
  + [Resources](#resources)
* [References](#references)
* [Citation](#citation)

## Introduction

## Arrays

```
NUMS=`seq 1 10` # or seq 1 1 10

for NUM in "${NUMS[@]}"; do
    echo "Current number: $NUM"
done
```

### Loop over an array’s elements

```
FILES=("2011-09-04 21.43.02.jpg"
"2011-09-05 10.23.14.jpg"
"2011-09-09 12.31.16.jpg"
"2011-09-11 08.43.12.jpg")

for FILE in "${FILES[@]}"; do
    echo "$FILE"
done
```

### Loop over an array’s indices

```
FILES=("2011-09-04 21.43.02.jpg"
"2011-09-05 10.23.14.jpg"
"2011-09-09 12.31.16.jpg"
"2011-09-11 08.43.12.jpg")

for ((i = 0; i < ${#FILES[@]}; i++)); do
    echo "${FILES[$i]}"
done

#Any of these declarations of $FILES should work:
#
#FILES=(2011-09-04\ 21.43.02.jpg
#2011-09-05\ 10.23.14.jpg
#2011-09-09\ 12.31.16.jpg
#2011-09-11\ 08.43.12.jpg)
#
#or
#
#FILES=("2011-09-04 21.43.02.jpg"
#"2011-09-05 10.23.14.jpg"
#"2011-09-09 12.31.16.jpg"
#"2011-09-11 08.43.12.jpg")
#
#or
#
#FILES[0]="2011-09-04 21.43.02.jpg"
#FILES[1]="2011-09-05 10.23.14.jpg"
#FILES[2]="2011-09-09 12.31.16.jpg"
#FILES[3]="2011-09-11 08.43.12.jpg"
```

* Note that this method of iterating over an array is not recommended owing to differences in how different shells handle array indexes. Arrays in Bash are indexed from 9, while in zsh they’re indexed from 1 (unless [option KSH\_ARRAYS](http://zsh.sourceforge.net/Doc/Release/Options.html#Shell-Emulation) is set).

## How to get the list of files in a directory in a shell script?

```
search_dir=/the/path/to/base/dir/
for entry in "$search_dir"/*
do
  echo "$entry"
done
```

* Note that we need to place `/*` outside of quotes (i.e., “$search\_dir/\*” doesn’t work) because you need to let the shell glob the wildcard.
* To loop through the current directory:

```
for entry in *
do
  echo "$entry"
done
```

* Simpler syntax:

```
yourfilenames=`ls ./*.txt`
for eachfile in $yourfilenames
do
   echo $eachfile
done
```

* `./` is the current working directory but could be replaced with any path; `*.txt` returns anything.txt
* You can check what will be listed easily by typing the ls command straight into the terminal.
* Basically, you create a variable `yourfilenames` containing everything the list command returns as a separate element, and then you loop through it. The loop creates a temporary variable `eachfile` that contains a single element of the variable it’s looping through, in this case a filename. This isn’t necessarily better than the other answers, but it is intuitive because people are already familiar with the `ls` command and the for loop syntax.

### Resources

## References

* [How to get the list of files in a directory in a shell script?](https://stackoverflow.com/questions/2437452/how-to-get-the-list-of-files-in-a-directory-in-a-shell-script)
* [Behavior of Arrays in bash scripting and zsh shell (Start Index 0 or 1?)](https://stackoverflow.com/questions/50427449/behavior-of-arrays-in-bash-scripting-and-zsh-shell-start-index-0-or-1)

## Citation

If you found our work useful, please cite it as:

```
@article{Chadha2020ShellScripting,
  title   = {Shell Scripting},
  author  = {Chadha, Aman},
  journal = {Distilled AI},
  year    = {2020},
  note    = {\url{https://aman.ai}}
}
```
