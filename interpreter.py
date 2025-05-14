import re

# Dictionary of meme keywords and their Python equivalents
meme_dict = {
    "jugaad": "=",
    "ghoom ghoom": "for item in",
    "jab tak hai jaan": "while",
    "agar": "if",
    "warna": "else",
    "kaam": "def",
    "bhej de": "return",
    "ek_min": "lambda",
    "mere_yaar": "my_list",       # Example list
    "kitaab": "my_dict",          # Example dictionary
    "sab_ek_saath": "list comprehension",
    "sach_hai_kya": "True",
    "darwaza_kholo": "open",
    "picture_dikhao": "print",
    "topa": "None",               # fixed from toopa
    "ginty_karo": "enumerate",
    "jodi_banao": "zip",
    "mere_gang": "my_set",
    "sabka_badla": "map",
    "kuch_bhi": "#",
    "tauba_tauba": "raise Exception",
    "kalakaar": "MyClass",
    "gang": "class",
    "bolo_zara": "input",
    "multi_hero": "Thread",
    "thoda_ruko": "time.sleep",
    "f": "f"  # for f-strings (left as-is)
}

# Function to convert meme code to valid Python code
def meme_to_python(meme_code):
    for meme, python in meme_dict.items():
        meme_code = re.sub(r'\b' + re.escape(meme) + r'\b', python, meme_code)
    return meme_code

# Run code from .dsl file
def run_from_file(filename):
    try:
        # Open the file and read its contents
        with open(filename, 'r', encoding='utf-8') as f:
            meme_code = f.read()

        # Convert meme code to Python code
        python_code = meme_to_python(meme_code)

        print(" Code:\n")
        print(python_code)  # Display the converted Python code for debugging

        print("\nOutput:\n")
        # Execute the converted Python code
        exec(python_code)

    except FileNotFoundError:
        print(f"🚫 File '{filename}' not found.")
    except SyntaxError as e:
        print(f"🔥 Syntax error in the meme code: {e}")
    except Exception as e:
        print(f"🔥 Error during execution: {e}")

# Main function to interact with the user
if __name__ == "__main__":
    filename = input("Enter the filename of your meme code (e.g., 'examples/hello.dsl'): ").strip()
    run_from_file(filename)
