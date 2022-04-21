# contextpyspell-demo.py

A quick demo of a format-aware spellchecker for ConTeXt using tree-sitter-context_en

## Installation

Clone or download this repo (possibly in a pyenv environment).

Install the `tree-sitter` dependency (using pip in this example):

    pip3 install tree_sitter

Install the `cyhunspell` dependency (using pip in this example):

    pip3 install cyhunspell
    
On first run, the script should configure and compile the included tree-sitter distribution for demo use.

## Trying it Out

This demo takes a single command line argument: the input file to process.

This demo will display the computed syntax tree of the input file, followed by any misspelled words, and suggested corrections for those words.

As an example, running this command:

    python3 contextpyspell-demo.py example_files/hello_world.tex
    
...should yield this output:

    Concrete syntax tree for example_files/hello_world.tex
    (document (preamble) (main (text_block (text) (paragraph_mark))) (postamble (text_block (text))))

    Found mispelled word: wurld! on line 2
    Possible corrections: ('world',)

## Limitations

This demo could also check other reader-intended content outside of body text (for example, heading title text), but it doesn't.

Hunspell supports all manner of human languages for spell checking. This demo is limited to US English.

This demo ships with a static copy of the tree-sitter-context_en parser. 

## Support

None; please do not use this demo for production work!


