# Desafio Criativo — Acelerando a Produtividade Comercial com IA

## Projeto: Assistente de Produtividade Comercial com IA

**Autor:** Marcelo Santos  
**Plataforma:** DIO.me  
**Tema:** Inteligência Artificial aplicada à produtividade e inteligência comercial B2B

---

## 1. Contexto e Objetivo

Este projeto foi desenvolvido como parte de um desafio prático da DIO.me sobre o uso de Inteligência Artificial para simplificar tarefas e aumentar a produtividade.

O cenário escolhido foi a rotina de uma equipe comercial B2B. A proposta é utilizar IA como um **Assistente de Produtividade Comercial**, capaz de receber indicadores e alertas previamente calculados e transformá-los em uma agenda priorizada de atuação para vendedores e gestores.

```text
Dados comerciais
        ↓
Indicadores e alertas
        ↓
Inteligência Artificial
        ↓
Priorização
        ↓
Plano de ação comercial
```

---

## 2. Passo 1 — Intenção

> Quero que a IA gere um plano diário priorizado de ações comerciais para vendedores e gestores comerciais, com o objetivo de direcionar o tempo da equipe para os clientes e oportunidades que apresentam maior necessidade de atenção ou potencial de resultado.

O problema não é apenas disponibilizar indicadores, mas ajudar a responder: **qual cliente merece atenção primeiro, qual é a evidência e qual ação deve ser executada?**

---

## 3. Passo 2 — Contexto e Restrições

O cenário considera informações como cliente, vendedor, região, última compra, recência, frequência, faturamento, ticket médio, ciclo histórico de recompra, variações recentes de comportamento e alertas comerciais previamente calculados.

A IA deve utilizar somente as informações fornecidas, organizar as ações por prioridade Alta, Média ou Baixa, apresentar a evidência que sustenta cada prioridade e diferenciar situações de risco de oportunidades.

Também foram estabelecidas restrições para impedir que a IA invente clientes, números, indicadores ou causas. Quando a causa de uma mudança não estiver nos dados, ela deve ser tratada como hipótese a ser investigada.

> **A IA não deve inventar o risco. Os indicadores e alertas fornecem a evidência; a IA organiza, prioriza e transforma essa evidência em ação comercial.**

---

## 4. Passo 3 — Prompt Final

```text
Você é um Assistente de Produtividade Comercial especializado em operações B2B.

Analise os clientes, indicadores, alertas e oportunidades comerciais fornecidos e produza um plano de ação priorizado para o vendedor ou gestor comercial, com o objetivo de direcionar seu tempo para as atividades com maior necessidade de atenção ou potencial de resultado.

Considere, quando disponíveis, informações como cliente, vendedor, região, última compra, recência, frequência, faturamento, ticket médio, ciclo histórico de recompra, variações recentes de comportamento e alertas comerciais previamente calculados.

Classifique cada ação como prioridade Alta, Média ou Baixa.

Para cada ação apresente:
1. Cliente
2. Situação identificada
3. Evidência disponível
4. Prioridade
5. Ação recomendada
6. Objetivo da ação

Ao final, apresente uma seção chamada "Agenda Comercial Prioritária", contendo no máximo cinco ações que merecem atenção primeiro.

Priorize situações sustentadas por evidências, como clientes fora do próprio ciclo histórico de recompra, redução relevante de frequência ou ticket, contas importantes com mudança de comportamento e oportunidades de recompra identificadas pelos dados.

Não invente clientes, números, causas ou informações ausentes. Não trate hipóteses como fatos. Caso uma possível causa não possa ser determinada pelos dados, indique-a explicitamente como hipótese que deve ser investigada pelo vendedor.

Não crie novos indicadores estatísticos nem altere os valores recebidos. Utilize os indicadores e alertas fornecidos como evidência para organizar e priorizar as ações.

Utilize linguagem executiva, objetiva e orientada à ação. Evite explicações teóricas extensas e recomendações genéricas.
```

---

## 5. Validação Prática

O prompt foi testado em um novo chat, sem contexto adicional, usando uma carteira fictícia com cinco clientes e diferentes situações.

| Cliente | Situação principal |
|---|---|
| Ômega Beleza | Conta relevante fora do ciclo histórico de recompra |
| Alfa Distribuidora | Fora do ciclo de recompra e com redução do ticket |
| Gama Comércio | Redução relevante do ticket |
| Delta Perfumaria | Próxima do ciclo habitual de recompra |
| Beta Cosméticos | Sem alerta ou alteração negativa relevante |

### Resultado

| Ordem | Cliente | Prioridade | Evidência principal |
|---:|---|---|---|
| 1 | Ômega Beleza | Alta | 73 dias de recência frente ao ciclo médio de 32 dias e R$ 228.000 de faturamento em 12 meses |
| 2 | Alfa Distribuidora | Alta | 52 dias de recência frente ao ciclo de 28 dias e ticket recente de R$ 9.800 frente a R$ 16.900 histórico |
| 3 | Gama Comércio | Alta | Ticket recente de R$ 7.100 frente a R$ 12.400 histórico |
| 4 | Delta Perfumaria | Média | 21 dias de recência para ciclo médio de 22 dias, caracterizando oportunidade próxima de recompra |
| 5 | Beta Cosméticos | Baixa | Nenhum alerta e ausência de mudança negativa relevante nos dados fornecidos |

Um resultado relevante ocorreu com Ômega Beleza. A IA recomendou investigar o motivo do afastamento **sem presumir a causa**, respeitando a restrição definida no prompt.

---

## 6. Avaliação do Teste

O teste foi avaliado em três dimensões:

**Priorização:** a IA colocou no topo os clientes com evidências mais relevantes de mudança de comportamento.

**Aderência às evidências:** utilizou recência, ciclo de recompra, faturamento, ticket médio e alertas fornecidos, sem precisar inventar novos indicadores.

**Controle de inferências:** não afirmou que preço, concorrência, insatisfação ou outro fator desconhecido causou a mudança de comportamento.

Também houve diferenciação entre **risco** e **oportunidade**: Delta Perfumaria foi tratada como oportunidade de recompra, e não como cliente problemático.

---

## 7. Aprendizados

O experimento mostrou que IA pode ser utilizada para organizar decisões operacionais a partir de evidências estruturadas.

Uma separação importante é:

```text
Motor analítico
      ↓
Calcula indicadores
Identifica alertas
Produz evidências

      ↓

Assistente de IA
      ↓
Interpreta
Prioriza
Organiza
Recomenda ações
```

Essa arquitetura reduz o risco de utilizar a IA generativa como fonte dos próprios indicadores.

---

## 8. Evolução Futura

O conceito pode evoluir para:

```text
Histórico de vendas
        ↓
RFM / RFMT
        ↓
Ciclo de recompra
        ↓
Alertas de comportamento
        ↓
Assistente de IA
        ↓
Agenda Comercial Prioritária
        ↓
Ação do vendedor
        ↓
Registro do resultado
```

O histórico das ações poderá futuramente permitir medir quais alertas anteciparam perda de clientes, quais ações resultaram em recompra, o tempo entre alerta e novo pedido e a efetividade das recomendações.

---

## 9. Tecnologias e Conceitos

- Inteligência Artificial Generativa
- Engenharia de Prompts
- Inteligência Comercial
- Produtividade Comercial
- B2B
- RFM / RFMT
- Ciclo de Recompra
- Priorização de Clientes
- Markdown
- GitHub

---

## Conclusão

O desafio demonstrou que um prompt estruturado pode transformar indicadores comerciais em uma rotina de atuação mais objetiva.

O objetivo não é substituir a decisão do vendedor ou gestor, mas reduzir o esforço necessário para identificar onde concentrar atenção.

> **Dados mostram o que está acontecendo. Indicadores estruturam a evidência. A IA pode ajudar a transformar essa evidência em prioridade e ação.**

O teste também reforçou a necessidade de estabelecer restrições explícitas para evitar que a IA invente causas, números ou justificativas ausentes nos dados.

