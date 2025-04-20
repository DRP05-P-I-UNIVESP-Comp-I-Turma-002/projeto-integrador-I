# Este é o ponto de entrada da aplicação
# Ele apenas chama a interface principal

from database.estrutura import verificar_coluna_foto
from interface.interface_principal import iniciar_interface

if __name__ == "__main__":
    verificar_coluna_foto()  # <- Adicionamos  após criar o dotorio database!
    iniciar_interface()
