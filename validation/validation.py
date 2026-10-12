import re

email_regex = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

def email_validator(email):
    if not re.match(email_regex, email):
        raise ValueError("خطا: فرمت ایمیل نامعتبر است!")


from models import users

#
# print("--- سیستم تست اعتبارسنجی (Validation Test) ---")
# print("(برای خروج از برنامه، در بخش آیدی کلمه exit را تایپ کنید)\n")
#
# while True:
#     print("-" * 30)
#     user_id_input = input("آیدی کاربر (عدد): ")
#
#     if user_id_input.lower() == 'exit':
#         print("خروج از سیستم تست. خسته نباشید!")
#         break
#
#     email_input = input("ایمیل: ")
#     password_input = input("رمز عبور: ")
#     first_name_input = input("نام: ")
#
#     try:
#         user_id = int(user_id_input)
#
#         # تلاش برای ساخت شیء خریدار
#         # (اطلاعات نام خانوادگی، تلفن و آدرس را موقتاً ثابت دادیم تا تست سریع‌تر انجام شود)
#         new_buyer = Buyer(
#             user_id=user_id,
#             email=email_input,
#             password=password_input,
#             first_name=first_name_input,
#             last_name="تستی",
#             phone="09120000000",
#             address="تهران"
#         )
#
#         print(f"\n✅ موفقیت! کاربر '{new_buyer.first_name}' با ایمیل '{new_buyer.email}' از سد ولیدیشن‌ها گذشت.")
#
#     except ValueError as e:
#         # ارورهایی که در فایل users.py تعریف کردید اینجا چاپ می‌شوند
#         print(f"\n❌ خطای اعتبارسنجی سیستم: {e}")
#
#     except Exception:
#         print("\n⚠️ خطای سیستمی: لطفا آیدی را فقط به صورت عدد وارد کنید.")