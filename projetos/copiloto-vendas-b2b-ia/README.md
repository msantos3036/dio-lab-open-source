# A3 Copiloto de Vendas B2B — IA para Atendimento Comercial

## Tema e objetivo
Projeto para o desafio **Copiloto de Vendas com IA para Atendimento ao Cliente**, da DIO. A solução apoia vendedores B2B depois que um cliente é identificado como oportunidade, risco de inatividade ou possibilidade de recompra.

**Usuário principal:** vendedor B2B e gestor comercial.

**Problema:** transformar contexto e evidências comerciais em uma abordagem de atendimento melhor preparada, sem inventar informações ou substituir a decisão do vendedor.

```text
Cliente priorizado → Contexto comercial → Base de conhecimento
→ Copiloto IA → Abordagem → Objeções → Próxima ação
```

## Abordagem
Foi criado um **copiloto baseado em prompt + base de conhecimento**. O sistema comercial ou motor analítico fornece indicadores e alertas; a IA resume, organiza, sugere perguntas, apoia objeções e recomenda próximos passos.

## Base de conhecimento
A empresa e os produtos deste projeto são fictícios. A pasta `knowledge/` contém:
- `contexto-do-negocio.md`
- `produtos.md`
- `perguntas-frequentes.md`
- `objecoes.md`

## Prompt principal
```text
Você é um Copiloto de Vendas B2B especializado em apoiar vendedores durante o atendimento comercial.

Utilize exclusivamente as informações do cliente e a base de conhecimento fornecida para preparar uma abordagem comercial contextualizada.

Considere informações como histórico de compras, recência, frequência, faturamento, ticket médio, ciclo de recompra, alertas existentes, produtos e informações comerciais disponíveis.

Para cada atendimento, apresente:
1. Resumo objetivo da situação do cliente
2. Evidências comerciais disponíveis
3. Objetivo recomendado para o contato
4. Sugestão de abordagem inicial
5. Perguntas que o vendedor pode fazer para compreender a necessidade
6. Possíveis objeções relacionadas ao contexto
7. Sugestão de resposta para cada objeção
8. Próxima ação recomendada

Não invente informações sobre o cliente, produtos, preços, estoque, condições comerciais ou causas para mudanças de comportamento.
Quando uma informação não estiver disponível, declare a limitação.
Não trate hipóteses como fatos.
Se uma resposta depender de preço, disponibilidade, prazo, desconto ou condição não presente na base, oriente o vendedor a confirmar essa informação antes de responder.
Use linguagem profissional e natural, adequada ao relacionamento B2B.
O objetivo é apoiar o vendedor, não substituir sua decisão ou negociar de forma autônoma.
```

## Simulações
Foram preparados três testes em `simulacoes/`:
1. **Recompra:** cliente próximo do ciclo habitual.
2. **Redução de ticket/ciclo:** mudança de comportamento sem causa conhecida.
3. **Objeção de preço:** resposta sem inventar desconto ou condição comercial.

## Exemplo
**Cliente:** Alfa Distribuidora  
**Recência:** 52 dias  
**Ciclo médio:** 28 dias  
**Ticket histórico:** R$ 16.900  
**Ticket recente:** R$ 9.800  
**Alerta:** fora do ciclo histórico de recompra.

**Resumo esperado:** há mudança de comportamento, mas os dados não informam a causa.

**Abordagem:** “Olá, [nome]. Estou entrando em contato para acompanhar suas necessidades de reposição. Já faz algum tempo desde nosso último pedido e gostaria de entender como está sua demanda atual e se existe algo em que possamos apoiar.”

## Regras de qualidade
- Não inventar fatos, preços, estoque, descontos ou prazos.
- Não presumir causas.
- Distinguir evidência de hipótese.
- Informar limitações.
- Manter a decisão final com o vendedor.

## Evolução futura
```text
Dados → RFM/RFMT → Alertas → Priorização → Copiloto → Atendimento → Resultado
```

Possíveis evoluções: integração com CRM/ERP, recuperação automática do histórico, catálogo integrado, registro de objeções, follow-ups, métricas de conversão e, futuramente, modelos preditivos com histórico suficiente.

## Conclusão
O projeto demonstra como uma base de conhecimento pequena e organizada pode tornar a IA mais contextualizada no atendimento comercial. A inteligência analítica identifica o que merece atenção; o copiloto ajuda o vendedor a transformar esse contexto em uma conversa comercial melhor preparada.

