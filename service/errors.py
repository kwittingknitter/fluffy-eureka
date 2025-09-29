"""Custom errors"""

class NoSeedDataError(Exception):
    """Error for no seed data found"""
    def __init__(self, message="No seed data found ", filepath=None):
        super().__init__(message+filepath)

class SeedDataInsertError(Exception):
    """Error for inserting seed data"""
    def __init__(self, message, e):
        super().__init__(message, e)
