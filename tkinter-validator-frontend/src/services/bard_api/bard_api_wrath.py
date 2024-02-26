from bardapi import Bard


class BardCommunication:
    """
        Class for communication with the IA
    """

    @classmethod
    def get_secure_1psid_cookie(cls):
        return ("dQgEGwI5yLpcTo8tUVTYJm3islVYnl4JKf"
                "-YtcuSdi6h1Gssp9KZ6lzsvj9wPl23EtNeuw.")

    @classmethod
    def question(cls, question):
        try:
            return \
                Bard(token=cls.get_secure_1psid_cookie()).get_answer(question)[
                    'content']
        except Exception as e:
            print(e)
