# This file contains code for loading a file, performing some replacement, and writing out the result.
import argparse
from string import ascii_letters


# Create a function for
def replace_every_nth_letter(data: str, n: int, replacement_char: str = "*") -> str:
    """
    Replace every nth letter with the specified character, then return the result.
    Parameters
    ----------
    data : str
        Data to process.
    n : int
        Controls the spacing of the replacement; every 'n'th letter is replaced. Restriction: n >= 1.
    replacement_char : str
        Character to use for replacing the nth letter.

    Returns
    -------
    str
        Data with the appropriate replacements.
    """
    letter_counter = 0
    processed_data = ""
    for char in data:
        if char in ascii_letters:
            # Character is a letter
            letter_counter += 1
        if letter_counter == n:
            # This letter is the nth; do replacement
            letter_counter = 0
            processed_data += replacement_char
        else:
            processed_data += char
    return processed_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Feature string replacer",
                                     description="Processes a file and replaces every 3rd letter with *, and every "
                                                 "space with -")
    parser.add_argument("input_file", help="The file to process.")
    parser.add_argument("output_file", help="The file to which the results should be written.")
    args = parser.parse_args()

    # Open input file, get contents
    f = open(args.input_file, "r")
    data = f.read()
    f.close()

    # Replace " " with "-"
    new_data = data.replace(" ", "-")

    # Process
    new_data = replace_every_nth_letter(new_data, n=3, replacement_char="*")

    # Write out data to file
    f = open(args.output_file, "w")
    f.write(new_data)
    f.close()

    # Done!

