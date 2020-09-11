import re

text = """
someone@domain.com
sdflksjdf@fsdf.sddf
"""

pattern = r"([a-z]+)@([a-z]+)\.([a-z]+)"

result = re.findall(pattern, text)
print(result)