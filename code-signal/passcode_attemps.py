def incorrectPasscodeAttempts(passcode, attempts):
    if passcode in attempts:
        i = attempts.index(passcode)
        if i <= 10:
            return True
    return False

passcode = "1111"
attempts = ["1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111",
 "1111"]

print(incorrectPasscodeAttempts(passcode, attempts))