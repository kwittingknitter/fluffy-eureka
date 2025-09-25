"""Custom errors"""

class UnsupportedOperationError(Exception):
    """Error for unsupported operation in utils.get_endpoint"""
    def __init__(self, message="Unsupported operation"):
        super().__init__(message)
