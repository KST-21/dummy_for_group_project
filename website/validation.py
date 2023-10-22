class Validation():
    def __init__(self) -> None:
        self.password_length_range = (8, 32)
        self.fullname_length_range = (2, 50)
        self.phone_number_length_range = (6, 16)
        
    def is_length_within_range(self, actual_length: int, max_length: int, min_length: int):
        return actual_length >= min_length and actual_length <= max_length
    
    def is_valid_password(self, password: str):
        min_password_length, min_password_length = self.password_length_range
        actual_password_length = len(password)
        return self.is_length_within_range(actual_password_length, min_password_length, min_password_length)
    
    def is_valid_fullname(self, fullname: str):
        min_fullname_length, max_fullname_length = self.fullname_length_range
        actual_fullname_length = len(fullname)
        return self.is_length_within_range(actual_fullname_length, min_fullname_length, max_fullname_length)
    
    def is_valid_phone_number(self, phone_number: str):
        min_phone_num_length, max_phone_num_length = self.phone_number_length_range
        actual_phone_num_length = len(phone_number)
        is_phone_num_within_range = self.is_length_within_range(actual_phone_num_length, min_phone_num_length, max_phone_num_length)
        return phone_number.isdigit() and is_phone_num_within_range
        