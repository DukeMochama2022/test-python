from utilities.math_utils import MathUtils
from utilities.test_utils import TextUtils

math_utils=MathUtils()
text_utils=TextUtils()
print("Factorial of 10 :", math_utils.factorial(10))
print("Vowels in my name is :", text_utils.count_vowels("Duke Mochama"))