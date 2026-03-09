def calculator_frecuency_words(text):
    
    frecuency={}
    words = text.split()
    
    for i in words:
        if not(i in frecuency):
            frecuency[i] = 0
            
        frecuency[i]+=1
    
    
        
    return frecuency


def create_report(dic):
    with open("report_top10.txt", "w", encoding="utf-8") as f:
        
        f.write("══════════════════════════════════════\n")
        f.write("        📊 Top 10 Palabras 📊          \n")
        f.write("══════════════════════════════════════\n\n")

        for i, (word, frec) in enumerate(dic.items()):
            if not(i < 10):
                break
            f.write(f"{i+1:2}. {word:<12} → {frec} veces\n")

        f.write("\n══════════════════════════════════════\n")

print(" Report saved as 'report_top10.txt'")
  
    
        
def to_show_top_10(dic):
    order = dict(sorted(dic.items(), key = lambda x:x[1], reverse=True))
    print("==============================")
    print("   📊   Top 10 words   📊   ")
    print("==============================")
    for i, (word, frec) in enumerate(order.items()):
        if not( i < 10):
            break
        
        print(f"{i+1:2}. {word:<10} → {frec} veces")
    
    print("===============================")
    create_report(order)
    
    
    
    
    