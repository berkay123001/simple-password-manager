import hashlib
import json

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

    def hash_password(self, password):
        """Şifreyi SHA-256 ile hash'ler."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Yeni bir kullanıcı kaydeder."""
        hashed_password = self.hash_password(password)  # Şifreyi hash'le
        if username in self.users:
            return False, "Bu kullanıcı adı zaten var."
        self.users[username] = {"password": hashed_password}
        self.save_users()
        return True, f"Hesap başarıyla oluşturuldu: {username}"

    def login_user(self, username, password):
        """Kullanıcıyı giriş yaparken doğrular."""
        hashed_password = self.hash_password(password)  # Girilen şifreyi hash'le
        if username not in self.users or self.users[username]["password"] != hashed_password:
            return False, "Kullanıcı adı veya şifre hatalı."
        return True, f"Hoş geldiniz, {username}!"
