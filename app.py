from langchain_core.output_parsers import JsonOutputParser
from model import RagLLM
from template import get_prompt
import json


try:
     # Step 1: Get Reddit username from user input
    username = input("Enter the Reddit username: ").strip()

    # Step 2: Initialize the model
    print("\n","Initializing LLM engine...")
    llm = RagLLM()

    # Step 3: Generate a persona prompt using the template and Reddit data
    print("\n","Generating prompt from template...")
    formatted_prompt = get_prompt(username)

     # Step 4: Send the prompt to the LLM and get a response
    print("\n","Running LLM Inference... (this might take a few seconds)")
    raw_output = llm.invoke(formatted_prompt)
    
    # Step 5: Save the parsed output to a text file named after the username
    print("\n","Saving results to file...")
    parser = JsonOutputParser()
    parsed_output = parser.parse(raw_output.content)
    output_file = f"{username}_persona.txt"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(parsed_output, indent=2))

    print(f"\n","Success: The process completed successfully. Output saved to `{output_file}`")

except Exception as e:
    print("\n","Error:", e)