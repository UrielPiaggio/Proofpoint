import read_file
import clear_text as clear
import statistics as stat
import os


def open_file():
    while True:
        path = input("Enter the fila path: ")
        if os.path.exists(path):
            cont = read_file.read_file(path)
            print("Opened successfully...")
            return cont
        
        else:
            print("Error...")
             
        
def main():
    cont=open_file() 
   
    text_normalize = clear.normalize_text(cont)
    
    estadsitica = stat.calculator_frecuency_words(text_normalize)
    
    stat.to_show_top_10(estadsitica)
    
    
if __name__ == "__main__":
    main()