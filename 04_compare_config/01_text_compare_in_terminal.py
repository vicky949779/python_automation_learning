import difflib   # comparision purpose use this

with open('04_compare_config/g_config.txt') as g_data:
    g_config = g_data.read()

with open('04_compare_config/new_config.txt') as n_data:
    n_config = n_data.read()

# difflib.Differ().compare() compares two lists of strings and highlights differences.

delta = difflib.Differ().compare(g_config.splitlines(), n_config.splitlines())

# print(delta)
# for data in delta:
#     print(data)
###########################################################################################################

# - → Line is present in g_config but missing in n_config (deleted line).
# + → Line is added in n_config but missing in g_config.
# → Line is unchanged in both files.
# ? → Shows character-level differences (not commonly used).
