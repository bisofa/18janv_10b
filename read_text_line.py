def read_and_print_third_line(file_path):
    try:
        
        with open(file_path, 'r') as file:
            
            lines = file.readlines()

            
            if len(lines) >= 3:
                
                print("Trešās rindas saturs:")
                print(lines[2])
            else:
                print("Kļūda: Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Kļūda: Fails '{file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. {e}")


file_path = 'piemers2.txt'
read_and_print_third_line(file_path)