import re

import courses

courses.get_python()
courses.get_php()
courses.javadoc

text ="+7(854)232-55-66"

mem = re.match(r"\+7\(\d{3}\)\d{3}-\d{2]-\d{2}", text)
print(mem)