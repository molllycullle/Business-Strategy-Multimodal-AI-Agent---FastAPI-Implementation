from transformers import pipeline

class ContentWriter:
    def generate_content(self, prompt):
        generator = pipeline("text-generation", model="t5-small")
        return generator(prompt, max_length=100)[0]['generated_text']

if __name__ == "__main__":
    writer = ContentWriter()
    prompt = "Write a blog introduction for a new tech product launch focusing on AI advancements."
    content = writer.generate_content(prompt)
    print("Generated Content:\n", content)
