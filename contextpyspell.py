#!/usr/bin/env python3

from tree_sitter import Language, Parser
from hunspell import Hunspell
import argparse

def traverse_tree(tree):
    cursor = tree.walk()
    
    reached_root = False
    while reached_root == False:
        yield cursor.node
    
        if cursor.goto_first_child():
            continue
    
        if cursor.goto_next_sibling():
            continue
    
        retracing = True
        while retracing:
            if not cursor.goto_parent():
                retracing = False
                reached_root = True
    
            if cursor.goto_next_sibling():
                retracing = False

def get_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="ConTeXt file to spellcheck")
    
    return parser.parse_args()



def initialize_tree_sitter():
    Language.build_library(
      # Store the library in the `build` directory
      '../build/my-languages.so',
    
      # Include one or more languages
      [
        '../vendor/tree-sitter-context_en',
      ]
    )

    CONTEXT_LANGUAGE = Language('../build/my-languages.so', 'context')
    
    parser = Parser()
    parser.set_language(CONTEXT_LANGUAGE)
    
    return CONTEXT_LANGUAGE, parser
    
    
def main():
    
    h = Hunspell()
    
    CONTEXT_LANGUAGE, context_parser = initialize_tree_sitter()
    
    args = get_cli_arguments()
    
    with open(args.input_file) as f:
        document = f.read()
    
    tree = context_parser.parse(bytes(document, "utf8"))
    
    root_node = tree.root_node
    
    print(f"Concrete syntax tree for {args.input_file}")
    print(root_node.sexp())
    print("")
    
    for node in traverse_tree(tree):
      if node.type == "text":
        # print(node.text.strip())
        checktext = node.text.decode().strip()
        words = checktext.split()
        
        for word in words:
            if h.spell(word) == False:
                print(f"Found mispelled word: {word} on line {node.start_point[0]}")
                suggestions = h.suggest(word)
                print(f"Possible corrections: {suggestions}") 
                print("")

        


if __name__ == "__main__":
    main()

    
