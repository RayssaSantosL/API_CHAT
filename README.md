*Chatbot de Ideias de Startup com OpenAI*

Descrição:
Este script interage com a API do OpenAI para gerar ideias de startup com base nas informações fornecidas pelo usuário. Ele solicita o nome do usuário, suas experiências ou habilidades e o valor que ele está disposto a investir. Em seguida, envia essas informações para a API do OpenAI e exibe as ideias de startup sugeridas pela API.

Módulos utilizados:
- requests: Para fazer solicitações HTTP à API do OpenAI.
- json: Para lidar com dados no formato JSON.

Funções:
- obter_ideias_startup():
    Esta função solicita informações do usuário, como nome, experiências e valor de investimento. Em seguida, monta uma mensagem para enviar à API do OpenAI com essas informações. Após receber a resposta da API, extrai e exibe as ideias de startup sugeridas.

Variáveis:
- API_KEY (str): Chave de API necessária para autenticação na API do OpenAI.
- API_URL (str): URL da API do OpenAI para completar o chat.
- headers (dict): Cabeçalhos necessários para autenticação na API.
- nome (str): Nome do usuário.
- experiencia (str): Experiências ou habilidades do usuário.
- investimento (int): Valor que o usuário está disposto a investir.
- mensagem_usuario (str): Mensagem montada com as informações do usuário para enviar à API.
- corpo_mensagem (dict): Corpo da mensagem em formato JSON para enviar à API.
- corpo_mensagem_json (str): Corpo da mensagem convertido para JSON.
- resposta (Response): Resposta da solicitação à API do OpenAI.
- mensagem_resposta (str): Mensagem de resposta da API contendo as ideias de startup sugeridas.

Uso:
1. Execute o script.
2. Forneça as informações solicitadas pelo programa (nome, experiências e valor de investimento).
3. Aguarde enquanto o programa envia essas informações para a API do OpenAI.
4. Veja as ideias de startup sugeridas pelo programa com base nas informações fornecidas.

Observações:
- Certifique-se de substituir "sua_api_key_aqui" pela sua chave de API real fornecida pela OpenAI.
- Este script assume que a chave de API está armazenada localmente no código. Em um ambiente de produção, é recomendável armazenar a chave de forma segura, como em uma variável de ambiente.

## 🚀 Sobre mim

Olá! Meu nome é Rayssa Santos, tenho 19 anos e sou uma entusiasta da tecnologia com uma paixão ardente pela programação. Atualmente, trabalho como recepcionista, mas estou determinada a mudar meu caminho profissional e embarcar em uma jornada como desenvolvedora de softwares.

Desde cedo, descobri minha fascinação pelo mundo da eletrônica e da administração. Formei-me nessas áreas e, posteriormente, aprimorei meu conhecimento ao concluir um curso de suporte de TI pela Google. Essa trajetória me proporcionou uma base sólida e multifacetada, preparando-me para os desafios dinâmicos que enfrentarei como desenvolvedora.

Além do meu interesse pela tecnologia, sou uma ávida leitora e viajante. Adoro explorar novos lugares e culturas, sempre em busca de inspiração e conhecimento. Minha personalidade é marcada pela paciência, observação e uma comunicação eficaz, habilidades que considero essenciais tanto no desenvolvimento de software quanto no trabalho em equipe.

O que mais me motiva na área de desenvolvimento de software é a constante sensação de desafio e superação. Adoro a emoção de enfrentar problemas complexos e encontrar soluções criativas para eles. Cada linha de código escrita é uma pequena vitória, e a ideia de criar algo que possa impactar positivamente a vida das pessoas me impulsiona ainda mais.

Meu maior objetivo é conquistar uma posição como desenvolvedora de software e, eventualmente, adquirir meu próprio apartamento. Estou comprometida em transformar esse sonho em realidade, dedicando-me incansavelmente ao aprimoramento das minhas habilidades e à busca de novas oportunidades.

Estou animada com a possibilidade de fazer parte de uma equipe dinâmica e inovadora, onde possa colaborar, aprender e crescer profissionalmente. Estou pronta para enfrentar os desafios que surgirem no caminho e ansiosa para contribuir com meu entusiasmo e habilidades para alcançar nossos objetivos em comum.

Obrigada pela oportunidade de me apresentar, e estou ansiosa para futuras conversas!

Atenciosamente,
Rayssa Santos
