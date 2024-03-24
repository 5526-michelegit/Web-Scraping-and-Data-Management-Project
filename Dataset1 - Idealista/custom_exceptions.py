class DeactivateException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'DeactivateException, {0} '.format(self.message)
        else:
            return 'DeactivateException has been raised'

class ScrapingDetectionException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'ScrapingDetectionException, {0} '.format(self.message)
        else:
            return 'ScrapingDetectionException has been raised'