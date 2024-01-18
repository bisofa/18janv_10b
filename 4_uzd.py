def read_file_by_extension():
    try:
        
        file_name = input("Ievadiet faila nosaukumu: ")
        file_extension = input("Ievadiet faila paplašinājumu: ")

        
        file_path = f"{file_name}.{file_extension}"

        
        with open(file_path, 'r') as file:
            
            content = file.read()

            
            print(f"\nFaila saturs ({file_path}):")
            print(content)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. {e}")


read_file_by_extension()
