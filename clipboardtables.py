from tkinter import Tk

def build_table(clipboard, add_header=True):
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
    clipboard = Tk().clipboard_get()
    table = build_table(clipboard)
    
    if table:
        print('\n'.join(table))