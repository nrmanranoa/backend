import re

def separate_elements(compound):
    # Regular expression to match elements and their counts
    pattern = re.compile(r'([A-Z][a-z]*)(\d*)')

    # Find all matches in the compound
    matches = pattern.findall(compound)

    # Extract elements and counts
    elements = [match[0] for match in matches]

    return elements