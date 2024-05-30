[![License](https://img.shields.io/github/license/PANICBUTT0N/latin_dict?logo=gnu)](license.md)
# latin_dict
### PANICBUTTON
## Overview
This is a simple program designed to sort the
[Cambridge Latin Book III dictionary](https://www.cambridgescp.com/files/legacy_root_files/singles/ukdic3/index.html)
into a CSV file. Possible implementations include importing to [Anki](https://apps.ankiweb.net/) (CSV files created by
this project can be directly imported into Anki).\
\
**How It's Formatted:**\
Each entry is a CSV row containing the
following values:
1. Entry index (zero-based line numbering)
2. Latin word
3. Gender
4. English definition
5. Index of referenced entry (see below)

**How It Works:**\
The Cambridge Latin Book III dictionary has all dictionary values stored in a massive string on line 178 of the page's
source. Individual entries are delimited by carets (^), and words are separated from their definitions by dollar signs
($).

The program  creates a list for each entry, comprised of the entry's initial components (Latin word and definition).
Each entry list is then nested in the global entries list.

Some noun entries have genders, denoted with "m." for masculine, "n." for neuter, or "f." for feminine. The program
locates these and migrates them from the Latin word cell to the gender cell.

Some definition values reference other entries in the dictionary, rather than providing their own definitions. These
definitions are formatted as "{see} [referenced_entry_word]". The program locates these referenced entries and inputs
their Latin word and definition values into the definition cells of the entries that reference them. It also adds the
index of the referenced entry to the entry that references it.

**Additional Formatting:**
* Some entries are preceded by asterisks (*). The program removes these.
* Some entries label genitive forms of Latin words with "{gen.}". The program preserves the genitive label, but
removes the curly braces.
* Some entries include plural forms of words, labeled with "pl." These are given a leading space for readability.
* Some entries contain percent signs (%), originally used to denote sub-entries. As of now, these are simply removed,
however, future commits of latin_dict may implement sub-entry denotation and formatting.
* Entries with multiple words in Latin word and/or definition cells were originally comma delimited. To prevent CSV
formatting issues, these commas are replaced with hyphens (-) during the code's runtime. However, they are re-replaced
with commas in the final CSV output.
<a/>
## License
[GNU General Public License](https://choosealicense.com/licenses/gpl-3.0/)