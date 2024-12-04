from PasswordManager.PasswordManager import PasswordManager
from PasswordManager.UserManager import UserManager
def main():
    user_manager = UserManager()

    while True:
        print("\n1. Hesap Oluştur")
        print("2. Giriş Yap")
        print("3. Çıkış Yap ")
        choice = input("Bir seçenek girin (1-2): ")

        if choice == "1":
            username = input("Kullanıcı adı: ").strip()
            password = input("Şifre: ").strip()
            success, message = user_manager.register_user(username, password)
            print(message)
        elif choice == "2":
            username = input("Kullanıcı adı: ").strip()
            password = input("Şifre: ").strip()
            success, message = user_manager.login_user(username, password)
            print(message)
            if success:
                password_manager = PasswordManager(username)
                while True:
                    print("\nPassword Manager")
                    print("1. Şifre Ekle")
                    print("2. Şifreleri Listele")
                    print("3. Şifre Sil")
                    print("4. Şifre Güncelle")
                    print("5. Çıkış")

                    sub_choice = input("Bir seçenek girin (1-5): ")

                    if sub_choice == "1":
                        site = input("Site Adı: ").strip()
                        username_input = input("Kullanıcı Adı: ").strip()
                        password_input = input("Şifre: ").strip()
                        password_manager.add_password(site, username_input, password_input)
                        print("Şifre başarıyla eklendi!")
                    elif sub_choice == "2":
                        print(password_manager.list_passwords())
                    elif sub_choice == "3":
                        password_index=int(input("Şifresi silinecek passwordun sırasını giriniz: "))-1
                        password_manager.delete_password(password_index)

                    elif sub_choice == "4":
                        password_index=int(input("Şifresi güncellenecek passwordun sırasını giriniz: "))-1
                        new_password=input("Yeni Şifreyi giriniz: ")
                        password_manager.update_password(password_index, new_password)

                    elif sub_choice == "5":
                        print("Çıkış yapılıyor...")
                        break
                    else:
                        print("Geçersiz seçim.")

        elif choice == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
