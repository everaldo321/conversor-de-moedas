Como Utilizar o Conversor de Moedas
Este projeto é uma aplicação interativa de conversão de moedas, desenvolvida com Python e Streamlit. Ele permite que o usuário selecione moedas de origem e destino e insira o valor a ser convertido. O conversor utiliza uma API de câmbio para obter as taxas de conversão em tempo real. Abaixo estão as etapas para usá-lo:

1. Instalação de Dependências
Primeiro, é necessário instalar as dependências necessárias para o projeto. Abra o terminal ou prompt de comando e execute o seguinte comando:

bash
Copiar código
pip install streamlit requests pandas
Esses pacotes incluem o Streamlit (para interface web), Requests (para fazer chamadas à API) e Pandas (para manipulação de dados).

2. Configuração da API
O projeto usa a ExchangeRate-API para obter as taxas de câmbio. Para garantir que funcione corretamente:

API Key: Verifique se há uma chave de API válida no código (API_KEY). Se necessário, registre-se em ExchangeRate-API para obter uma chave.
Endpoint da API: Confirme se o endpoint da API está correto. O código atual usa https://v6.exchangerate-api.com.
3. Executar o Projeto
Após configurar a API e instalar as dependências, execute o aplicativo Streamlit. No terminal, digite:

bash
Copiar código
streamlit run nome_do_arquivo.py
Substitua nome_do_arquivo.py pelo nome do arquivo Python onde o código do projeto está salvo. A aplicação abrirá automaticamente em uma janela do navegador.

4. Usando a Interface
Na interface do conversor, você verá:

Seleção de Moeda: Use os menus suspensos para escolher a moeda de origem e a moeda de destino.
Valor a Converter: Insira o valor que deseja converter.
Botão "Converter": Clique no botão para iniciar a conversão. O aplicativo exibirá o valor convertido e as taxas de câmbio atuais.
Além disso, uma tabela e um gráfico de barras mostrarão as taxas de câmbio de outras moedas para referência.

5. Personalização
O projeto também possui uma seção de CSS para personalização da interface. Para modificar cores, fontes e outros estilos visuais, ajuste o arquivo styles.css e recarregue o aplicativo.

6. Exploração e Atualização
Explore os diferentes valores de conversão e atualize as taxas de câmbio sempre que necessário. Para expandir o projeto, você pode adicionar mais funcionalidades, como a inclusão de mais moedas ou uma opção para salvar as conversões.

Esse guia deve ajudar outros usuários a entender e utilizar o projeto de conversão de moedas com facilidade!











ChatGPT pode cometer erros. Considere ver
