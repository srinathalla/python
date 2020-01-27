class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for mail in emails:
            local, domain = mail.split('@')
            if '+' in local:
                local = local[:local.index('+')]

            local = local.replace('.', '')
            seen.add(local + '@' + domain)

        return len(seen)


s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com",
                         "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
