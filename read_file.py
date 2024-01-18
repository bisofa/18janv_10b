def read_and_print_file(file_path):
    try:
       
        with open(file_path, 'r') as file:
           
            content = file.read()
            
            print("Faila saturs:")
            print(content)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. {e}")


file_path = 'piem.txt'
read_and_print_file(file_path)