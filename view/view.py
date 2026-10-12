import tkinter as tk
from tkinter import ttk, messagebox

from models.users import User, Buyer, Seller
# ----------------- توابع عملیاتی -----------------
def submit_form():
    try:
        user_id = int(entry_id.get())
        email = entry_email.get()
        password = entry_password.get()
        first_name = entry_fname.get()

        # ساخت شیء خریدار (مقادیر نام خانوادگی، تلفن و آدرس را پیش‌فرض دادیم تا فرم شلوغ نشود)
        new_buyer = Buyer(
            user_id=user_id, email=email, password=password, first_name=first_name,
            last_name="تستی", phone="09120000000", address="تهران"
        )

        # اگر اطلاعات بدون خطا بود و ولیدیشن پاس شد، آن را به جدول سمت راست اضافه کن
        # tk.END یعنی به انتهای جدول اضافه کن
        table.insert("", tk.END, values=(new_buyer.id, new_buyer.first_name, new_buyer.email, new_buyer.password))

        messagebox.showinfo("موفقیت", f"کاربر {new_buyer.first_name} با موفقیت ثبت شد!")

        # پاک کردن کادرهای متنی بعد از ثبت موفق
        entry_id.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_fname.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("خطای اعتبارسنجی", str(e))
    except Exception:
        messagebox.showerror("خطای سیستمی", "لطفاً آیدی را فقط به صورت عدد وارد کنید.")


# ----------------- توابع نمایشی (غیرفعال) -----------------
def coming_soon(action_name):
    messagebox.showinfo("در دست توسعه", f"بخش {action_name} در نسخه‌های بعدی فعال خواهد شد.")


def update_user(): coming_soon("«ویرایش اطلاعات»")


def delete_user(): coming_soon("«حذف کاربر»")


def search_user(): coming_soon("«جستجوی کاربر»")


# ----------------- تنظیمات پنجره اصلی -----------------
root = tk.Tk()
root.title("سیستم مدیریت فروشگاه - پنل ادمین")
root.geometry("850x450")  # پنجره را بزرگتر کردیم تا جدول جا بشود
root.eval('tk::PlaceWindow . center')

# ==========================================
# فریم سمت چپ (بخش فرم ورود اطلاعات)
# ==========================================
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

tk.Label(left_frame, text="-- فرم ثبت نام --", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(left_frame, text="شناسه (ID):").pack(pady=5)
entry_id = tk.Entry(left_frame)
entry_id.pack()

tk.Label(left_frame, text="ایمیل:").pack(pady=5)
entry_email = tk.Entry(left_frame)
entry_email.pack()

tk.Label(left_frame, text="رمز عبور:").pack(pady=5)
entry_password = tk.Entry(left_frame, show="*")
entry_password.pack()

tk.Label(left_frame, text="نام:").pack(pady=5)
entry_fname = tk.Entry(left_frame)
entry_fname.pack()

# چیدمان دکمه‌ها در یک فریم کوچک زیر فرم
buttons_frame = tk.Frame(left_frame)
buttons_frame.pack(pady=25)

tk.Button(buttons_frame, text="ثبت", command=submit_form, bg="#4CAF50", fg="white", width=8).grid(row=0, column=3,
                                                                                                  padx=2, pady=2)
tk.Button(buttons_frame, text="جستجو", command=search_user, bg="#2196F3", fg="white", width=8).grid(row=0, column=2,
                                                                                                    padx=2, pady=2)
tk.Button(buttons_frame, text="ویرایش", command=update_user, bg="#FF9800", fg="black", width=8).grid(row=1, column=3,
                                                                                                     padx=2, pady=2)
tk.Button(buttons_frame, text="حذف", command=delete_user, bg="#F44336", fg="white", width=8).grid(row=1, column=2,
                                                                                                  padx=2, pady=2)

# ==========================================
# فریم سمت راست (بخش جدول نمایش اطلاعات)
# ==========================================
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

tk.Label(right_frame, text="-- لیست کاربران ثبت شده --", font=("Arial", 12, "bold")).pack(pady=10)

# تعریف ستون‌های جدول
columns = ("ID", "Name", "Email", "Password")
table = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)

# نام‌گذاری هدر (سرستون) های جدول
table.heading("ID", text="شناسه")
table.heading("Name", text="نام")
table.heading("Email", text="ایمیل")
table.heading("Password", text="رمز عبور")

# تنظیم عرض ستون‌ها
table.column("ID", width=50, anchor=tk.CENTER)
table.column("Name", width=100, anchor=tk.CENTER)
table.column("Email", width=180, anchor=tk.CENTER)
table.column("Password", width=120, anchor=tk.CENTER)

# اضافه کردن اسکرول‌بار به جدول (برای زمانی که تعداد کاربران زیاد می‌شود)
scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=table.yview)
table.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
table.pack(fill=tk.BOTH, expand=True)

# اجرای حلقه اصلی برنامه
root.mainloop()