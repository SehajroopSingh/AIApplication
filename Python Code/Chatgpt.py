




import openai
userinput = input("What's on your mind? \n")
# Set the GPT-3 API key and endpoint
openai.api_key = "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"
openai.api_endpoint = "https://api.openai.com/v1/completions"

# Use the `openai.Completion.create()` method to generate completions using GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=userinput,
    max_tokens=1024,
    n=1,
    temperature=0.5,
)

print(response["choices"][0]["text"])

input_variablele = input("Anything else? Write 'Y' or 'N' \n")



if input_variablele == "Y":
    power = input("Tell me! \n")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=power,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )
    print(response["choices"][0]["text"])
    
elif input_variablele == "N":
    print("Have a nice day!")
else :
    print("I don't understand. Please try again.")
    input_variablele = input("Anything else? Write 'Y' or 'N' \n")
    
