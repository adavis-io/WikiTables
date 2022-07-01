from tkinter import Tk

def build_table(clipboard, add_header=True):
    '''Generate a list of wiki-formatted table rows from a string provided,
    optionally including a template header row. Assumes input string data is
    tab-delimited - i.e. tabs delimit columns of data, with newlines separating
    individual rows.

    Arguments: 
        clipboard: a string containing the table to format
        add_header: whether to add a template header row

    returns: 
        a list containing wiki-formatted table rows as strings 
    '''
    if not clipboard:
        return
    
    colcount = len(clipboard.split('\n')[0].split('\t'))
    if add_header:
        header = '||'.join(['= header {:d} ='.format(c) for c in range(colcount)])
        header = '||{:s}||'.format(header)

        table_rows = [header]
    else:
        table_rows = []
    for row in clipboard.split('\n'):
        if row:
            table_rows.append('||{:s}||'.format(row.replace('\t', '||')))
    
    return table_rows

if __name__ == '__main__':
    '''Generate a Wiki-formatted text table of the clipboard contents.

    Usage: Enter data into Excel as normal. Highlight the data table to format
    and copy to the clipboard. Run 'py clipboardtables.py' from command prompt,
    PowerShell, or terminal of choice, then copy the string output for later
    use.
    '''
    clipboard = Tk().clipboard_get()
    table = build_table(clipboard)
    
    if table:
        print('\n'.join(table))