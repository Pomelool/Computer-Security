trials:

1 anyʼ OR ʼxʼ=ʼx # (unicode smuggling, where the the "single quote" is actually not the standard single quote but some char that looks like it, later translated by database as single quote)
but this is not working!!


2 any\' OR \' k \'=\' k \'# (after doubling the single quote, \' becomes \'', which is translated as one single quote)
but I don't understand why this 'k' = 'k' is not working, but 1=1 does.

so answer is any\' OR 1=1#
