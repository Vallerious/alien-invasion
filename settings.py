class Settings:
    """ A class that contains all the settings for the alien invasion game. """

    class __Settings:
        def __init__(self, **options):
            self.options = options

    instance = None

    def __init__(self):
        if not Settings.instance:
            Settings.instance = Settings.__Settings(
                background_color=(230, 230, 230),
                screen_dim=(1200, 800),
                caption='Alien Invasion',
                total_lives=3
            )

    def __getattr__(self, name):
        return self.instance.options[name]
