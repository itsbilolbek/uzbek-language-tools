import polib
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check for translation errors in a PO file.')
    parser.add_argument('po_file', type=str, help='Path to the PO file to check')
    parser.add_argument("output_file", type=str, help="Path to save the output results")
    args = parser.parse_args()

    po = polib.pofile(args.po_file)
    
    errors = []
    for entry in po:
        if not entry.msgstr:
            errors.append(f"Missing translation for: {entry.msgid}")
        elif not entry.msgstr.strip():
            errors.append(f"Empty translation for: {entry.msgid}")
        elif entry.msgstr == entry.msgid:
            errors.append(f"Translation is the same as source for: {entry.msgid}")

    if errors:
        print("Translation errors found:")
        for error in errors:
            print(error)
    else:
        print("No translation errors found.")
