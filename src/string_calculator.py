# string_calculator.py
import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    
    delimiter = ','
    if numbers.startswith("//"):
        parts = numbers.split('\n', 1)
        delimiter = parts[0][2:] 
        numbers = parts[1]
    
    numbers = numbers.replace('\n', delimiter)
    
    num_list = re.split(f'[{re.escape(delimiter)}]', numbers)
    
    num_list = [int(num) for num in num_list if num]
    negatives = [num for num in num_list if num < 0]
    
    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
    
    return sum(num_list)