import json

passwords = []


def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def register_user():
    users = load_users()
    while True:
        username = input("Kullanıcı adı oluşturun: ").strip()
        if username in users:
            print("Bu kullanıcı adı zaten var. Başka bir kullanıcı adı deneyin.")
            continue
        password = input("Şifre oluşturun: ").strip()
        users[username] = password
        save_users(users)
        print(f"Hesap başarıyla oluşturuldu, {username}!")
        return username


def login_user():
    """Var olan kullanıcı için giriş yapar."""
    users = load_users()
    while True:
        username = input("Kullanıcı adınızı girin: ").strip()
        if username not in users:
            print("Bu kullanıcı adı mevcut değil. Önce hesap oluşturun.")
            return None
        password = input("Şifrenizi girin: ").strip()
        if users[username] == password:
            print(f"Giriş başarılı, {username}!")
            return username
        else:
            print("Hatalı şifre. Tekrar deneyin.")


def user_menu():
    """Kullanıcıya hesap oluşturma veya giriş yapma seçeneği sunar."""
    while True:
        print("\n1. Hesap Oluştur")
        print("2. Giriş Yap")
        choice = input("Bir seçenek girin (1-2): ")
        if choice == "1":
            return register_user()
        elif choice == "2":
            username = login_user()
            if username:
                return username
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")


def load_passwords(username):
    """Belirli bir kullanıcı için şifreleri JSON dosyasından yükler."""
    filename = f"{username}_passwords.json"
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_passwords(username):
    """Belirli bir kullanıcı için şifreleri JSON dosyasına kaydeder."""
    filename = f"{username}_passwords.json"
    with open(filename, "w") as file:
        json.dump(passwords, file, indent=4)
    print(f"{username} için şifreler kaydedildi.")


def add_password(username):
    """Yeni bir şifre ekler ve JSON dosyasına kaydeder."""
    while True:
        site = input("Site Adı: ").strip()
        if not site:
            print("Site adı boş bırakılamaz!")
            continue
        username_input = input("Kullanıcı Adı: ").strip()
        if not username_input:
            print("Kullanıcı adı boş bırakılamaz!")
            continue
        password = input("Şifre: ").strip()
        if not password:
            print("Şifre boş bırakılamaz!")
            continue
        passwords.append({"site": site, "username": username_input, "password": password})
        save_passwords(username)
        print(f"{site} için şifre başarıyla eklendi!")
        break


def list_passwords():
    """Kayıtlı şifreleri listeler."""
    if not passwords:
        print("Henüz hiçbir şifre eklenmedi!")
    else:
        print("\nKayıtlı Şifreler:")
        print(f"{'No':<4}{'Site':<20}{'Kullanıcı Adı':<20}{'Şifre':<20}")
        print("-" * 60)
        for index, record in enumerate(passwords, start=1):
            print(f"{index:<4}{record['site']:<20}{record['username']:<20}{record['password']:<20}")


def display_menu():
    """Kullanıcıya menüyü gösterir."""
    print("\nPassword Manager")
    print("1. Şifre Ekle")
    print("2. Şifreleri Listele")
    print("3. Çıkış")


def main():

    global passwords
    username = user_menu()  # Hesap oluştur veya giriş yap
    passwords = load_passwords(username)  # Kullanıcıya özel şifreleri yükle

    while True:
        display_menu()
        choice = input("Bir seçenek girin (1-3): ")
        if choice == "1":
            add_password(username)  # Kullanıcıya özel şifre ekleme
        elif choice == "2":
            list_passwords()
        elif choice == "3":
            save_passwords(username)  # Çıkarken şifreleri kaydet
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
