# 📝 insights.md

Durante a realização do laboratório, foram obtidos os seguintes aprendizados e observações:

## 🔎 Comparativo entre documentos indexados

| Documento                    | Categoria   | Destaques encontrados           | Qualidade da resposta |
|------------------------------|-------------|----------------------------------|------------------------|
| doc001 - IA na Indústria     | Tecnologia  | "modelos de linguagem", "IA"     | Alta                   |
| doc002 - Relatório Q1 2024  | Finanças    | "EBITDA", "crescimento de mercado"| Alta                   |

## 📌 Insights Técnicos

- O uso de **skillsets cognitivos** melhora significativamente a qualidade da indexação, permitindo a extração de entidades e metadados relevantes automaticamente.
- A configuração de **sugestores (suggesters)** permite implementar recursos tipo autocomplete e sugestões em tempo real com base nos campos indexados.
- A aplicação de **filtros por data e categoria** torna as consultas mais eficazes e precisas.

## ⚠️ Desafios encontrados

- Documentos muito longos podem exceder limites de tokenização e demandam pré-processamento.
- A escolha de *analyzers* (ex: `pt.microsoft`) impacta diretamente na qualidade semântica das buscas.

---

> _Este projeto reforça a aplicabilidade prática do Azure Cognitive Search e serve como base para soluções reais de busca inteligente em ambientes corporativos e acadêmicos._
