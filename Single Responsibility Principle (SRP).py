#Single Responsibility Principle (SRP) – Tek Sorumluluk İlkesi

#Bu ilkeye göre, her sınıf veya fonksiyon tek bir sorumluluğa sahip olmalıdır.

#Neden önemli?

#Bir sınıf veya fonksiyonun amacı net olur.
#Kod tekrar kullanılabilir hale gelir.
#Güncellenmesi ve genişletilmesi kolaylaşır.

def save_user_to_database(username):
    # Veritabanına kaydetme işlemi
    print(f"User {username} saved to database.")

def send_email(email):
    # Email gönderme işlemi
    print(f"Sending email to {email}.")

# Fonksiyonları kullanma
save_user_to_database("Muhammet Enes Duran")
send_email("muhammetenesduran@gmail.com")