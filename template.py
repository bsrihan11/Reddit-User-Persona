from langchain.prompts import PromptTemplate
from scrapper import get_user_data
from schema import parser


def format_messages(data):
    """
    Joins a list of text entries into a single string separated by newlines.
    
    """
    
    return "\n".join(data)



def get_prompt(username):
    """
    Generates a prompt to be used by an LLM for creating a user persona from Reddit activity.

    Parameters:
        username: The Reddit username.

    Returns:
        str: A formatted prompt including the user's posts, comments, and instructions for generating a structured persona.

    Raises:
        ValueError: If the username is empty or user data is missing.
        ConnectionError: If Reddit client initialization fails.
        RuntimeError: If the user is not found or data cannot be retrieved.
    """
    
    user_data = get_user_data(username)
    
    
    persona_prompt = PromptTemplate(
            input_variables=['username','posts', 'comments'],
            template="""You are an expert in understanding online behavior. Based on the following Reddit user's activity (posts and comments), create a detailed and structured user persona. 

            ### User:
            {username}

            ### Reddit Posts:
            {posts}

            ### Reddit Comments:
            {comments}

            ---

            {format_instruction}

            --- 

            Note:
            - Citations are compulsory for all the fields mentioned above and having non default values.
            - Output the persona in clean plain text. Be concise but informative.
          
            """,
            partial_variables={"format_instruction": parser.get_format_instructions()}
        )



    formatted_prompt = persona_prompt.format(**user_data)
    
    
    return formatted_prompt







