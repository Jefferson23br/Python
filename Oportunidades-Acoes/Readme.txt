# Analisador de Ações da B3

Este é um script Python que analisa todas as ações da B3, obtendo os preços históricos de cada ativo e calculando a máxima e mínima dos preços. Caso o preço atual de uma ação seja inferior a 70% da sua máxima, o script registra a ação como possível compra e cria um gráfico para análise. Caso haja erro ao processar algum ativo, o erro também é registrado para posterior verificação.

## Funcionalidades

- **Análise de Ações da B3**: O script coleta informações sobre todas as ações listadas na B3 e analisa seus preços históricos.
- **Análise de Preço Atual**: Compara o preço atual de cada ação com o preço máximo histórico, identificando oportunidades de compra quando o preço atual for inferior a 70% da máxima.
- **Geração de Gráficos**: Cria gráficos para ajudar na análise visual das ações com possíveis oportunidades de compra.
- **Registro de Erros**: Caso algum erro ocorra durante o processamento de um ativo, o script registra o erro para análise posterior.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `matplotlib`
  - `yfinance`
  - `numpy`
  - `requests`

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

pip install pandas matplotlib yfinance numpy requests

Como Executar o Script
Para rodar o script diretamente em seu terminal (CMD), basta seguir os seguintes passos:

Clone o repositório ou baixe os arquivos para o seu computador.

Abra o terminal ou CMD.

Navegue até o diretório onde o script está localizado.

Execute o script com o seguinte comando:

python nome_do_script.py
Criando um Executável (.exe)
Se você preferir criar um executável .exe para rodar o script sem precisar do Python instalado, siga as instruções abaixo:

Instale o PyInstaller:

pip install pyinstaller
Crie o executável executando o seguinte comando no terminal dentro da pasta do script:

pyinstaller --onefile nome_do_script.py
Isso criará um executável nome_do_script.exe na pasta dist/ que pode ser executado diretamente em qualquer máquina Windows.

Como Funciona o Script
O script começa coletando a lista de ações da B3.

Para cada ação, ele obtém os preços históricos usando a biblioteca yfinance.

O script calcula a máxima e mínima dos preços históricos.

Compara o preço atual com a máxima histórica:

Se o preço atual for menor que 70% da máxima histórica, ele registra a ação como possível compra.

Para ações com oportunidades de compra, o script gera um gráfico de preços históricos para visualização.

Caso ocorra um erro ao processar algum ativo, o erro é registrado em um arquivo de log.

Contribuição
Se você deseja contribuir com melhorias, fique à vontade para fazer um fork do repositório e enviar um pull request. Certifique-se de seguir as melhores práticas e de que o código está bem documentado.

Licença
Este projeto é licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
