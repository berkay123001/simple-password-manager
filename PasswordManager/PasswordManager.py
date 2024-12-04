import json

class PasswordManager:
    def __init__(self, username):
        self.username = username
        self.file_name = f"{username}_passwords.json"
        self.passwords = self.load_passwords()

    def load_passwords(self):
        """Şifreleri JSON dosyasından yükler."""
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_passwords(self):
        """Şifreleri JSON dosyasına kaydeder."""
        with open(self.file_name, "w") as file:
            json.dump(self.passwords, file, indent=4)

    def add_password(self, site, username, password):
        """Yeni bir şifre ekler."""
        self.passwords.append({"site": site, "username": username, "password": password})
        self.save_passwords()

    def list_passwords(self):
        """Kayıtlı şifreleri listeler."""
        if not self.passwords:
            return "Henüz hiçbir şifre eklenmedi!"
        result = "\nKayıtlı Şifreler:\n"
        result += f"{'No':<4}{'Site':<20}{'Kullanıcı Adı':<20}{'Şifre':<20}\n"
        result += "-" * 60 + "\n"
        for index, record in enumerate(self.passwords, start=1):
            result += f"{index:<4}{record['site']:<20}{record['username']:<20}{record['password']:<20}\n"
        return result
