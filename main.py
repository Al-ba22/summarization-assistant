from pathlib import Path

def load_prompt_template():
    with open("prompts/summarization_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()

def load_sample_text():
    with open("samples/sample_input.txt", "r", encoding="utf-8") as f:
        return f.read()

def format_prompt(prompt_template, text):
    return prompt_template.replace("{{TEXT}}", text)

def main():
    prompt_template = load_prompt_template()
    sample_text = load_sample_text()
    full_prompt = format_prompt(prompt_template, sample_text)
    
    print("\n--- Generated Prompt ---\n")
    print(full_prompt)

if __name__ == "__main__":
    main()
