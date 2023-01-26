class NameTooShortError(Exception):
    """ Name less than or equal to 4 characters"""
    pass


class MustContainAtSymbolError(Exception):
    ''' Email does not have @ '''
    pass


class InvalidDomainError(Exception):
    ''' the domain is different than .com, .org... '''
    pass


email = input()
while email != "End":
    good_email = True

    if '@' in email:
        if len(email.split('@')[0]) <= 4:
            good_email = False
            raise NameTooShortError("Name must be more than 4 characters")

    else:
        good_email = False
        raise MustContainAtSymbolError("Email must contain @")

    if email.split('.')[-1] not in ['com', 'bg', 'org', 'net']:
        good_email = False
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if good_email:
        print("Email is valid")

    email = input()