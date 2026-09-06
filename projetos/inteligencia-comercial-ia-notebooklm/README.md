# Miniguia de Estudos com NotebookLM
## Inteligência Comercial com IA — RFM, Churn e Comportamento de Compra B2B

**Autor:** Marcelo Santos  
**Plataforma:** DIO.me  
**Ferramenta principal:** Google NotebookLM  
**Tema:** Inteligência Artificial aplicada à Inteligência Comercial

---

## 1. Contexto e Objetivos

Este projeto foi desenvolvido como parte de um desafio prático da DIO.me com o objetivo de utilizar Inteligência Artificial como ferramenta de aprendizagem ativa.

O tema escolhido foi **Inteligência Comercial com IA**, com foco em como históricos de vendas podem apoiar a identificação de mudanças relevantes no comportamento de clientes, riscos de inatividade e oportunidades de recompra.

O estudo buscou responder principalmente:

- Quais indicadores podem ser calculados a partir de históricos de vendas?
- Quais análises podem ser feitas apenas com regras estatísticas?
- Quando o uso de Machine Learning passa a fazer sentido?
- Como evitar generalizações indevidas ao aplicar resultados científicos em cenários B2B?
- Como transformar conceitos de RFM e churn em regras simples, transparentes e auditáveis?
- Como diferenciar fórmulas objetivas, hipóteses de implementação e parâmetros que precisam ser calibrados com dados reais?

A proposta final não foi apenas resumir as fontes, mas construir um **modelo conceitual de MVP de Inteligência Comercial B2B**, priorizando explicabilidade e uso prático.

---

## 2. Curadoria de Fontes

### Fonte 1 — RFM e Segmentação de Clientes
**Recency, Frequency, Monetary Value, Clustering, and Internal and External Indices for Customer Segmentation from Retail Data**  
https://www.mdpi.com/1999-4893/16/9/396

Contribuições: RFM, segmentação de clientes, clustering e perfis de comportamento.

### Fonte 2 — RFMT e Machine Learning
**Customer Analysis Using Machine Learning-Based Classification Algorithms for Effective Segmentation Using Recency, Frequency, Monetary, and Time**  
https://www.mdpi.com/1424-8220/23/6/3180

Contribuições: expansão do RFM com dimensão temporal, intervalo entre compras e segmentação/classificação.

### Fonte 3 — Churn e Machine Learning
**Customer Churn Prediction: A Systematic Review of Recent Advances, Trends, and Challenges in Machine Learning and Deep Learning**  
https://www.mdpi.com/2504-4990/7/3/105

Contribuições: técnicas de churn, desbalanceamento, overfitting, concept drift e interpretabilidade.

### Fonte 4 — IA Explicável aplicada a Churn
**Explainable AI-driven Customer Churn Prediction**  
https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1748799/full

Contribuições: modelos preditivos, explicabilidade e SHAP.

---

## 3. Engenharia de Prompts e “Cicatrizes”

### Tentativa 1 — Fontes incorretas no NotebookLM

**Prompt inicial:**

> Considerando exclusivamente as fontes fornecidas, explique quais indicadores podem ser calculados a partir de um histórico de transações de vendas para identificar clientes que apresentam mudança relevante de comportamento de compra. Separe os indicadores que podem ser implementados por regras estatísticas daqueles que exigem ou podem se beneficiar de Machine Learning.

**Problema encontrado:** o NotebookLM identificou que as fontes carregadas pertenciam a outro estudo, relacionado a computação quântica e otimização de portfólios, e informou corretamente que não havia base suficiente para responder ao tema comercial.

**Cicatriz 01:** antes de avaliar o prompt, é necessário validar se as fontes realmente pertencem ao tema estudado.

---

### Tentativa 2 — Fontes corretas, mas generalização excessiva

Com as fontes adequadas, o NotebookLM identificou Recência, Frequência, Valor Monetário, Tempo Médio entre Compras, clustering, churn, concept drift e IA explicável.

O problema foi que alguns resultados de datasets específicos foram apresentados de forma excessivamente geral, como comportamento de devolução observado em moda B2C, “bill shock” de telecomunicações e sazonalidade baseada em estações do ano.

**Cicatriz 02:** resultados encontrados em um setor ou dataset não devem ser automaticamente transformados em regra geral para qualquer empresa.

---

### Tentativa 3 — Adaptação explícita ao cenário B2B

**Prompt:**

> Com base exclusivamente nas fontes carregadas, avalie criticamente quais dos indicadores e métodos apresentados anteriormente são realmente viáveis para uma empresa B2B que possui apenas histórico de pedidos, clientes, datas, produtos, quantidades, valores, vendedor e região.

A resposta passou a separar os indicadores em três grupos: implementação imediata por regras estatísticas; necessidade de histórico/novas variáveis; e técnicas de Machine Learning dependentes de maior volume e qualidade de dados.

O MVP passou a priorizar Recência, Frequência, Valor Monetário, Tempo Médio entre Compras e comparação do cliente com seu próprio histórico.

Porém, a IA introduziu limites como janela fixa de 12 meses, 1,5 vezes o ciclo de recompra e queda de 40% no ticket sem comprovação universal.

**Cicatriz 03:** uma regra matemática transparente não é necessariamente uma regra validada.

---

### Tentativa 4 — Auditoria da própria solução

**Prompt:**

> Audite criticamente o modelo MVP proposto anteriormente. Identifique todos os números, limites, janelas temporais, pesos, faixas ou critérios definidos sem evidência suficiente para serem considerados regras universais de negócio. Classifique cada parâmetro como fundamentado pelas fontes, hipótese de implementação ou parâmetro que precisa ser calibrado com dados históricos da empresa. Não substitua os parâmetros por novos valores arbitrários.

A auditoria distinguiu fórmulas objetivas, parâmetros configuráveis, hipóteses e regras dependentes de validação empresarial.

**Principal aprendizado:** a IA pode ajudar a propor regras, mas a decisão de negócio exige validação empírica e conhecimento do contexto da empresa.

---

## 4. Miniguia de Estudo

### 4.1 RFM

**Recência (R):** mede há quanto tempo o cliente realizou sua última compra.

```text
Recência = Data Atual - Data da Última Compra
```

**Frequência (F):** mede quantos pedidos o cliente realizou em determinado período.

```text
Frequência = Quantidade de pedidos únicos no período
```

**Monetário (M):** representa o valor financeiro movimentado pelo cliente.

```text
Monetário = Soma do valor das compras
```

R, F e M devem ser analisados em conjunto. Um cliente pode ter alto faturamento histórico e, ainda assim, já estar inativo.

### 4.2 RFMT

A dimensão **T — Time** acrescenta o comportamento temporal. Um indicador particularmente útil em B2B é o **Tempo Médio entre Compras**.

Exemplo:

```text
Pedido 1 → 10/01
Pedido 2 → 25/01 = 15 dias
Pedido 3 → 20/02 = 26 dias
Pedido 4 → 10/03 = 18 dias

T = (15 + 26 + 18) / 3
T = 19,67 dias
```

Esse indicador permite comparar o comportamento atual do cliente com seu próprio padrão histórico.

### 4.3 Análise intra-cliente

Uma das principais conclusões do estudo foi priorizar:

```text
Cliente atual
      versus
Histórico do próprio cliente
```

antes de:

```text
Cliente atual
      versus
Média de toda a carteira
```

Em B2B, clientes podem possuir ciclos de compra muito diferentes. Regras genéricas de dias sem comprar podem gerar falsos positivos.

### 4.4 Alertas auditáveis

Em vez de apresentar apenas:

```text
Risco de churn: 83%
```

um MVP pode explicar:

```text
Tempo médio de recompra: 28 dias
Dias desde a última compra: 47 dias
Parâmetro atual: 1,5 × ciclo histórico
Limite calculado: 42 dias
Situação: cliente ultrapassou seu padrão histórico
```

Isso melhora auditabilidade, confiança e validação das regras.

---

## 5. Estrutura Conceitual do MVP

Campos mínimos:

```text
cliente
pedido
data
produto
quantidade
valor
vendedor
região
```

Indicadores:

```text
R = Recência
F = Frequência
M = Valor Monetário
T = Tempo Médio entre Compras
```

Análises possíveis:

- cliente fora do seu ciclo histórico de recompra;
- queda relevante de ticket;
- redução de frequência;
- clientes novos que não realizaram segunda compra;
- contas relevantes em processo de inatividade.

---

## 6. Parâmetros Configuráveis

O estudo mostrou que limites de negócio não devem ficar fixos no código.

Exemplos:

```text
H = janela histórica
k_ciclo = tolerância do ciclo de recompra
W_curto = janela recente
k_retração = limite relativo de queda de ticket
k_novo = multiplicador de monitoramento de novo cliente
```

Esses parâmetros devem ser calibrados com dados históricos e regras reais da empresa.

---

## 7. Quando usar Machine Learning

Machine Learning pode ser útil futuramente para:

- segmentação multidimensional;
- classificação de risco de churn;
- detecção de padrões não lineares;
- concept drift;
- previsão de comportamento;
- explicabilidade por técnicas como SHAP.

Seu uso deve ocorrer apenas quando houver histórico suficiente, qualidade de dados, definição clara de churn e capacidade de medir falsos positivos e falsos negativos.

---

## 8. Glossário

**RFM:** Recency, Frequency e Monetary Value.  
**RFMT:** extensão do RFM com dimensão temporal.  
**Recência:** tempo desde a última compra.  
**Frequência:** quantidade de compras ou pedidos realizados.  
**Monetário:** valor financeiro movimentado pelo cliente.  
**Inter-Purchase Time:** intervalo entre compras consecutivas.  
**Churn:** perda ou abandono de um cliente.  
**Clustering:** agrupamento de clientes com características semelhantes.  
**K-Means:** algoritmo de agrupamento não supervisionado.  
**XGBoost / LightGBM:** algoritmos supervisionados usados em classificação.  
**Concept Drift:** mudança ao longo do tempo no comportamento ou distribuição dos dados.  
**SHAP:** método de explicabilidade para estimar a contribuição das variáveis em uma previsão.  
**Outlier:** observação muito diferente do comportamento geral da base.  
**Overfitting:** quando um modelo aprende excessivamente os dados de treinamento e perde capacidade de generalização.  
**MVP:** Minimum Viable Product — produto mínimo viável.  
**Hipótese de implementação:** regra ou parâmetro ainda não validado empiricamente.  
**Parâmetro configurável:** valor alterável conforme características da empresa.  
**Regra auditável:** regra cujo cálculo e justificativa podem ser compreendidos pelo usuário.

---

## 9. Prompts Reutilizáveis

### Prompt para análise de fontes

> Considerando exclusivamente as fontes fornecidas, explique quais indicadores podem ser calculados para analisar o comportamento de clientes. Diferencie técnicas estatísticas de métodos de Machine Learning e cite as fontes utilizadas.

### Prompt para avaliar aplicabilidade

> Analise criticamente quais técnicas apresentadas nas fontes são realmente aplicáveis ao cenário descrito. Destaque variáveis ausentes, limitações e riscos de generalização.

### Prompt para evitar generalizações

> Identifique quais conclusões estão baseadas em datasets ou setores específicos e não podem ser generalizadas automaticamente para outro negócio. Reescreva essas conclusões de forma mais cautelosa.

### Prompt para auditoria de regras

> Identifique todos os números, limites, pesos e janelas temporais propostos. Classifique cada um como evidência das fontes, hipótese ou parâmetro que precisa de calibração.

### Prompt para construção de MVP

> Proponha uma versão mínima da solução utilizando apenas os dados explicitamente disponíveis. Priorize regras simples, transparentes, explicáveis e auditáveis. Não utilize Machine Learning quando regras estatísticas forem suficientes.

---

## 10. Principais Aprendizados

O processo realizado foi:

```text
Perguntar
   ↓
Verificar as fontes
   ↓
Questionar a resposta
   ↓
Identificar generalizações
   ↓
Refinar o prompt
   ↓
Auditar as regras propostas
   ↓
Separar evidência de hipótese
   ↓
Transformar conhecimento em aplicação prática
```

O principal aprendizado foi que **pensamento crítico continua indispensável mesmo quando a resposta da IA parece tecnicamente sofisticada**.

Uma resposta pode estar bem escrita, conter fórmulas e referências e ainda assim introduzir parâmetros arbitrários ou transportar conclusões de um setor para outro sem validação.

---

## 11. Evolução Futura

```text
Dados transacionais
        ↓
RFM / RFMT
        ↓
Indicadores
        ↓
Regras de comportamento
        ↓
Alertas comerciais
        ↓
Validação dos resultados
        ↓
Machine Learning
        ↓
Predição e recomendação
```

A primeira versão deve priorizar explicabilidade e validação. Machine Learning passa a fazer sentido quando o histórico acumulado permitir medir objetivamente se os alertas realmente antecipam perda, recompra ou mudança relevante de comportamento.

---

## 12. Tecnologias e Conceitos

- Google NotebookLM
- Inteligência Artificial
- Engenharia de Prompts
- Curadoria de Fontes
- RFM / RFMT
- Inteligência Comercial
- Churn
- Machine Learning
- IA Explicável
- GitHub
- Markdown

---

## Conclusão

O NotebookLM foi utilizado não apenas para resumir conteúdos, mas como ferramenta de investigação.

A evolução dos prompts permitiu observar quatro níveis de maturidade:

1. validar se as fontes são adequadas;
2. identificar técnicas e conceitos;
3. adaptar os conceitos ao contexto B2B;
4. auditar criticamente as próprias regras produzidas pela IA.

O resultado final foi um miniguia que combina pesquisa, engenharia de prompts, pensamento crítico e aplicação prática em Inteligência Comercial.

