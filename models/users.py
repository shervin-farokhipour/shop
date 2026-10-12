from datetime import datetime

from validation.validation import email_validator


class User:
    def __init__(self, user_id, email, password):
        self.id = user_id
        self.email = email
        self.password = password
        self.created_at = datetime.now()

    # ---------------- EMAIL ----------------
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        email_validator(email)
        self.__email = email

    # ---------------- PASSWORD ----------------
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("خطا: رمز عبور باید حداقل ۸ کاراکتر باشد.")
        if not any(char.isupper() for char in value):
            raise ValueError("خطا: رمز عبور باید حداقل یک حرف بزرگ (A-Z) داشته باشد.")
        if not any(char.isdigit() for char in value):
            raise ValueError("خطا: رمز عبور باید حداقل یک عدد داشته باشد.")
        self._password = value


class Buyer(User):
    def __init__(self, user_id, email, password, first_name, last_name, phone, address):
        super().__init__(user_id, email, password)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address

    # ---------------- FIRST NAME ----------------
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        clean_name = value.strip()
        if len(clean_name) < 2:
            raise ValueError("خطا: نام نمی‌تواند کمتر از ۲ کاراکتر باشد.")
        if len(clean_name) > 50:
            raise ValueError("خطا: نام بیش از حد طولانی است (حداکثر ۵۰ کاراکتر).")
        self._first_name = clean_name


class Seller(User):
    def __init__(self, user_id, email, password, store_name, phone, support_email):
        super().__init__(user_id, email, password)
        self.store_name = store_name
        self.phone = phone
        self.support_email = support_email