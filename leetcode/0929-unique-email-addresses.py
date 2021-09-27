class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            name, domain = email.split('@', 1)
            name = name.split('+', 1)[0].replace('.', '')
            email_set.add((name, domain))
        return len(email_set)