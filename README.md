
# DictGen :: A Python script that generates dictionaries (based on word frequency) from files. 

This small script is particularly useful for generating dictionaries for text editors such as vim.

It takes an arbitrary number of arguments and produced a dict by listing the n most frequent words. (there is a default number)

Output can contain frequency count. (disabled by default)

It can be modified to list only words of length between a certain range and so on. (there is a default)

Also, output can be modified to be upper, lower or mixed case.

Additionally if requests, bs4 and nltk are installed it will take URLs as an argument and generate dicts based on that.

The integration with nltk allows to filter words deemed stopwords by nltk.

```text
usage: dict-generator [-h] [-o [OUTPUT]] [-f] [-l [LENGTH]] [-n [NUMBER]]
                      [-p [{lower,upper,alnum,upperlower}]] [-m [MAXIMUM]]
                      [-s]
                      sources [sources ...]

Generate a dictionary from a file (and other tool).

positional arguments:
  sources

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        The [OUTPUT FILE] where the DICT should be written
  -f, --frequency       Add [FREQUENCY] count to entries
  -l [LENGTH], --length [LENGTH]
                        specify the minimul [LENGTH] of entries
  -n [NUMBER], --number [NUMBER]
                        specify the [NUMBER] of entries
  -p [{lower,upper,alnum,upperlower}], --pattern [{lower,upper,alnum,upperlower}]
                        specify the [CASE] of entries
  -m [MAXIMUM], --maximum [MAXIMUM]
                        specify the [MAXIMUM] for all entries
  -s, --stopWordsFilter
                        don't show entries classed as common by NLTK.
```

Because I don't hava a lot of data, my strategy was to find all the files (starting from the CWD) from a specific filetypes using the silver searcher (ag).

> depends on ag [can be replaced with grep and regexp]
> the args needed:
> 1 : the file type [java,vim,markdown ... ]
> 2 : output location

```sh
generate-dictionary(){
	dict-generator -n 2000 -l 4 -m 12 -p upper $(ag  -g "" --$1 / 2>/dev/null | xargs) >> $2
	dict-generator -n 2000 -l 4 -m 12 -p lower $(ag  -g "" --$1 / 2>/dev/null | xargs) >> $2
}
```

This makes a dictionary with a maximum of 4000k words (2000 upper and 2000 lower) from all files of a given type and outputs that in a specified file.

