MAX_LEN = 50   # global
DEF_STR = ''

class Message():
    def __init__(self, sender, recipient):
        self.set_sender(sender)
        self.set_recipient(recipient)
        self.wishList = []


    def set_sender(self, sender):       # set with validation for sender
        if len(sender) <= MAX_LEN:
            self.sender = sender
            return True
        self.sender = DEF_STR
        return False


    def set_recipient(self, recipient):   # set with validation for recipient
        if len(recipient) <= MAX_LEN:
            self.recipient = recipient
            return True
        self.recipient = DEF_STR
        return False

    def append(self, line):  # method for body
        if self.str_ok(line) is True:
            self.wishList.append(str(line))
        else:
            self.wishList.append(DEF_STR)


    def str_ok(self, line):   #validation for body
        if len(line) <= MAX_LEN:
           return True
        else:
            return False

    def to_string(self): #for display
        return 'From: {}\nTo: {}\n{}'.format(self.sender, self.recipient,'\n'.join(self.wishList))
