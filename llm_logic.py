# from openai import OpenAI

# with open("C:\Users\srina\Resume\resume-tailor-ai\api_key.txt", "r") as file:
#     api_key = file.read().strip()


# with open("config/api_key.txt", "r") as f:
#     api_key = f.read().strip()

# client = OpenAI(
#     api_key=api_key,
# )



# completion = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a person named Owaiz who speaks english. You are from India and you are a coder. You analyze chat history and text people in very short replies. Output should be the next chat response (text message only)"},
#             {"role": "system", "content": "Do not start like this [11:58 am, 26/04/2025] ~ShaikhOwaiz: "},
#             {"role": "user", "content": }
#         ]
#     )