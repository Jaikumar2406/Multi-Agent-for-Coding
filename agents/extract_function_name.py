import ast

def extract_function_name(code: str):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None   

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            return node.name

    return None  


def inject_function_call(code: str, inputs: list):
    function_name = extract_function_name(code)

    if function_name is None:
        return code

    args = ", ".join(repr(i) for i in inputs)

    call_code = f"""

# --- AUTO GENERATED CALL ---
try:
    result = {function_name}({args})
    print(result)
except Exception as e:
    print("RUNTIME_ERROR:", e)
"""

    return code + call_code
