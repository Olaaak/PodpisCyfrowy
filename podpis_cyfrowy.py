import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.backends import default_backend
from Crypto.PublicKey import RSA





import ytscraper100


def wygeneruj_rsa(bin_file_path):
    
    #ytscraper100.generuj_wyniki(1000, bin_file_path)

    with open(bin_file_path, 'rb') as file:

        # Generowanie klucza prywatnego

        klucz_prywatny = RSA.generate(2048, file.read)
        prywatny = klucz_prywatny.export_key()
        with open('klucz_prywatny.pem', 'wb') as plik_pryw:
            plik_pryw.write(prywatny)

        #generowanie klucza publicznego

        publiczny = klucz_prywatny.publickey().export_key()
        with open('klucz_publiczny.pem', 'wb') as plik_pub:
            plik_pub.write(publiczny)

        print("Klucz RSA wygenerowany i zapisany")

        return klucz_prywatny



# Funkcja realizująca podpisanie wybranego pliku


def podpisz(klucz_prywatny_plik, plik_do_podpisu, podpis):

    # załadowanie klucza prywatnego z pliku
    with open(klucz_prywatny_plik, "rb") as klucz:
        klucz_prywatny = serialization.load_pem_private_key(
            klucz.read(),
            password=None,
            backend=default_backend()
        )

    with open(plik_do_podpisu, 'rb') as plik:
        file_data = plik.read()

        sha3_hash = hashlib.sha3_256(file_data).digest()

        #podpisanie pliku

        signature = klucz_prywatny.sign(
            sha3_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA3_256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA3_256()
        )

        # zapisanie do pliku
        with open(podpis, 'wb') as podpis_plik:
            podpis_plik.write(signature)

        return True



#Funkcja weryfikująca poprawnosć podpisu cyfrowego



def sprawdz(klucz_publiczny_plik, plik, podpis):
    try:
        with open(klucz_publiczny_plik, 'rb') as klucz_publiczny_plik1, \
                open(plik, 'rb') as plik1, \
                open(podpis, 'rb') as podpis1:
            
        

            klucz_publiczny = serialization.load_pem_public_key(
                klucz_publiczny_plik1.read(),
                backend=default_backend()
            )

         
            plik_d = plik1.read()
            podpis3 = podpis1.read()

            sha3_hash = hashlib.sha3_256(plik_d).digest()

            try:
                klucz_publiczny.verify(
                    podpis3,
                    sha3_hash,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA3_256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA3_256()
                )

                return True

            except Exception:
                return False

    except IOError:
        print(f"Błąd odczytu pliku")


wygeneruj_rsa('TrueRNG.bin')

wynik_podpisz = podpisz('klucz_prywatny.pem', '1.jpg', 'podpis.bin')

if wynik_podpisz:
        print("Plik podpisany.")


wynik_sprawdz = sprawdz('klucz_publiczny.pem', '1.jpg', 'podpis.bin')

if wynik_sprawdz:
        print("Podpis cyfrowy jest poprawny.")
else:
        print("Podpis cyfrowy jest niepoprawny.")