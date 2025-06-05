# Azure Cognitive Search Lab

Este repositório documenta a prática e aplicação de técnicas com **Azure AI Search** para ingestão, indexação e consulta de grandes volumes de dados. O laboratório foi desenvolvido como parte do desafio "Azure Cognitive Search: Utilizando AI Search para indexação e consulta de Dados".

## 📌 Objetivo

Explorar o uso do **Azure Cognitive Search** para:

* Ingestão inteligente de documentos (estruturados e não estruturados);
* Criação e personalização de índices de busca com enriquecimento por IA;
* Consulta e análise dos dados indexados com técnicas de AI Search.

## 🧠 Tecnologias Utilizadas

* **Azure AI Search (Cognitive Search)**
* **Data Source**: JSON, PDF, HTML, ou Blob Storage
* **Skillsets**: OCR, tradução, extração de chave, entidade nomeada
* **Índices Inteligentes** com enriquecimento semântico
* **Azure Portal, Postman ou SDK (.NET/Python)** para consultas

## 📁 Estrutura do Repositório

```text
azure-cognitive-search-lab/
├── README.md                 # Documentação principal
├── ingestao/                 # Scripts ou anotações da ingestão de dados
├── indexacao/                # Configurações dos índices criados
├── consultas/                # Exemplos de queries e respostas
└── insights.md               # Análise dos resultados e aprendizados
```

## 🧪 Etapas Realizadas

### 1️⃣ Ingestão de Dados

* Upload de documentos no Azure Blob Storage
* Definição de data source no Cognitive Search
* Aplicação de skillset para extração automática de conteúdo e metadados

### 2️⃣ Criação de Índices

* Campos personalizados (ex: título, data, palavras-chave)
* Campos otimizados para buscas semânticas e filtros
* Indexação automática com preview de campos enriquecidos

### 3️⃣ Consultas

* Consulta via Portal Azure e REST API
* Utilização de filtros, ranking, destaque de trechos e sugestões
* Exemplo de pergunta: *"Quais documentos mencionam inteligência artificial e foram criados após 2022?"*

## 🔍 Exemplos

Os exemplos utilizados estão nas pastas `ingestao/`, `indexacao/` e `consultas/`, incluindo:

* Arquivo JSON simulando entrada de dados
* Script de configuração de índice
* Exemplos de queries com respostas

## 📌 Resultados e Benefícios

* Indexação eficiente de grandes volumes de documentos
* Consultas otimizadas com enriquecimento semântico
* Visualização rápida de trechos relevantes nos resultados
* Possibilidade de automação e escalabilidade com pipelines de IA

## 💡 Futuras Explorações

* Integração com bots ou sistemas de atendimento inteligente
* Geração de dashboards analíticos com Power BI sobre dados indexados
* Conexão com modelos generativos para Q\&A em linguagem natural

---

> *Este projeto reforça a aplicabilidade prática do Azure Cognitive Search e serve como base para soluções reais de busca inteligente em ambientes corporativos e acadêmicos.*
