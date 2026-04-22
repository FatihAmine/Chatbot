from transformers import GPT2LMHeadModel, GPT2Tokenizer


def generate_response(prompt: str) -> str:
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=60,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.9,
        top_p=0.95,
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    user_text = input("> ")
    print(generate_response(user_text))
