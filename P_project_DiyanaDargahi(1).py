
import mysql.connector                  # اتصال پایتون به دیتابیس
import os                               # ارتباط با سیستم عامل و کار با فایل و پوشه ها
from mysql.connector import Error       # دریافت خطاهای مربوط به اتصال و دستورات دیتابیس


class Database:

    def __init__(self, host, user, password, database=None):
        self.host = host                # ذخیره آدرس سرور دیتابیس
        self.user = user                # ذخیره نام کاربری
        self.password = password        # ذخیره رمز عبور
        self.database = database        # ذخیره نام دیتابیس (مقدار پیش فرض None)
        self.connection = None          # برای نگهداری ارتباط با دیتابیس
        self.cursor = None              # ابزار ارسال دستورات به دیتابیس
        self.connect()                  # فراخوانی تابع اتصال به دیتابیس

    def connect(self):                  # تابع تلاش برای اتصال به MySQL
        try:
            self.connection = mysql.connector.connect(
                host=self.host,         # آدرس سرور دیتابیس
                user=self.user,         # نام کاربری
                password=self.password, # رمز عبور
                database=self.database  # نام دیتابیس
            )
            self.cursor = self.connection.cursor()  # ایجاد ابزار ارسال دستورات به دیتابیس

        except Error as e:              # دریافت خطاهای احتمالی هنگام اتصال
            print(e)                    # نمایش متن خطا

    def create_database(self, name):    # تابع ساخت دیتابیس
        try:
            self.cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {name}"  # ساخت دیتابیس در صورت وجود نداشتن
            )
            print('Database created!')  # نمایش پیام موفقیت

        except Error as e:              # دریافت خطاهای احتمالی
            print(e)                    # نمایش متن خطا

    def connect_database(self, name):   # تابع اتصال به دیتابیس ساخته شده
        try:
            if self.cursor:             # بررسی وجود cursor
                self.cursor.close()     # بستن cursor قبلی

            if self.connection:         # بررسی وجود اتصال قبلی
                self.connection.close() # بستن اتصال قبلی

            self.database = name        # ذخیره نام دیتابیس جدید

            self.connection = mysql.connector.connect(
                host=self.host,         # آدرس سرور
                user=self.user,         # نام کاربری
                password=self.password, # رمز عبور
                database=self.database  # اتصال به دیتابیس مورد نظر
            )

            self.cursor = self.connection.cursor()  # ایجاد cursor جدید

        except Error as e:              # دریافت خطاهای احتمالی
            print(e)                    # نمایش متن خطا

    def create_question_table(self):    # تابع ساخت جدول سوال ها
        try:
            sql = '''
            CREATE TABLE IF NOT EXISTS questions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                question TEXT NOT NULL,
                option_a VARCHAR(255) NOT NULL,
                option_b VARCHAR(255) NOT NULL,
                option_c VARCHAR(255) NOT NULL,
                option_d VARCHAR(255) NOT NULL,
                correct_answer CHAR(1) NOT NULL
            )
            '''                         # ذخیره دستور ساخت جدول در متغیر sql

            self.cursor.execute(sql)    # ارسال دستور ساخت جدول به MySQL
            self.connection.commit()    # ثبت تغییرات در دیتابیس
            print('Questions table created!') # نمایش پیام موفقیت

        except Error as e:              # دریافت خطاهای احتمالی
            print(e)                    # نمایش متن خطا


db_info = {                             # ذخیره اطلاعات اتصال به دیتابیس در دیکشنری
    'host': 'localhost',                # آدرس سرور
    'user': 'root',                     # نام کاربری
    'password': 'YOUR_PASSWORD'         # رمز عبور دیتابیس
}

db = Database(**db_info)                # ارسال اطلاعات دیکشنری به پارامترهای کلاس

if db.connection and db.connection.is_connected():  # بررسی برقراری اتصال
    print('Connected successfully')    # نمایش پیام اتصال موفق

    db.create_database('AskMeQuiz')     # فراخوانی تابع ساخت دیتابیس

    db.connect_database('AskMeQuiz')    # اتصال به دیتابیس ساخته شده

    db.create_question_table()          # فراخوانی تابع ساخت جدول سوال ها
