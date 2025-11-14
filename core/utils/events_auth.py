from django_eventstream.channelmanager import DefaultChannelManager

class ChannelManager(DefaultChannelManager):
    def can_read_channel(self, user, channel):
        # all channels (just one as of writing this) require auth.
        if user is None:
            return False
        return True
