import random
import time
import math
import matplotlib.pyplot as plt
from googleapiclient.discovery import build

def pobierz_dlugosci_komentarzy(api_key, video_ids, max_comments_per_video):
    youtube = build('youtube', 'v3', developerKey=api_key)

    wszystkie_dlugosci_komentarzy = []

    for video_id in video_ids:
        # Pobierz pierwsze 100 komentarzy
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100
        )
        response = request.execute()

        while 'items' in response and len(wszystkie_dlugosci_komentarzy)<max_comments_per_video:
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comment_length = len(comment)
                wszystkie_dlugosci_komentarzy.append(comment_length)

            if 'nextPageToken' in response:
                # Jeżeli istnieje kolejna strona komentarzy, pobierz ją
                request = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    maxResults=100,
                    pageToken=response['nextPageToken']
                )
                response = request.execute()
            else:
                # Jeżeli nie ma kolejnej strony, zakończ pętlę
                break
    
    return wszystkie_dlugosci_komentarzy



  #       for item in response['items']:
  #          komentarz = item['snippet']['topLevelComment']['snippet']['textDisplay']
  #          dlugosc_komentarza = len(komentarz)
  #          wszystkie_dlugosci_komentarzy.append(dlugosc_komentarza)
#
  #          # Pobierz odpowiedzi na dany komentarz
  #          if 'replies' in item:
  #              for reply in item['replies']['comments']:
  #                  tekst_odpowiedzi = reply['snippet']['textDisplay']
  #                  dlugosc_odpowiedzi = len(tekst_odpowiedzi)
  #                  wszystkie_dlugosci_komentarzy.append(dlugosc_odpowiedzi)
#
  #  # Zamieszaj długości komentarzy
  #  #random.shuffle(wszystkie_dlugosci_komentarzy)
#
  #  return wszystkie_dlugosci_komentarzy

def generuj_liczby_binarne(liczby):
    liczby_binarne = []

    for liczba in liczby:
        if liczba % 2 == 0:
            liczby_binarne.append(0)
        else:
            liczby_binarne.append(1)
    return liczby_binarne

def konwertuj_do_4_bitowych(liczby_bin):
    liczby_4_bitowe = []
    aktualna_liczba = 0

    while len(liczby_bin) >= 4:############################################################################################### 4/8
        aktualna_partia = liczby_bin[:4]###################################################################################### 4/8
        aktualna_liczba = 0

        for bit in aktualna_partia:
            aktualna_liczba = (aktualna_liczba << 1) | bit

        liczby_4_bitowe.append(aktualna_liczba)
        liczby_bin = liczby_bin[4:]########################################################################################### 4/8

    return liczby_4_bitowe

# Ustaw klucz API YouTube Data
api_key = 'AIzaSyA7eDRVuoOcMC8qBK2MKh43B4rhCv7xVZo'

# Identyfikatory filmów
video_ids = [
    '9P5FA3Em1P8',
    'gdZLi9oWNZg',
    'jNQXAC9IVRw',
    'WMweEpGlu_U',
    'XsX3ATc3FbA',
    'MBdVXkSdhwU',
    '9bZkp7q19f0',
    '-5q5mZbe3V8',
    'ioNng23DkIM',
    'kffacxfA7G4',
]

# Ustaw maksymalną liczbę komentarzy do pobrania dla każdego filmu


# Pobierz długości poszczególnych komentarzy i odpowiedzi
# dlugosci_komentarzy = pobierz_dlugosci_komentarzy(api_key, video_ids, max_comments_per_video)

# Sprawdź, czy liczby są parzyste czy nieparzyste i wygeneruj liczby binarne
#liczby_bin = generuj_liczby_binarne(dlugosci_komentarzy)

# Konwertuj liczby binarne na 4-bitowe
# liczby_4_bitowe = konwertuj_do_4_bitowych(liczby_bin)


# Wyświetl zamieszane identyfikatory filmów i liczby 4-bitowe
#for i, (video_id, liczba) in enumerate(zip(video_ids, liczby_4_bitowe), start=1):
#    print(f"Film {i}: {video_id} | Liczba 4-bitowa: {liczba}")

def generuj_rozklad(numbers):
    # Licz entropię
    rozklad = {}
    for number in numbers:
        rozklad[number] = rozklad.get(number, 0) + 1

    rozklad = {k: v / len(numbers) for k, v in rozklad.items()}

    # Wygeneruj wykres
    plt.bar(rozklad.keys(), rozklad.values())
    plt.xlim(0, 200)
    plt.xlabel('Dlugosc komentarza')
    plt.ylabel('rozklad')
    plt.title('Wykres rozkladu')
    plt.show()

def generuj_rozklad_dzwon(numbers):
    # Licz entropię
    rozklad = {}
    for number in numbers:
        rozklad[number] = rozklad.get(number, 0) + 1

    rozklad = {k: v / len(numbers) for k, v in rozklad.items()}

    # Wygeneruj wykres
    x = list(rozklad.keys())
    y = list(rozklad.values())
    
    # Separate odd and even values
    odd_x = [num for num in x if num % 2 == 1]
    odd_y = [rozklad[num] for num in odd_x]
    even_x = [num for num in x if num % 2 == 0]
    even_y = [rozklad[num] for num in even_x]
    
    plt.bar(odd_x, odd_y, color='red', label='Odd')
    plt.bar(even_x, even_y, color='blue', label='Even')
    
    plt.xlim(-200, 200)
    plt.xlabel('Dlugosc komentarza')
    plt.ylabel('Rozklad')
    plt.title('Wykres rozkladu')
    plt.legend()
    plt.show()


# Generuj wykres entropii
def generuj_wykres_entropii(numbers):
    # Licz entropię
    entropia = {}
    for number in numbers:
        if number != 0 and number != 15:################################################################################################# 255/15
            entropia[number] = entropia.get(number, 0) + 1

    entropia = {k: v / len(numbers) for k, v in entropia.items()}


 #   liczba = 0
 #   for number in numbers:
 #       if number != 0 and number != 255:##################################################################################### powinno byc prawdopodobienstwo zamiast wartosci
 #           liczba +=  number*math.log2(number)
 #   liczba = liczba*(-1)
 #   print(f"{liczba}")


    # Wygeneruj wykres
    plt.bar(entropia.keys(), entropia.values())
    plt.xlabel('Liczba 4-bitowa')################################################################################################################### 4/8
    plt.ylabel('Czestotliwosc wystepowania')
    plt.title('Empiryczny rozkład zmiennych losowych po post-procesingu')
    plt.show()

# Wygeneruj wykres entropii uzyskanych wyników
def generuj_wyniki(ile_ma_wygenerowac, bin_file_path):
    poprzedni_wynik = int(time.time() * 1000)
    
    max_comments_per_video = (ile_ma_wygenerowac/10)*4

    rozklad_lista = []
    entropia_lista = []

    
    binaryFile = open(bin_file_path, "ab")

    
    

    for video_id in video_ids:
        random.seed(poprzedni_wynik)  # Ustaw ziarno na poprzedni wynik + czas systemowy w milisekundach

        # Pobierz długości komentarzy dla danego filmu
        dlugosci_komentarzy = pobierz_dlugosci_komentarzy(api_key, [video_id], max_comments_per_video)
        # Sprawdź, czy liczby są parzyste czy nieparzyste i wygeneruj liczby binarne
        liczby_bin = generuj_liczby_binarne(dlugosci_komentarzy)
        random.shuffle(liczby_bin)
        # Konwertuj liczby binarne na 4-bitowe
        liczby_4_bitowe = konwertuj_do_4_bitowych(liczby_bin)
        for liczba in dlugosci_komentarzy:
            rozklad_lista.append(liczba)
        for liczba in liczby_4_bitowe:
            if liczba != 0 and liczba != 15:######################################################################################################## 255/15
                #print(f"Film: {video_id} | Liczba 4-bitowa: {liczba}")
                binaryFile.write(bytes(liczba)) ############################################################################### 8/4
            entropia_lista.append(liczba)
            # Oblicz nowy poprzedni wynik
            poprzedni_wynik = liczba


    #generuj_rozklad(rozklad_lista)
    #generuj_rozklad_dzwon(rozklad_lista)
    #generuj_wykres_entropii(entropia_lista)

    binaryFile.close()
        
# Fun generująca wyniki
#generuj_wyniki(10)