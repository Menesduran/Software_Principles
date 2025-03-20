#Separation of Concerns (SoC) – Ayrı Sorumluluklar İlkesi

#Bu ilke, bir yazılım sistemindeki farklı işlevlerin (örneğin, veri işleme, kullanıcı girişi, çıktı gösterme) ayrı bileşenlere bölünmesini savunur.

#Neden önemli?

#Kod daha düzenli olur.
#Değişiklik yapmak daha kolaydır.
#Bakımı ve test edilmesi daha pratiktir.


# 1) Kullanıcıdan giriş alma (Input)
def get_name():
    return input("Enter your name: ")

# 2️) Veriyi işleme (Processing)
def create_greeting(name):
    return f"Hello, {name}! Welcome to the system."

# 3️) Sonucu ekrana yazdırma (Output)
def display_message(message):
    print(message)

# Ana program
def main():
    name = get_name()  # Kullanıcıdan isim al
    greeting = create_greeting(name)  # Mesajı oluştur
    display_message(greeting)  # Mesajı ekrana yazdır

if __name__ == "__main__":
    main()