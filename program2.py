def decode_message(s: str, p: str) -> bool:
    # Initialize the lengths of the message and the pattern
    m, n = len(s), len(p)
    
    # Create a DP table where dp[i][j] represents if pattern[0:j] matches message[0:i]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True
    
    # Handle patterns with leading '*' which can match an empty message
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                # Current characters match or '?' can match a single character
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    # Return if the entire message matches the entire pattern
    return dp[m][n]

# Test cases
print(decode_message("aa", "a"))    # False
print(decode_message("aa", "*"))    # True
print(decode_message("cb", "?a"))   # False
print(decode_message("cb", "c?"))   # True
