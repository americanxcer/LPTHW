# the variable formater is defined of containing these 4 %variables which need to be further defined
formatter = "%r %r %r %r"

# here they are defined as numbers
print formatter % (1, 2, 3, 4)
# here they are defined as the words of the numbers
print formatter % ("one", "two", "three", "four")
# here they are defined as these words
print formatter % (True, False, False, True)
# here they are defined as the formatter itself, which makes it write the four %r's for everythime the word "format" is written
print formatter % (formatter, formatter, formatter, formatter)
# here they are defined as these sentences
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
