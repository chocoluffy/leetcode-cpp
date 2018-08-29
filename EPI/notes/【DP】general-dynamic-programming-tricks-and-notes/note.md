## padding and index
usually we need to set base case.
like for dp in strings, the base case is usually empty string. 
thus we enlarge the usual dp table by increasing the height and width by 1.
but when we iterate the table, and refer to the original string, we need to reduce the index by 1 to match with original string index.
