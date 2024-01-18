import csv

def read_and_print_second_column(csv_file_path):
    try:
        
        with open(csv_file_path, 'r', newline='') as csvfile:
            
            csv_reader = csv.reader(csvfile)
            
            
            print("Otrās kolonnas dati:")
            for row in csv_reader:
                if len(row) >= 2:
                    print(row[1])
    except FileNotFoundError:
        print(f"Kļūda: Fails '{csv_file_path}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt CSV failu. {e}")


csv_file_path = 'piemers.csv'
read_and_print_second_column(csv_file_path)