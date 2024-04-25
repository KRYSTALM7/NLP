import re
import os
from nltk.tokenize import word_tokenize
from collections import Counter
import textstat

# Step 1: Read file and extract code snippet
def read_code_file(file_path):
    with open(file_path, 'r') as file:
        code_snippet = file.read()
    return code_snippet

# Step 2: Preprocessing
def preprocess_code(code):
    # Extract function name, parameters, and comments
    function_name = re.search(r'def\s+([^\s(]+)|void\s+([^\s(]+)', code)
    parameters = re.findall(r'\((.*?)\)', code)[0].split(',')
    if function_name:
        function_name = function_name.group(1) or function_name.group(2)
    else:
        function_name = "unknown_function"
    return function_name.strip(), [param.strip() for param in parameters]

# Step 3: Feature Extraction
def extract_features(code):
    tokens = word_tokenize(code)
    word_counts = Counter(tokens)
    top_keywords = [word for word, count in word_counts.most_common(10)]
    return top_keywords

# Step 4: NLG Techniques
def generate_template_documentation(function_name, parameters):
    template = f"Function: {function_name}\nParameters: {', '.join(parameters)}"
    return template

# Step 5: Evaluation
def evaluate_readability(documentation):
    return textstat.flesch_reading_ease(documentation)

# Step 6: Integration
def generate_and_evaluate_documentation(file_path):
    # Read code file
    code_snippet = read_code_file(file_path)

    # Preprocess code
    function_name, parameters = preprocess_code(code_snippet)

    # Extract features
    features = extract_features(code_snippet)

    # Generate documentation
    generated_doc = generate_template_documentation(function_name, parameters)

    # Evaluate readability
    readability_score = evaluate_readability(generated_doc)

    return generated_doc, readability_score

# Example usage
file_path = "S:\CODES\PYTHON3.0\CRYPTOGRAPHY ASSIGNMENTS\euclidean.py"  # Path to your code file
generated_doc, readability_score = generate_and_evaluate_documentation(file_path)

print("Generated Documentation:")
print(generated_doc)
print("Readability score:", readability_score)
