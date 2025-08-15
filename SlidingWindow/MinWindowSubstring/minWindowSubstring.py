def minWindow(self, s: str, t: str) -> str:
    # Trivial case
    if t == "":
        return ""

    countOfT, window = {}, {}

    # Count the frequency number of characters needed in t
    for char in t:
        countOfT[char] = 1 + countOfT.get(char, 0)

    # Initiate the variables for what we have and need for the characters in t
    # have - the number of t-character in the current window
    # need - the number of t-character needed for the window to be valid
    have, need = 0, len(countOfT)

    # Left pointer initialized
    left = 0

    # Result variable initialized
    res, resLen = [-1, -1], float("infinity")

    # Algorithm starts
    for right in range(len(s)):
        char = s[right]
        window[char] = 1 + window.get(char, 0)

        # If the current char is in t, and their frequencies in curr window and t are the same
        if (char in countOfT) and (window[char] == countOfT[char]):
            have += 1

        # As long as the current window is valid (have == need),
        # shrink the current window by incrementing left pointer
        # to find the minimum valid window size
        while have == need:
            windowLen = right - left + 1
            if windowLen < resLen:
                res = [left, right]
                resLen = windowLen
            # Shrink from the left pointer
            window[s[left]] -= 1
            
            if s[left] in countOfT and window[s[left]] < countOfT[s[left]]:
                have -= 1

            left += 1

    left, right = res

    return s[left : right + 1] if resLen != float("infinity") else ""

