import streamlit as st
from datetime import date

st.set_page_config(
    page_title="InovaSUS Connect",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# IDENTIDADE VISUAL
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #F5F7F6;
}
[data-testid="stSidebar"] {
    background: #123047;
}
[data-testid="stSidebar"] * {
    color: #F5F8FA !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #D6E5E9 !important;
}
h1, h2, h3 {
    color: #123047;
    font-family: 'Manrope', sans-serif;
}
.hero {
    background: linear-gradient(120deg, #123047 0%, #17616B 100%);
    padding: 35px 38px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 8px;
}
.hero p {
    color: #D9EEEE;
    font-size: 16px;
}
.eyebrow {
    color: #F4A340;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.metric-card {
    background: white;
    border: 1px solid #E5EBE9;
    border-radius: 16px;
    padding: 20px;
    min-height: 125px;
    box-shadow: 0 3px 12px rgba(18,48,71,.04);
}
.metric-label {
    color: #647782;
    font-size: 13px;
    font-weight: 600;
}
.metric-number {
    color: #123047;
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    font-weight: 800;
    margin-top: 8px;
}
.metric-icon {
    font-size: 22px;
}
.project-card {
    background: white;
    border: 1px solid #E5EBE9;
    border-radius: 16px;
    padding: 21px;
    margin-bottom: 12px;
}
.tag {
    display: inline-block;
    background: #DDF4EC;
    color: #176B62;
    padding: 5px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 700;
}
.small-muted {
    color: #71818A;
    font-size: 13px;
}
div.stButton > button {
    border-radius: 10px;
    border: 0;
    background: #0F8B8D;
    color: white;
    font-weight: 700;
    padding: 9px 18px;
}
div.stButton > button:hover {
    background: #0B6F72;
    color: white;
}
.stTextInput input, .stTextArea textarea, .stSelectbox div,
.stDateInput input {
    border-radius: 10px;
}
hr {
    border-color: #E5EBE9;
}
</style>
""", unsafe_allow_html=True)

# DADOS DEMONSTRATIVOS
if "desafios" not in st.session_state:
    st.session_state.desafios = [
        {
            "titulo": "Reduzir faltas às consultas na APS",
            "area": "Atenção Primária",
            "instituicao": "Unidade Básica de Saúde",
            "descricao": "Desenvolver estratégias para melhorar a adesão dos usuários às consultas agendadas.",
            "status": "Aberto"
        },
        {
            "titulo": "Melhorar a educação em saúde da mulher",
            "area": "Saúde da Mulher",
            "instituicao": "Secretaria Municipal de Saúde",
            "descricao": "Criar recursos educativos acessíveis sobre saúde ginecológica e autocuidado.",
            "status": "Aberto"
        },
        {
            "titulo": "Qualificar o acolhimento na rede pública",
            "area": "Humanização",
            "instituicao": "Serviço de Saúde",
            "descricao": "Propor soluções para tornar o acolhimento mais resolutivo e humanizado.",
            "status": "Em desenvolvimento"
        }
    ]

if "talentos" not in st.session_state:
    st.session_state.talentos = []

if "projetos" not in st.session_state:
    st.session_state.projetos = [
        {
            "nome": "Acolhe SUS",
            "area": "Humanização",
            "etapa": "Ideação",
            "descricao": "Proposta de melhoria do acolhimento nos serviços de saúde."
        },
        {
            "nome": "Saúde em Rede",
            "area": "Atenção Primária",
            "etapa": "Prototipação",
            "descricao": "Estratégia digital de educação e comunicação em saúde."
        }
    ]

# MENU LATERAL
with st.sidebar:
    st.markdown("""
    <div style="padding:18px 5px 25px 5px;">
        <div style="font-size:30px;">💡</div>
        <div style="font-family:Manrope;font-size:21px;font-weight:800;">
            InovaSUS <span style="color:#54D6C5;">Connect</span>
        </div>
        <div style="font-size:11px;color:#B8D4D9;">
            INOVAÇÃO ABERTA EM SAÚDE PÚBLICA
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    pagina = st.radio(
        "NAVEGAÇÃO",
        [
            "Visão geral",
            "Mural de desafios",
            "Talentos e equipes",
            "Trilha empreendedora",
            "Vitrine de soluções",
            "Avaliação de projetos"
        ],
        label_visibility="visible"
    )

    st.markdown("---")
    st.markdown(
        "<div style='font-size:12px;color:#B8D4D9;'>"
        "Conectando conhecimento,<br>transformando o SUS.</div>",
        unsafe_allow_html=True
    )

# CABEÇALHO DA PÁGINA
def cabecalho(titulo, subtitulo):
    st.markdown(f"""
    <div style="margin-bottom:24px;">
        <div class="eyebrow">INOVASUS CONNECT</div>
        <h1 style="margin:5px 0;">{titulo}</h1>
        <p style="color:#71818A;margin-top:0;">{subtitulo}</p>
    </div>
    """, unsafe_allow_html=True)

def cartao(indicador, numero, icone):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">{icone}</div>
        <div class="metric-label">{indicador}</div>
        <div class="metric-number">{numero}</div>
    </div>
    """, unsafe_allow_html=True)

# VISÃO GERAL
if pagina == "Visão geral":
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">INOVAÇÃO • COLABORAÇÃO • IMPACTO SOCIAL</div>
        <h1>Ideias que transformam<br>o futuro do SUS.</h1>
        <p>Uma rede colaborativa que conecta desafios reais dos serviços
        públicos de saúde ao conhecimento acadêmico e à inovação.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Panorama da inovação")
    a, b, c, d = st.columns(4)

    with a:
        cartao("Desafios cadastrados", len(st.session_state.desafios), "🎯")
    with b:
        cartao("Talentos conectados", len(st.session_state.talentos), "👥")
    with c:
        cartao("Projetos em andamento", len(st.session_state.projetos), "🚀")
    with d:
        cartao("Soluções apresentadas", 0, "💡")

    st.write("")
    esquerda, direita = st.columns([1.35, 1])

    with esquerda:
        st.subheader("Desafios em destaque")
        for item in st.session_state.desafios[:3]:
            st.markdown(f"""
            <div class="project-card">
                <span class="tag">{item['area']}</span>
                <h3 style="margin:12px 0 5px 0;">{item['titulo']}</h3>
                <div class="small-muted">{item['instituicao']}</div>
                <p>{item['descricao']}</p>
            </div>
            """, unsafe_allow_html=True)

    with direita:
        st.subheader("Como funciona?")
        etapas = [
            ("01", "Empatia", "Identificação de necessidades reais do SUS."),
            ("02", "Ideação", "Construção coletiva de propostas inovadoras."),
            ("03", "Prototipação", "Desenvolvimento de soluções iniciais."),
            ("04", "Validação", "Avaliação e aprimoramento das propostas."),
            ("05", "Pitch", "Apresentação das soluções e impacto esperado.")
        ]
        for numero, nome, descricao in etapas:
            st.markdown(f"""
            <div class="project-card" style="padding:13px 17px;">
                <span style="color:#0F8B8D;font-weight:800;">{numero}</span>
                <b style="color:#123047;margin-left:10px;">{nome}</b>
                <div class="small-muted" style="margin-top:5px;">{descricao}</div>
            </div>
            """, unsafe_allow_html=True)

# MURAL DE DESAFIOS
elif pagina == "Mural de desafios":
    cabecalho("Mural de desafios", "Problemas reais dos serviços de saúde que podem se transformar em inovação.")

    with st.expander("＋ Publicar novo desafio", expanded=False):
        with st.form("novo_desafio"):
            titulo = st.text_input("Título do desafio")
            area = st.selectbox("Área temática", [
                "Atenção Primária", "Saúde da Mulher", "Saúde da Criança",
                "Saúde do Idoso", "Saúde Mental", "Gestão em Saúde",
                "Humanização", "Tecnologia em Saúde", "Outra"
            ])
            instituicao = st.text_input("Instituição ou serviço de saúde")
            descricao = st.text_area("Descreva o problema identificado")
            enviar = st.form_submit_button("Publicar desafio")

            if enviar:
                if titulo and descricao:
                    st.session_state.desafios.append({
                        "titulo": titulo,
                        "area": area,
                        "instituicao": instituicao or "Instituição não informada",
                        "descricao": descricao,
                        "status": "Aberto"
                    })
                    st.success("Desafio cadastrado!")
                else:
                    st.warning("Preencha o título e a descrição.")

    st.write("")
    busca = st.text_input("🔎 Buscar desafios", placeholder="Digite uma palavra-chave...")
    for i, item in enumerate(st.session_state.desafios):
        if busca.lower() in (item["titulo"] + item["area"] + item["descricao"]).lower():
            with st.container(border=True):
                st.markdown(f"*{item['titulo']}*")
                st.markdown(f"<span class='tag'>{item['area']}</span>", unsafe_allow_html=True)
                st.caption(f"{item['instituicao']} • {item['status']}")
                st.write(item["descricao"])
                if st.button("Tenho interesse", key=f"interesse_{i}"):
                    st.info("Interesse registrado para demonstração.")

# TALENTOS E EQUIPES
elif pagina == "Talentos e equipes":
    cabecalho("Talentos e equipes", "Conecte pessoas, competências e conhecimentos para desenvolver soluções.")

    st.subheader("Cadastre seu perfil colaborativo")
    with st.form("cadastro_talento"):
        nome = st.text_input("Nome")
        instituicao = st.text_input("Universidade ou instituição")
        curso = st.text_input("Curso ou área de atuação")
        habilidades = st.multiselect(
            "Suas principais competências",
            ["Enfermagem", "Medicina", "Fisioterapia", "Nutrição",
             "Psicologia", "Tecnologia", "Design", "Gestão",
             "Pesquisa", "Educação em Saúde", "Comunicação"]
        )
        enviar = st.form_submit_button("Cadastrar talento")

        if enviar:
            if nome and curso:
                st.session_state.talentos.append({
                    "nome": nome,
                    "instituicao": instituicao,
                    "curso": curso,
                    "habilidades": habilidades
                })
                st.success("Perfil cadastrado com sucesso!")
            else:
                st.warning("Informe seu nome e sua área de atuação.")

    st.divider()
    st.subheader("Rede de talentos")
    if st.session_state.talentos:
        for pessoa in st.session_state.talentos:
            with st.container(border=True):
                st.markdown(f"*👤 {pessoa['nome']}*")
                st.caption(f"{pessoa['curso']} • {pessoa['instituicao']}")
                st.write("Competências: " + ", ".join(pessoa["habilidades"]))
    else:
        st.info("Os talentos cadastrados aparecerão aqui.")

# TRILHA EMPREENDEDORA
elif pagina == "Trilha empreendedora":
    cabecalho("Trilha empreendedora", "Transforme um problema em uma solução com potencial de impacto no SUS.")

    fases = {
        "Empatia": "Compreenda o contexto, escute os usuários e identifique necessidades.",
        "Ideação": "Gere possibilidades e selecione propostas com potencial de transformação.",
        "Prototipação": "Construa uma versão inicial da solução.",
        "Validação": "Teste a proposta com usuários e profissionais do serviço.",
        "Pitch": "Apresente a solução, sua viabilidade e seu impacto esperado."
    }

    etapa = st.selectbox("Selecione a etapa de desenvolvimento", list(fases.keys()))
    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">TRILHA DE DESENVOLVIMENTO</div>
        <h1>{etapa}</h1>
        <p>{fases[etapa]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Workspace do projeto")
    nome_projeto = st.text_input("Nome do projeto")
    problema = st.text_area("Qual problema sua equipe pretende resolver?")
    proposta = st.text_area("Qual solução vocês estão propondo?")
    proximo_passo = st.text_area("Qual será o próximo passo da equipe?")

    if st.button("Salvar informações da etapa"):
        st.success("Informações registradas nesta demonstração.")

# VITRINE DE SOLUÇÕES
elif pagina == "Vitrine de soluções":
    cabecalho("Vitrine de soluções", "Conheça projetos e propostas desenvolvidos pela rede colaborativa.")

    with st.expander("＋ Cadastrar solução"):
        with st.form("nova_solucao"):
            nome = st.text_input("Nome da solução")
            area = st.selectbox("Área de atuação", [
                "Atenção Primária", "Saúde da Mulher", "Humanização",
                "Gestão em Saúde", "Tecnologia em Saúde", "Outra"
            ])
            descricao = st.text_area("Apresentação da solução")
            etapa = st.selectbox("Etapa atual", [
                "Ideação", "Prototipação", "Validação", "Implementação"
            ])
            enviar = st.form_submit_button("Adicionar à vitrine")

            if enviar:
                if nome and descricao:
                    st.session_state.projetos.append({
                        "nome": nome,
                        "area": area,
                        "etapa": etapa,
                        "descricao": descricao
                    })
                    st.success("Projeto adicionado à vitrine!")
                else:
                    st.warning("Informe o nome e a apresentação.")

    st.write("")
    col1, col2 = st.columns(2)
    for i, projeto in enumerate(st.session_state.projetos):
        with [col1, col2][i % 2]:
            with st.container(border=True):
                st.markdown("💡")
                st.markdown(f"### {projeto['nome']}")
                st.markdown(f"<span class='tag'>{projeto['area']}</span>", unsafe_allow_html=True)
                st.write(projeto["descricao"])
                st.caption(f"Etapa: {projeto['etapa']}")

# AVALIAÇÃO
elif pagina == "Avaliação de projetos":
    cabecalho("Avaliação de projetos", "Analise o potencial de inovação, viabilidade e impacto das soluções.")

    if not st.session_state.projetos:
        st.info("Cadastre projetos na vitrine antes de avaliá-los.")
    else:
        nomes = [p["nome"] for p in st.session_state.projetos]
        selecionado = st.selectbox("Projeto para avaliação", nomes)
        projeto = next(p for p in st.session_state.projetos if p["nome"] == selecionado)

        st.markdown(f"### {projeto['nome']}")
        st.write(projeto["descricao"])
        st.divider()

        st.subheader("Critérios de avaliação")
        inovacao = st.slider("Potencial de inovação", 0, 10, 5)
        viabilidade = st.slider("Viabilidade de execução", 0, 10, 5)
        impacto = st.slider("Impacto potencial no SUS", 0, 10, 5)
        sustentabilidade = st.slider("Sustentabilidade da proposta", 0, 10, 5)
        feedback = st.text_area("Comentários e recomendações")

        if st.button("Finalizar avaliação"):
            media = (inovacao + viabilidade + impacto + sustentabilidade) / 4
            st.success(f"Avaliação registrada nesta demonstração. Média: {media:.1f}/10")
            st.write("*Recomendação:* " +
                     ("Potencial para desenvolvimento piloto." if media >= 7
                      else "Necessita de aprimoramentos antes do piloto."))
            if feedback:
                st.write("*Feedback:*", feedback)

st.markdown("""
<div style="text-align:center;padding:35px 0 15px 0;color:#829199;font-size:12px;">
    INOVASUS CONNECT • Conectando conhecimento, transformando o SUS.
</div>
""", unsafe_allow_html=True)