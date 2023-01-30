class UserBlacklisted(Exception):
    """
    Выдается, когда пользователь пытается что-то сделать, находять в черном списке.
    """

    def __init__(self, message="Юзерок в niggerlist(blacklist)"):
        self.message = message
        super().__init__(self.message)


class UserNotOwner(Exception):
    """
    Выдается, когда пользователь пытается что-то сделать, но не является владельцем бота.
    """

    def __init__(self, message="Юзерок не создатель бота!"):
        self.message = message
        super().__init__(self.message)