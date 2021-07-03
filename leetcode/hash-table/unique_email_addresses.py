class Solution:
    def validate_email(self, email_address: str):
        email_arr = email_address.split('@')

        email_arr[0] = email_arr[0].replace('.', "")

        if '+' in email_arr[0]:
            email_arr[0] = email_arr[0][:email_arr[0].index('+')]

        return email_arr[0] + '@' + email_arr[-1]

    def numUniqueEmails(self, emails: list) -> int:
        if not emails:
            return 0
        
        return len(set(map(self.validate_email, emails)))
