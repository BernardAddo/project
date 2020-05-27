from typing import List, Dict, Any, Union  # used to provide type hinting
from tkinter import*
from tkinter import ttk

# Dictionary that maps numbers to their alphabet form
# This is used to quickly get these letters for bases higher than 10
num_to_letters: Dict = {

    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J',
    20: 'K',
    21: 'L',
    22: 'M',
    23: 'N',
    24: 'O',
    25: 'P',
    26: 'Q'

}

# Dictionary that maps alphabets to their numeric form
# This is used to quickly get the correspondig values of
# such alphabets especially when converting from bases higher
# than 10 to other bases
letters_to_num: Dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
}


class BaseStack:
    """
    Stack Implementation based of python list (array)
    values are kept in as string to suite the implementation needs
    methods:
        pop:
            pops out the last element of the stack and returns it
        push:
            pushes an element to the top of the stack
        to_base_string:
            Helper function to convert the stack to a string
            representing the results after computation of bases
    """

    def __init__(self, content: List = None) -> None:
        self._stack = content or []

    def pop(self) -> Union[str, int]:
        """
        pop: pops out the last element of the stack and returns it
        """
        return self._stack.pop()

    def push(self, value: Union[str, int]) -> bool:
        """
        push: pushes an element to the top of the stack
        """
        self._stack.append(str(value))
        return True

    def to_base_string(self):
        """
        to_base_string: Helper function to convert the stack to a string
                        representing the results after computation of bases
        """
        stack = self._stack[::-1]
        return ''.join(stack)


class Converter:
    """
    Converter:
        Contains functions to do actual conversion numbers from one base to another.
        methods:
            convert(number: Union[str, int],to_base:int = 10, from_base: int=10)
            from_base_ten(number: Union[str, int],base: int) -> str
            to_base_ten(number: Union[str, int],base: int) -> str
    """

    def convert(self, number: Union[str, int], to_base: int = 10, from_base: int = 10) -> str:
        """
        convert:
            description:
                Entry point to handle all kinds of conversions.

                It calls the appropriate (function from_base_ten or to_base_ten) to
                do the actual conversion depending on the arguments provided
                If none of the bases we are converting between is 10, we first convert
                to base 10 and then to the desired base.
                Leaving both to_base and from_base blank just results
                returning the value
            arguments:
                number:
                    types: str, int
                    default: None
                to_base:
                    description: The base to convert to
                    types: int
                    default: 10
                from_base:
                    description: The base we are converting from
                    types: int
                    default: 10
            returns:
                type: str
            example:
                convert(number=10, to_base=2, from_base=10)
                    convert from base 10 to base 2
                convert(number=10, to_base=2)
                    converts from base 10 to base 2
                convert(number=10, from_base=11)
                    converts from base 11 to base 10
        """
        if from_base != 10:
            number = self.to_base_ten(number, from_base)
        if to_base != 10:
            number = self.from_base_ten(number, to_base)
        return number

    def from_base_ten(self, number: Union[str, int], base: int) -> str:
        """
        from_base_ten:
            description:
                Converts a number from base ten to the specified base.
            arguments:
                number:
                    types: str, int
                    default: None

                base:
                    description: The base we are converting to
                    types: int
                    default: None
            returns:
                type: str
            example:
                from_base_ten(number=10, base=2)
                    convert from base 10 to base 2

        """
        stack: BaseStack = BaseStack()
        number = int(number)
        while True:
            if number < base:
                # if the number is greater than 9, get its corresponding
                # letter and push to the stack else push the remainder to the
                # stack
                stack.push(num_to_letters.get(number, number))
                break
            else:
                number, remainder = number // base, number % base
                # if the remainder is greater than 9, get its corresponding
                # letter and push to the stack else push the remainder to the
                # stack
                stack.push(num_to_letters.get(remainder, remainder))
        return stack.to_base_string()

    def to_base_ten(self, number: Union[str, int], base) -> str:
        """
        to_base_ten:
            description:
                Converts a number from a given base to  base ten.
            arguments:
                number:
                    types: str, int
                    default: None

                base:
                    description: The base we are converting the number from
                    types: int
                    default: None
            returns:
                type: str
            example:
                to_base_ten(number=10, base=2)
                    convert from base 2 to base 10
        """
        number = str(number)[::-1]
        result = 0
        for i in range(len(number) - 1, -1, -1):
            # if the current character (ie. number[i]) is a letter, get its corresponding
            # numeric value for the calculation otherwise it is considered a number and used directly
            result += int(letters_to_num.get(number[i], number[i])) * base ** i
        return str(result)


#Code for Graphical User interface
#Takes three inputs from: number, current base, base to be converted to

def calculate(*args):
    try:
        number=int(value.get())
        from_base= int(base_from.get())
        to_base= int(base_to.get())
        result.set(Converter().convert(number=number,to_base=to_base,from_base=from_base))
    except ValueError:
        pass

root=Tk()
root.title('Number Base Converter')

mainframe= ttk.Frame(root,padding="100 60 60 100")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

value= StringVar()
base_from= StringVar()
base_to= StringVar()
result= StringVar()

value_entry=ttk.Entry(mainframe,width=5, textvariable=value)
value_entry.grid(column=1, row=2, sticky=(W,E))

base_from_entry= ttk.Entry(mainframe,width=5, textvariable=base_from)
base_from_entry.grid(column=2, row=2, sticky=(W,E))

base_to_entry= ttk.Entry(mainframe,width=5,textvariable=base_to)
base_to_entry.grid(column=3, row=2, sticky=(W,E))

ttk.Label(mainframe,textvariable=result).grid(column=1, row=3, sticky=(W,E))
ttk.Button(mainframe,text='convert',command=calculate).grid(column=2,row=3,sticky=(W,E))
ttk.Label(mainframe,text='Number').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe,text='From Base').grid(column=2, row=1, sticky=W)
ttk.Label(mainframe,text='To Base').grid(column=3, row=1, sticky=W)

for child in mainframe.winfo_children():child.grid_configure(padx=5,pady=5)
value_entry.focus()
base_from_entry.focus()
base_to_entry.focus()
root.bind('<Return>',calculate)
root.mainloop()
