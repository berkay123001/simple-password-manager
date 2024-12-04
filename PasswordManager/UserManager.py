import json
import os


class UserManager:
    def __init__(self, user_file="users.json"):
        self.user_file = user_file
        self.users = self.load_users()

    def load_users(self):
        """Kullanıcıları JSON dosyasından yükler."""
        try:
            with open(self.user_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        """Kullanıcıları JSON dosyasına kaydeder."""
        with open(self.user_file, "w") as file:
            json.dump(self.users, file, indent=4)

    def register_user(self, username, password):
        """Yeni bir kullanıcı kaydeder."""
        if username in self.users:
            return False, "Bu kullanıcı adı zaten var."
        self.users[username] = password
        self.save_users()
        return True, f"Hesap başarıyla oluşturuldu: {username}"

    def login_user(self, username, password):
        """Kullanıcı giriş yapar."""
        if username not in self.users or self.users[username] != password:
            return False, "Kullanıcı adı veya şifre hatalı."
        return True, f"Hoş geldiniz, {username}!"

#---------------------------------------------------------------------------
    def delete_user(self, username):
        """Kullanıcıyı siler."""
        if username in self.users:
            del self.users[username]  # Kullanıcıyı kullanıcı listesinden kaldır
            self.save_users()  # Güncel listeyi kaydet
            user_file = f"{username}_passwords.json"
            try:
                os.remove(user_file)  # Kullanıcının şifre dosyasını sil
                return True, f"{username} başarıyla silindi."
            except FileNotFoundError:
                return True, f"{username} silindi ancak şifre dosyası bulunamadı."
        else:
            return False, "Kullanıcı bulunamadı!"

