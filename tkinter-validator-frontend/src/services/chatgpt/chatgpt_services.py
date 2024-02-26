from openai import OpenAI


class ChatgptService:
    @classmethod
    def get_answer(cls, question: str = 'hi'):
        try:
            client = OpenAI(
                # api_key='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',
                api_key='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',
            )
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return str(e)
