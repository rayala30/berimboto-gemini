class GoogleAIPrompt:
    def __init__(self, text, context=None, instructions=None, examples=None):
        self.text = text
        self.context = context
        self.instructions = instructions
        self.examples = examples

    def to_dict(self):
        # Adapt the dictionary structure based on the specific Google AI LLM
        prompt_dict = {
            "text": self.text,
            "context": self.context,
            # ... other fields as needed
        }
        return prompt_dict