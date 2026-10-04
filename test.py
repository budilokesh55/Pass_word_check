s = input()

# Flags to check each condition
has_upper = False
has_lower = False
has_digit = False
has_special = False
no_consecutive = True

special = "@#$%&*"

# Check every character
for i in range(len(s)):

    if s[i].isupper():
        has_upper = True

    if s[i].islower():
        has_lower = True

    if s[i].isdigit():
        has_digit = True

    if s[i] in special:
        has_special = True

    # Check consecutive identical characters
    if i > 0 and s[i] == s[i - 1]:
        no_consecutive = False

# Check all conditions
if (len(s) >= 8 and
    has_upper and
    has_lower and
    has_digit and
    has_special and
    no_consecutive):

    print("STRONG")
else:
    print("WEAK")

    