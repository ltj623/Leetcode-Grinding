class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        h = {}

        for email in emails:
            local, domain = email.split('@')
            local = local.replace(".","")
            if '+' in local:
                local = local[:local.index('+')]
            h[local + '@' + domain] = h.get(local + '@' + domain, 0) + 1
        return len(h)