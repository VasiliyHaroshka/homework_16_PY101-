import string


class ActionsWithStrOrInt:
    """
    Class ActionsWithStrOrInt is used for recognize data that you give it when creating object of this class
    and executes some actions (described in methods) with your data.

    Attributes
    ----------
    value: str
        data that you give it when create object of this class

    Methods
    -------
    actions()
        - if you give type of data is 'str':
        this method returns list with all vowel letters from data if multiply of amount vowels letters in data
        to amount consonants letters in data more than length of data;
        - if you give type of data is 'int':
        this method returns multiply of sum all even numbers in data to length of data.

    len_value(self)
        Calculate length of string or integer that you give when you created object of class.
    """
    value: str | int

    def __init__(self, value: str | int) -> None:
        self.value = value

    def actions(self) -> list:
        """
        - if you give type of data is 'str':
        this method returns list with all vowel letters from data if multiply of amount vowels letters in data
        to amount consonants letters in data more than length of data;
        - if you give type of data is 'int':
        this method returns multiply of sum all even numbers in data to length of data.
        :return: list of vowels or list of consonants or integer equals multiply of sum all even numbers in data
                 to length of data.
        """
        count_vowels: int = 0
        vowels: list = []
        count_consonants: int = 0
        consonants: list = []
        if isinstance(self.value, str):
            for later in self.value:
                if later.lower() in "aeiouyауоыиэяюёе":
                    count_vowels += 1
                    vowels.append(later)
                elif later in string.punctuation or later in string.digits:
                    pass
                else:
                    count_consonants += 1
                    consonants.append(later)
            if count_vowels * count_consonants <= len(self.value):
                return vowels
            else:
                return consonants

        elif isinstance(self.value, int):
            even: list = []
            for i in str(self.value):
                if int(i) % 2 == 0:
                    even.append(int(i))
            return sum(even) * len(str(self.value))

        else:
            print("Error. Your data is not integer or string type.")

    def len_value(self) -> int:
        """
        Calculate length of string or integer that you give when you created object of class.
        :return: length of data
        """
        return len(str(self.value))


data = input("Input your data and program will give it to object of class ActionsWithStrOrInt: ")
options = input(
    "If you want to give your data as a integer, input 'i', otherwise input something different: ")
if options == 'i':
    try:
        sample = ActionsWithStrOrInt(int(data))
    except ValueError:
        print("Data that was input could not convert to integer type.\nYour data was given as a string type.")
        sample = ActionsWithStrOrInt(data)
else:
    sample = ActionsWithStrOrInt(data)

print(f"Result of 'actions' method's work: {sample.actions()}")
print(f"Result of 'len_value' method's work: {sample.len_value()}")
