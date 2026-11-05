import streamlit as st
from datetime import date

# --------------------------------------------------
# CONFIGURAÇÃO E IDENTIDADE VISUAL
# --------------------------------------------------

st.set_page_config(
    page_title="InovaSUS Connect",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #F5F8F6;
}
[data-testid="stSidebar"] {
    background: #123047;
}
[data-testid="stSidebar"] * {
    color: white !important;
}
.hero {
    background: linear-gradient(120deg, #123047, #126D70);
    padding: 36px;
    border-radius: 20px;
    color: white;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 38px;
    margin-bottom: 8px;
}
.hero p {
    color: #DDF4EC;
    font-size: 17px;
}
.section-title {
    color: #123047;
    font-size: 25px;
    font-weight: 800;
    margin: 12px 0 20px 0;
}
.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #E1EAE6;
    min-height: 115px;
}
.metric-number {
    color: #0F8B8D;
    font-size: 30px;
    font-weight: 800;
}
.metric-label {
    color: #526875;
    font-size: 13px;
}
.challenge-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #DFEAE5;
    margin-bottom: 12px;
}
.tag {
    background: #DDF4EC;
    color: #126D70;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}
.stButton button[kind="primary"] {
    background: #0F8B8D;
    border: none;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# DADOS DEMONSTRATIVOS
# --------------------------------------------------

if "desafios" not in st.session_state:
    st.session_state.desafios = [
        {
            "titulo": "Baixa adesão de idosos ao tratamento da hipertensão",
            "instituicao": "UBS Esperança",
            "area": "Saúde do idoso",
            "descricao": "Desenvolver estratégias educativas e tecnológicas para melhorar a adesão ao tratamento.",
            "status": "Aberto"
        },
        {
            "titulo": "Dificuldade de acesso à saúde ginecológica",
            "instituicao": "UBS Centro",
            "area": "Saúde da mulher",
            "descricao": "Pensar soluções para ampliar o acesso a consultas e procedimentos ginecológicos.",
            "status": "Aberto"
        },
        {
            "titulo": "Fragilidade na comunicação entre equipes da APS",
            "instituicao": "Unidade de Saúde Norte",
            "area": "Atenção Primária",
            "descricao": "Criar ferramentas para facilitar a comunicação e a continuidade do cuidado.",
            "status": "Em andamento"
        }
    ]

if "talentos" not in st.session_state:
    st.session_state.talentos = [
        {"nome": "Ana Souza", "curso": "Enfermagem", "habilidade": "Saúde coletiva"},
        {"nome": "Lucas Lima", "curso": "Engenharia de Software", "habilidade": "Programação"},
        {"nome": "Marina Alves", "curso": "Design", "habilidade": "Design thinking"},
        {"nome": "Pedro Costa", "curso": "Medicina", "habilidade": "Atenção à saúde"}
    ]

if "equipes" not in st.session_state:
    st.session_state.equipes = []

if "projetos" not in st.session_state:
    st.session_state.projetos = [
        {
            "nome": "Hipertensão em Rede",
            "desafio": "Baixa adesão de idosos ao tratamento da hipertensão",
            "fase": "Empatia",
            "resumo": "Estratégia de acompanhamento e educação em saúde para pessoas idosas."
        }
    ]

if "avaliacoes" not in st.session_state:
    st.session_state.avaliacoes = []


# --------------------------------------------------
# MENU LATERAL
# --------------------------------------------------

st.sidebar.markdown("## 🌱 InovaSUS")
st.sidebar.caption("CONNECT | INOVAÇÃO EM SAÚDE")
st.sidebar.markdown("---")

pagina = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Início",
        "💡 Mural de desafios",
        "🧩 Talentos e equipes",
        "🚀 Trilha empreendedora",
        "🏆 Vitrine de soluções",
        "📊 Avaliação"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("*Conectando conhecimento,*")
st.sidebar.markdown("*transformando o SUS.*")
st.sidebar.caption("Plataforma demonstrativa | MVP acadêmico")


# --------------------------------------------------
# PÁGINA INICIAL
# --------------------------------------------------

if pagina == "🏠 Início":

    st.markdown("""
    <div class="hero">
        <h1>InovaSUS Connect 🌱</h1>
        <p>Conectando conhecimento, transformando o SUS.</p>
        <p>Uma rede colaborativa que transforma desafios reais da saúde pública
        em soluções inovadoras, sustentáveis e socialmente relevantes.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    indicadores = [
        (len(st.session_state.desafios), "Desafios cadastrados"),
        (len(st.session_state.talentos), "Talentos na rede"),
        (len(st.session_state.equipes), "Equipes formadas"),
        (len(st.session_state.projetos), "Projetos em desenvolvimento")
    ]

    for coluna, (numero, legenda) in zip([c1, c2, c3, c4], indicadores):
        with coluna:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{numero}</div>
                <div class="metric-label">{legenda}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">Como funciona a inovação colaborativa?</div>',
                unsafe_allow_html=True)

    etapas = st.columns(5)
    passos = [
        ("01", "Identificar", "Mapear problemas reais do SUS."),
        ("02", "Conectar", "Reunir pessoas e competências."),
        ("03", "Desenvolver", "Criar soluções colaborativas."),
        ("04", "Validar", "Testar ideias na prática."),
        ("05", "Transformar", "Compartilhar resultados.")
    ]

    for col, (numero, titulo, descricao) in zip(etapas, passos):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{numero}</div>
                <b style="color:#123047">{titulo}</b>
                <p style="font-size:13px;color:#526875">{descricao}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("### 🎯 Nosso propósito")
    st.write(
        "Aproximar universidades e serviços públicos de saúde, "
        "promovendo aprendizagem baseada em problemas, inovação aberta "
        "e empreendedorismo social."
    )

    st.info("Explore o menu lateral para conhecer os módulos da plataforma.")


# --------------------------------------------------
# MURAL DE DESAFIOS
# --------------------------------------------------

elif pagina == "💡 Mural de desafios":

    st.markdown('<div class="section-title">💡 Mural de desafios do SUS</div>',
                unsafe_allow_html=True)

    st.write("Problemas reais dos serviços de saúde podem se transformar em oportunidades de inovação.")

    with st.expander("＋ Cadastrar novo desafio", expanded=False):
        with st.form("form_desafio"):
            titulo = st.text_input("Título do desafio")
            instituicao = st.text_input("Instituição ou serviço de saúde")
            area = st.selectbox(
                "Área temática",
                ["Atenção Primária", "Saúde da mulher", "Saúde do idoso",
                 "Saúde mental", "Gestão em saúde", "Tecnologia em saúde",
                 "Saúde da criança", "Outra"]
            )
            descricao = st.text_area("Descreva o problema identificado")
            enviar = st.form_submit_button("Publicar desafio", type="primary")

            if enviar:
                if titulo.strip() and instituicao.strip() and descricao.strip():
                    st.session_state.desafios.append({
                        "titulo": titulo,
                        "instituicao": instituicao,
                        "area": area,
                        "descricao": descricao,
                        "status": "Aberto"
                    })
                    st.success("Desafio cadastrado!")
                else:
                    st.warning("Preencha título, instituição e descrição.")

    busca = st.text_input("🔎 Buscar desafios", placeholder="Digite uma palavra-chave")

    for i, desafio in enumerate(st.session_state.desafios):
        if busca.lower() in (desafio["titulo"] + desafio["area"] + desafio["descricao"]).lower():
            st.markdown(f"""
            <div class="challenge-card">
                <span class="tag">{desafio['area']}</span>
                <h3 style="color:#123047">{desafio['titulo']}</h3>
                <p style="color:#526875">📍 {desafio['instituicao']}</p>
                <p>{desafio['descricao']}</p>
                <b style="color:#0F8B8D">● {desafio['status']}</b>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Excluir desafio", key=f"excluir_desafio_{i}"):
                st.session_state.desafios.pop(i)
                st.rerun()


# --------------------------------------------------
# TALENTOS E EQUIPES
# --------------------------------------------------

elif pagina == "🧩 Talentos e equipes":

    st.markdown('<div class="section-title">🧩 Matchmaking de talentos</div>',
                unsafe_allow_html=True)

    st.write("Conecte estudantes de diferentes áreas a partir de suas competências.")

    with st.expander("＋ Cadastrar talento"):
        with st.form("form_talento"):
            nome = st.text_input("Nome do estudante")
            curso = st.selectbox(
                "Curso",
                ["Enfermagem", "Medicina", "Fisioterapia", "Psicologia",
                 "Farmácia", "Engenharia de Software", "Design",
                 "Administração", "Outro"]
            )
            habilidade = st.text_input("Principal habilidade ou competência")
            enviar_talento = st.form_submit_button("Cadastrar talento")

            if enviar_talento:
                if nome.strip() and habilidade.strip():
                    st.session_state.talentos.append({
                        "nome": nome,
                        "curso": curso,
                        "habilidade": habilidade
                    })
                    st.success("Talento cadastrado!")
                else:
                    st.warning("Preencha todos os campos.")

    st.markdown("### Pessoas disponíveis na rede")

    colunas = st.columns(2)
    for i, talento in enumerate(st.session_state.talentos):
        with colunas[i % 2]:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style="color:#123047">👤 {talento['nome']}</h3>
                <p>{talento['curso']}</p>
                <span class="tag">{talento['habilidade']}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 🤝 Formar equipe")

    with st.form("form_equipe"):
        nome_equipe = st.text_input("Nome da equipe")
        integrantes = st.multiselect(
            "Selecione os integrantes",
            [t["nome"] for t in st.session_state.talentos]
        )
        desafio_equipe = st.selectbox(
            "Desafio relacionado",
            [d["titulo"] for d in st.session_state.desafios]
        )
        criar_equipe = st.form_submit_button("Criar equipe", type="primary")

        if criar_equipe:
            if nome_equipe.strip() and integrantes:
                st.session_state.equipes.append({
                    "nome": nome_equipe,
                    "integrantes": integrantes,
                    "desafio": desafio_equipe
                })
                st.success("Equipe criada!")
            else:
                st.warning("Informe o nome da equipe e pelo menos um integrante.")

    if st.session_state.equipes:
        st.markdown("### Equipes formadas")
        for equipe in st.session_state.equipes:
            st.markdown(f"*{equipe['nome']}* — {equipe['desafio']}")
            st.caption("Integrantes: " + ", ".join(equipe["integrantes"]))


# --------------------------------------------------
# TRILHA EMPREENDEDORA
# --------------------------------------------------

elif pagina == "🚀 Trilha empreendedora":

    st.markdown('<div class="section-title">🚀 Trilha empreendedora</div>',
                unsafe_allow_html=True)

    st.write("Um espaço de aprendizagem para transformar problemas em soluções.")

    fases = [
        ("1. Empatia", "Compreender as necessidades dos usuários e profissionais do SUS.",
         "Mapa de empatia", "O que as pessoas sentem, pensam, falam e fazem?"),
        ("2. Ideação", "Gerar possibilidades e selecionar ideias inovadoras.",
         "Brainstorming", "Quais soluções podem responder ao desafio?"),
        ("3. Prototipação", "Construir uma representação inicial da solução.",
         "Protótipo", "Como podemos representar nossa ideia de forma simples?"),
        ("4. Validação", "Testar a solução e coletar contribuições dos usuários.",
         "Plano de validação", "Como saberemos se a solução funciona?"),
        ("5. Pitch final", "Apresentar a proposta, seus impactos e sua viabilidade.",
         "Apresentação", "Qual problema resolvemos e qual transformação propomos?")
    ]

    for titulo, descricao, ferramenta, pergunta in fases:
        with st.expander(titulo):
            st.write(descricao)
            st.markdown(f"*Ferramenta:* {ferramenta}")
            st.info(pergunta)

    st.markdown("### Registrar avanço de um projeto")

    if st.session_state.projetos:
        with st.form("form_fase"):
            projeto_selecionado = st.selectbox(
                "Projeto",
                [p["nome"] for p in st.session_state.projetos]
            )
            nova_fase = st.selectbox(
                "Etapa alcançada",
                ["Empatia", "Ideação", "Prototipação", "Validação", "Pitch final"]
            )
            registrar_fase = st.form_submit_button("Atualizar etapa")

            if registrar_fase:
                for projeto in st.session_state.projetos:
                    if projeto["nome"] == projeto_selecionado:
                        projeto["fase"] = nova_fase
                st.success("Etapa atualizada!")
    else:
        st.info("Cadastre um projeto na Vitrine de Soluções para acompanhar sua evolução.")


# --------------------------------------------------
# VITRINE DE SOLUÇÕES
# --------------------------------------------------

elif pagina == "🏆 Vitrine de soluções":

    st.markdown('<div class="section-title">🏆 Vitrine de soluções</div>',
                unsafe_allow_html=True)

    st.write("Conheça projetos acadêmicos desenvolvidos para responder aos desafios do SUS.")

    with st.expander("＋ Cadastrar novo projeto"):
        with st.form("form_projeto"):
            nome_projeto = st.text_input("Nome do projeto")
            desafio_projeto = st.selectbox(
                "Desafio relacionado",
                [d["titulo"] for d in st.session_state.desafios]
            )
            resumo = st.text_area("Resumo executivo da solução")
            link_pitch = st.text_input("Link do vídeo de apresentação (opcional)")
            cadastrar_projeto = st.form_submit_button("Publicar projeto", type="primary")

            if cadastrar_projeto:
                if nome_projeto.strip() and resumo.strip():
                    st.session_state.projetos.append({
                        "nome": nome_projeto,
                        "desafio": desafio_projeto,
                        "fase": "Empatia",
                        "resumo": resumo,
                        "pitch": link_pitch
                    })
                    st.success("Projeto publicado na vitrine!")
                else:
                    st.warning("Preencha o nome e o resumo do projeto.")

    for projeto in st.session_state.projetos:
        st.markdown(f"""
        <div class="challenge-card">
            <span class="tag">{projeto['fase']}</span>
            <h3 style="color:#123047">🚀 {projeto['nome']}</h3>
            <p><b>Desafio:</b> {projeto['desafio']}</p>
            <p>{projeto['resumo']}</p>
        </div>
        """, unsafe_allow_html=True)

        if projeto.get("pitch"):
            st.markdown(f"[▶️ Assistir ao pitch]({projeto['pitch']})")


# --------------------------------------------------
# AVALIAÇÃO
# --------------------------------------------------

elif pagina == "📊 Avaliação":

    st.markdown('<div class="section-title">📊 Avaliação das soluções</div>',
                unsafe_allow_html=True)

    st.write("Espaço demonstrativo para avaliação acadêmica e potencial de implementação.")

    if st.session_state.projetos:
        with st.form("form_avaliacao"):
            projeto_avaliado = st.selectbox(
                "Projeto avaliado",
                [p["nome"] for p in st.session_state.projetos]
            )
            avaliador = st.text_input("Nome do avaliador ou professor")
            inovacao = st.slider("Grau de inovação", 0, 10, 5)
            viabilidade = st.slider("Viabilidade de implementação", 0, 10, 5)
            impacto = st.slider("Potencial de impacto social", 0, 10, 5)
            feedback = st.text_area("Comentários e recomendações")
            piloto = st.checkbox("Recomendo desenvolver um projeto-piloto")

            enviar_avaliacao = st.form_submit_button("Registrar avaliação", type="primary")

            if enviar_avaliacao:
                if avaliador.strip():
                    st.session_state.avaliacoes.append({
                        "projeto": projeto_avaliado,
                        "avaliador": avaliador,
                        "inovacao": inovacao,
                        "viabilidade": viabilidade,
                        "impacto": impacto,
                        "feedback": feedback,
                        "piloto": piloto
                    })
                    st.success("Avaliação registrada!")
                else:
                    st.warning("Informe o nome do avaliador.")

        if st.session_state.avaliacoes:
            st.markdown("### Avaliações registradas")
            for avaliacao in st.session_state.avaliacoes:
                media = (
                    avaliacao["inovacao"] +
                    avaliacao["viabilidade"] +
                    avaliacao["impacto"]
                ) / 3

                st.markdown(f"*{avaliacao['projeto']}*")
                st.write(f"Avaliador: {avaliacao['avaliador']}")
                st.write(f"Nota média: {media:.1f}/10")
                st.write(f"Recomenda piloto: {'Sim' if avaliacao['piloto'] else 'Não'}")
                if avaliacao["feedback"]:
                    st.caption(avaliacao["feedback"])
                st.divider()
    else:
        st.info("Ainda não existem projetos cadastrados.")


# --------------------------------------------------
# RODAPÉ
# --------------------------------------------------

st.markdown("---")
st.markdown(
    "<center style='color:#71858D;font-size:12px'>"
    "InovaSUS Connect • Inovação aberta • Educação • Empreendedorismo social"
    "</center>",
    unsafe_allow_html=True
)
