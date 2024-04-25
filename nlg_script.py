import re
from nltk.tokenize import word_tokenize
from collections import Counter
import textstat
import sys

# Function to read code file and extract code snippet
def read_code_file(file_path):
    with open(file_path, 'r') as file:
        code_snippet = file.read()
    return code_snippet

# Preprocess code
def preprocess_code(code):
    # Extract function name, parameters, and comments
    function_name = re.search(r'def\s+([^\s(]+)|void\s+([^\s(]+)', code)
    parameters = re.findall(r'\((.*?)\)', code)[0].split(',')
    if function_name:
        function_name = function_name.group(1) or function_name.group(2)
    else:
        function_name = "unknown_function"
    return function_name.strip(), [param.strip() for param in parameters]

# Generate documentation using template-based NLG
def generate_template_documentation(function_name, parameters):
    template = f"Function: {function_name}\nParameters: {', '.join(parameters)}"
    return template

# Evaluate readability of the documentation
def evaluate_readability(documentation):
    return textstat.flesch_reading_ease(documentation)

# Main function
def main():
    file_path = sys.argv[1]  # Path to the code file
    code_snippet = read_code_file(file_path)
    function_name, parameters = preprocess_code(code_snippet)
    generated_doc = generate_template_documentation(function_name, parameters)
    readability_score = evaluate_readability(generated_doc)
    print(generated_doc)
    print(readability_score)

if __name__ == "__main__":
    main()
