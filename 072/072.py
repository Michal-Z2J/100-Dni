'''
Napisz program w Pythonie, który zorganizuje pliki tekstowe z folderu "źródłowego" do folderów "docelowych" 
na podstawie ich rozszerzeń. Przykładowo, wszystkie pliki .txt powinny zostać przeniesione do folderu txt, 
a pliki .csv do folderu csv.
Kroki do wykonania zadania:
Utwórz folder źródłowy source oraz kilka plików tekstowych z różnymi rozszerzeniami, takimi jak .txt, .csv i .md.
Napisz program, który:
a. Wyszuka wszystkie pliki tekstowe w folderze źródłowym.
b. Dla każdego pliku utworzy folder docelowy (jeśli jeszcze nie istnieje) na podstawie rozszerzenia pliku.
c. Przeniesie plik do odpowiedniego folderu docelowego.
'''
import os
import shutil
from glob import glob

files = glob("*[!.py]")
print("Znalezione pliki:")

for file in files:
    file_basename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    print(f"Nazwa pliku bez rozszerzenia: {file_basename} - Rozszerzenie pliku: {file_extension}")
    if not os.path.exists(file_extension):
        os.mkdir(file_extension)
        print(f"Utworzono folder {file_extension}")
    else:
        print(f"Folder {file_extension} już istnieje")
    source = f"{file}"
    destination = f"{file_extension}"
    shutil.move(source, destination)
    print(f"Przeniesiono {source} do {destination}")