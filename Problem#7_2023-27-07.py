""" 
Problem :
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


class Solution:
    def num_decodings(message):
        """_summary_

        Args:
            message (string): Coded Message

        Returns:
            int: number of possible decoded messages
        """
        if not message:
            return 0

        n = len(message)
        dp = [0] * (n + 1)

        dp[n] = 1
        dp[n - 1] = 1 if message[n - 1] != '0' else 0

        for i in range(n - 2, -1, -1):
            if message[i] == '0':
                continue

            num = int(message[i:i + 2])
            if num <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]

#__main__
print(Solution.num_decodings('111'))  # Output: 3 ('aaa', 'ka', and 'ak')
print(Solution.num_decodings('12'))   # Output: 2 ('ab' and 'l')
print(Solution.num_decodings('226'))  # Output: 3 ('bz', 'vf', and 'bbf')

