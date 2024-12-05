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
        if username not in self.users:
            return False, "Kullanıcı adı bulunamadı."

        if "attempts" not in self.users[username]:
            self.users[username]["attempts"] = 0

        if self.users[username]["attempts"] >= 5:
            return False, "Hesabınız geçici olarak kilitlendi. Daha sonra tekrar deneyin."

        hashed_password = self.hash_password(password)

        if self.users[username]["password"] == hashed_password:
            self.users[username]["attempts"] = 0
            self.save_users()
            return True, f"Hoş geldiniz, {username}!"
        else:
            self.users[username]["attempts"] += 1
            self.save_users()
            remaining_attempts = 5 - self.users[username]["attempts"]
            if remaining_attempts > 0:
                return False, f"Yanlış şifre! Kalan deneme hakkınız: {remaining_attempts}"
            else:
                return False, "Hesabınız geçici olarak kilitlendi. Daha sonra tekrar deneyin."
