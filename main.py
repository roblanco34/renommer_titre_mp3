import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

# Demande du chemin du dossier à l'utilisateur avec vérification
folder_path = input("Entrez le chemin du dossier contenant les fichiers MP3 : ")
while not os.path.isdir(folder_path):
    print("Chemin invalide. Veuillez entrer un chemin de dossier valide.")
    folder_path = input("Entrez le chemin du dossier contenant les fichiers MP3 : ")

# Liste des fichiers MP3 dans le dossier
mp3_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]

if not mp3_files:
    print("Aucun fichier MP3 trouvé dans le dossier.")
else:
    # Parcours des fichiers MP3
    for filename in mp3_files:
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Chargement des métadonnées du fichier MP3
            audio = MP3(file_path, ID3=EasyID3)
            
            # Extraction du nom de fichier sans extension
            title = os.path.splitext(filename)[0]
            
            # Modification de la propriété "titre"
            audio["title"] = title
            
            # Sauvegarde des modifications
            audio.save()
            print(f"Le titre de '{filename}' a été renommé en '{title}'")
        
        except Exception as e:
            print(f"Erreur lors du traitement du fichier {filename}: {e}")
