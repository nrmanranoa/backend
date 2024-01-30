import re
import time
import random

def separate_elements(compound):
    # Regular expression to match elements and their counts
    pattern = re.compile(r'([A-Z][a-z]*)(\d*)')

    # Find all matches in the compound
    matches = pattern.findall(compound)

    # Extract elements and counts
    elements = [match[0] for match in matches]

    return elements

def fooness(formula: str) -> float:
    # Mocking a time-consuming operation
    time.sleep(random.uniform(1, 5))
    return random.uniform(0, 1)