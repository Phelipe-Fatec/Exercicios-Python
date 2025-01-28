# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    num = 0
    while True:
        classificacao = 'Seguro'
        if palavras_suspeitas[num] in mensagem:
            classificacao = 'Phishing'
            break
        num += 1
        if num == len(palavras_suspeitas):
            break
    return classificacao
    
        
        
email_usuario = input()

email_usuario = email_usuario.strip()

resultado = verificar_phishing(email_usuario)

print(f"Classificação: {resultado}")