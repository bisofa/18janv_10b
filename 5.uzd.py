def write_name_to_file(file_path, user_name):
    try:
        
        with open(file_path, 'a') as file:
            
            file.write(user_name + '\n')

        print(f"Vārds '{user_name}' veiksmīgi ierakstīts failā {file_path}.")
    except IOError as e:
        print(f"Kļūda: Neizdevās ierakstīt failā. {e}")
    except Exception as e:
        print(f"Kļūda: Nezināma kļūda. {e}")


user_name = input("Ievadiet savu vārdu: ")


file_path = 'lietotajs.txt'


write_name_to_file(file_path, user_name)
