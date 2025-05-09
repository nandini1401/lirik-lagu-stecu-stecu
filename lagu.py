import time
import sys

def print_karaoke_style():
    lyrics = [
        # Verse 1
        (["Aduh", "abang", "bukan", "maksudku", "begitu"], [0.3, 0.3, 0.4, 0.4, 0.8]),
        (["Masalah", "stecu", "bukan", "brarti", "tak", "mau"], [0.4, 0.4, 0.3, 0.3, 0.3, 0.8]),
        (["Jual", "mahal", "dikit", "kan", "bisa"], [0.3, 0.3, 0.3, 0.3, 0.8]),
        (["Coba", "kase", "effortnya", "saja"], [0.3, 0.3, 0.5, 1.0]),
        
        # Bridge
        (["Kalo", "memang", "cocok", "bisa", "datang", "ke", "rumah"], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1.0]),
        
        # Chorus
        (["Stecu", "stecu", "stelan", "cuek", "baru", "malu"], [0.3, 0.3, 0.4, 0.4, 0.3, 0.8]),
        (["Adu", "ade", "ini", "mau", "juga", "abang", "yang", "rayu"], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 1.0]),
        (["Stecu", "stecu", "stelan", "cuek", "baru", "malu"], [0.3, 0.3, 0.4, 0.4, 0.3, 0.8]),
        (["Adu", "ade", "ini", "mau", "juga", "abang", "yang", "maju"], [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 2.0]),
    ]

    for words, delays in lyrics:
        if not words[0]:
            time.sleep(delays[0])
            print()
        else:
            for word, delay in zip(words, delays):
                print(word, end=' ', flush=True) 
                time.sleep(delay)
            print()  
            time.sleep(0.3)  

print("✨ Stecu ✨")
time.sleep(1)
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print_karaoke_style()

