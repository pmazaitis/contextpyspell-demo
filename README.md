# contextpyspell-demo.py

A quick demo of a format-aware spellchecker for ConTeXt using tree-sitter-context_en

## Installation

Clone or download this repo (possibly in a pyenv environment).

Install the tree-sitter dependency (using pip in this example):

    pip3 install tree_sitter

Install the cyhunspell dependency (using pip in this example):

    pip3 install cyhunspell
    
On first run, the script should configure and compile the included tree-sitter distribution for demo use.

## Trying it Out

This demo takes a single argument: the input file to process.

This demo will display the computed syntax tree of the input file, followed by any misspelled words, and suggested corrections for those words.

As an example, running this:

    python contextpyspell-demo.py example_files/cow.tex
    
...should yield this:

    Concrete syntax tree for example_files/cow.tex
    (document (preamble) (main (text_block (text) (paragraph_mark))) (postamble (text_block (text))))

    Found mispelled word: Cuw. on line 2
    Possible corrections: ('Cu', 'Cu w', 'Cue', 'Cw', 'Caw', 'Cur', 'Cut', 'Cow', 'Cud', 'Cum', 'Cup', 'Cub')

## Limitations

This demo could also check other reader-intended content outside of body text (for example, heading title text), but it doesn't.

Hunspell supports all manner of human languages for spell checking. This demo is limited to US English.

## Support

None; please do not use this demo for production work!


