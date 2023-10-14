# Class Explorer 2
#from qtenvhead import *
from PyQt5.QtWidgets import *
#from class_explorer import (sort, unique_methods, autocolumnize, list)

class SubclassDiagram:
    def __init__(self, parent, width=80):
        self.width = 80 # Default width
        self.parent = parent
        self.children = self.parent.__subclasses__()
    
    def run(self, *ags, **specialWidth):
        MASTER_TABLE = []
        for subclass in self.children:
            # if subclass was specified in specialWidth, use that width
            width = specialWidth.get(str(subclass.__name__), self.width)
            Hdivider= width*'─'
            
            blocks = [f'┌{Hdivider}┐',
                    f'│{subclass.__name__.center(width)}│',
                    f'├{Hdivider}┤',
            ]
            
            methods = self.list_columnize(self.sort(self.unique_methods(subclass, self.parent)), width)
            for line in methods:
                line = line.rstrip('\n').ljust(width,' ')
                line = f"│{line}│"
                blocks.append(line)
            
            footer = f'└{Hdivider}┘'
            
            blocks.append(footer)
            MASTER_TABLE.append(blocks)
        
        ## Print MASTER_TABLE
        print('')
        title = ' ' + self.parent.__name__ +' '
        titleWidth = len(title)
        titleTop = '╔' + titleWidth*'═' + '╗'
        titleBottom = '╚' + titleWidth*'═' + '╝'
        
        titleBlock = f"""
{titleTop}
║{title}║
{titleBottom}
    ╱╲
   ╱  ╲
    ││
    ││
"""
        print(titleBlock)
        for diagram in MASTER_TABLE:
            print('\n'.join(diagram))
            print('\n')
        print(f'╚══End {self.parent.__name__}\n\n')
            
    @staticmethod
    def sort(x): x=x; x.sort(); return x
    
    @staticmethod
    def unique_methods(subclass, parent, ignore_validation=False) -> list[str]: 
        """Input takes python objects as input and returns the unique methods of the subclass"""
        s = set(dir(subclass))
        p = set(dir(parent))
        
        # Check that parent class is subset of subclass
        if not p.issubset(s) and not ignore_validation:
            raise ValueError("Parent class is not a subset of subclass")
        
        return list(s.difference(p))
    
    @staticmethod
    def list_columnize(list, displaywidth=80):
        """Display a list of strings as a compact set of columns.

        Each column is only as wide as necessary.
        Columns are separated by two spaces (one was not legible enough).
        """
        outList = []
        
        if not list:
            #self.stdout.write("<empty>\n")
            #return
            return []

        nonstrings = [i for i in range(len(list))
                        if not isinstance(list[i], str)]
        if nonstrings:
            raise TypeError("list[i] not a string for i in %s"
                            % ", ".join(map(str, nonstrings)))
        size = len(list)
        if size == 1:
            #self.stdout.write('%s\n'%str(list[0]))
            #return
            return ['%s\n'%str(list[0])]
        # Try every row count from 1 upwards
        for nrows in range(1, len(list)):
            ncols = (size+nrows-1) // nrows
            colwidths = []
            totwidth = -2
            for col in range(ncols):
                colwidth = 0
                for row in range(nrows):
                    i = row + nrows*col
                    if i >= size:
                        break
                    x = list[i]
                    colwidth = max(colwidth, len(x))
                colwidths.append(colwidth)
                totwidth += colwidth + 2
                if totwidth > displaywidth:
                    break
            if totwidth <= displaywidth:
                break
        else:
            nrows = len(list)
            ncols = 1
            colwidths = [0]
        for row in range(nrows):
            texts = []
            for col in range(ncols):
                i = row + nrows*col
                if i >= size:
                    x = ""
                else:
                    x = list[i]
                texts.append(x)
            while texts and not texts[-1]:
                del texts[-1]
            for col in range(len(texts)):
                texts[col] = texts[col].ljust(colwidths[col])
            #self.stdout.write("%s\n"%str("  ".join(texts)))
            outList.append("%s\n"%str("  ".join(texts)))
        
        return outList



"""
https://en.wikipedia.org/wiki/Box-drawing_character?useskin=vector
Box Drawing[1]
Official Unicode Consortium code chart (PDF)
 	0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
U+250x	─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
U+251x	┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
U+252x	┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
U+253x	┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
U+254x	╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
U+255x	═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
U+256x	╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
U+257x	╰	╱	╲	╳	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿
Notes
1.^ As of Unicode version 15.1

'light_bar_box' : '┌─┐│┘─└│',
'light_bar_box_x2' : '╔═╗║╝═╚║'

"""

if __name__ == '__main__':
    import os
    os.system("")
    d = SubclassDiagram(QAbstractButton)
    d.run(QRadioButton=25, QCheckBox=25, QPushButton=25, QToolButton=40)
    #frame = SubclassDiagram(QFrame)
    #frame.run()
    #widget = SubclassDiagram(QWidget)
    #widget.run()
    