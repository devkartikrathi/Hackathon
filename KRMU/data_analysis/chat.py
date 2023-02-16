import openai
import pandas as pd
import ast
from key import KEY

openai.api_key = KEY

class coder:

    def __init__(self, data, inst, col_name):
        self.df = data
        self.instruction = inst
        self.columns = col_name

    def _code(self):
        column_info = " ".join([f"{column}: float" for column in self.columns])
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate only code that can be run using a single python exec function with all code is seperated with ';' to perform the following data analysis on a pandas dataframe named as df file and always add print function to output with correct notation: {self.instruction}\n\nColumn information: {column_info}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        code = response["choices"][0]["text"]
        return code