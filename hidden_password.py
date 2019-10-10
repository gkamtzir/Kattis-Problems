def check_password(password, message):
    # This is the current index of the
    # message string.
    index = 0
    for i in range(len(password)):
        target = password[i]
        rest = password[i + 1:]

        # The target hasn't been found yet.
        found = False

        for j in range(index, len(message)):
            # If the target is found the index
            # is updated and the iteration outer
            # loop continues.
            if target == message[j]:
                index = j + 1
                found = True
                break
            elif message[j] in rest:
                # If the letter is not the target
                # and is one of the following letters
                # then the message is invalid.
                return False
        # Checking if the target letter
        # could not be found.
        if not found:
            return False
    return True

password, message = map(str, input().split())

result = check_password(password, message)

if result:
    print("PASS")
else:
    print("FAIL")

        

